code = """import json
import re

# Load the civic documents document data
civic_docs_data = var_functions.query_db:5
if isinstance(civic_docs_data, str):
    with open(civic_docs_data, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_data

# Load the latest funding data
funding_data = var_functions.query_db:48
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding = json.load(f)
else:
    funding = funding_data

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Look for project names containing Park
        if 'Park' in line and len(line) > 5 and not line.startswith('('):
            # Skip header metadata
            if any(skip in line for skip in ['Subject:', 'Page', 'Item', 'To:', 'From:', 'Date:', 'Public Works', 'Commission', 'Agenda']):
                continue
            
            # Check following lines for completion in 2022
            next_lines = lines[i:i+15]
            next_text = ' '.join(next_lines)
            
            # Look for completion indicators and 2022
            lower_next = next_text.lower()
            if ('completed' in lower_next or 'completion' in lower_next) and '2022' in next_text:
                # Additional check - avoid future projects
                if 'to be completed' not in lower_next and 'scheduled' not in lower_next:
                    park_projects_2022.append(line)

# Remove duplicates
unique_projects = list(set(park_projects_2022))

# Find funding matches
funding_matches = []
total_funding = 0

for project in unique_projects:
    for fund in funding:
        fund_name = fund.get('Project_Name', '')
        # Use case-insensitive matching
        if project.lower() in fund_name.lower():
            amount = int(fund.get('Amount', 0))
            total_funding += amount
            funding_matches.append({
                'project': project,
                'funding_name': fund_name,
                'amount': amount
            })

result = {
    'park_projects_completed_2022': unique_projects,
    'project_count': len(unique_projects),
    'total_funding': total_funding,
    'matches': funding_matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
