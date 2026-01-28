code = """import json
import os

# Load the data
mongo_file = globals()['var_functions.query_db:5']
funding_file = globals()['var_functions.query_db:20']

# Load data (handle both file paths and direct data)
if isinstance(mongo_file, str) and mongo_file.endswith('.json'):
    with open(mongo_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = mongo_file

if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_file

# Build funding map
funding_map = {}
for record in funding_records:
    name = record['Project_Name'].strip()
    amount = int(record['Amount'])
    funding_map[name] = amount

spring_projects = []
matched_funding = 0

# Process documents
for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Look for Spring 2022
    if 'spring 2022' in lower_text or 'mar 2022' in lower_text or 'apr 2022' in lower_text or 'may 2022' in lower_text:
        lines = text.split('\n')
        
        current_project = None
        for line in lines:
            line_lower = line.lower().strip()
            
            # Try to identify project name
            if (len(line) > 5 and not line.startswith('(') and not line.startswith('▪') and 
                not any(x in line_lower for x in ['project schedule', 'updates:', 'complete design:', 'begin construction:', 'advertise:']) and
                ':' not in line):
                current_project = line.strip()
            
            # Check for Spring 2022 in schedule line
            if current_project and '2022' in line:
                if 'spring 2022' in line_lower or 'mar 2022' in line_lower or 'apr 2022' in line_lower or 'may 2022' in line_lower:
                    # Remove duplicates
                    if current_project not in [p['name'] for p in spring_projects]:
                        spring_projects.append({'name': current_project})

# Match with funding
matches = []
for proj in spring_projects:
    proj_name = proj['name']
    
    # Direct match
    if proj_name in funding_map:
        amount = funding_map[proj_name]
        matches.append({'name': proj_name, 'funding': amount})
        matched_funding += amount
    else:
        # Substring match
        for fund_name, amount in funding_map.items():
            if proj_name.lower() in fund_name.lower() or fund_name.lower() in proj_name.lower():
                matches.append({'name': proj_name, 'matched': fund_name, 'funding': amount})
                matched_funding += amount
                break

result = {
    'project_count': len(matches),
    'total_funding': matched_funding,
    'projects': [{'project': m['name'], 'funding': m['funding']} for m in matches]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:14': ['Funding'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:28': {'status': 'loaded', 'civic_docs': 5, 'funding_records': 500}, 'var_functions.query_db:36': [{'count': '500', 'total_funding': '28094000'}]}

exec(code, env_args)
