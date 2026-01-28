code = """import json
import re

# Load data from file paths
civic_docs = json.load(open('/tmp/tmpu9m4oj6r.json'))
funding = json.load(open('/tmp/tmpg3x0v1j7.json'))

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names containing Park
        if 'Park' in line and len(line) > 5:
            # Skip headers and metadata
            skip_patterns = ['Subject', 'Page', 'Item', 'To:', 'From:', 'Date:', 'Agenda', 'Commission', 'Public Works']
            is_header = any(pattern in line for pattern in skip_patterns)
            
            if not is_header and not line.startswith('(') and not line.startswith('cid'):
                # Look ahead for completion status and date
                next_section = '\n'.join(lines[i:i+15])
                lower_next = next_section.lower()
                
                # Check if completed in 2022
                if re.search(r'completed[^\n]*2022|2022[^\n]*completed|november\s+2022|december\s+2022', lower_next):
                    park_projects_2022.append(line)

# Remove duplicates
unique_projects = list(set(park_projects_2022))

# Find funding matches
total_funding = 0
matches = []

for project in unique_projects:
    project_lower = project.lower()
    for fund_rec in funding:
        fund_name = fund_rec.get('Project_Name', '')
        fund_amount = int(fund_rec.get('Amount', 0))
        
        # Check if this project matches the funding record
        if project_lower in fund_name.lower():
            total_funding += fund_amount
            matches.append({
                'project': project,
                'funding_name': fund_name,
                'amount': fund_amount
            })

result = {
    'project_count': len(unique_projects),
    'total_funding': total_funding,
    'projects': unique_projects,
    'matches': matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json'}

exec(code, env_args)
