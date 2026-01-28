code = """import json
import re

# Load data from stored files
civic_docs_data = json.load(open(var_functions.query_db:60))
funding_data = json.load(open(var_functions.query_db:48))

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Look for park project names
        if 'Park' in line and len(line) > 5:
            # Skip headers and metadata
            skip_patterns = ['Subject:', 'Page', 'Item', 'To:', 'From:', 'Date:']
            if any(pattern in line for pattern in skip_patterns):
                continue
            if line.startswith('('):
                continue
            
            # Check following lines for completion in 2022
            next_lines = lines[i:i+15]
            next_text = ' '.join(next_lines)
            
            # If completed in 2022, add to list
            if 'completed' in next_text.lower() and '2022' in next_text:
                park_projects.append(line)

# Remove duplicates
unique_projects = list(set(park_projects))

# Find funding matches
total_funding = 0
matches = []

for project in unique_projects:
    project_lower = project.lower()
    for fund_rec in funding_data:
        fund_name = fund_rec.get('Project_Name', '')
        fund_amount = int(fund_rec.get('Amount', 0))
        
        # If project name is part of funding record name
        if project_lower in fund_name.lower():
            total_funding += fund_amount
            matches.append([project, fund_name, fund_amount])

result = {
    'project_count': len(unique_projects),
    'total_funding': total_funding,
    'projects': unique_projects,
    'funding_matches': matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
