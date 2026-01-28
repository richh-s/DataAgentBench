code = """import json, re, os

# Load data
with open(var_functions.query_db:6, 'r') as f:
    funding_data = json.load(f)
with open(var_functions.query_db:7, 'r') as f:
    civic_docs_data = json.load(f)

print('Loaded', len(funding_data), 'funding records and', len(civic_docs_data), 'civic documents')

# Extract projects
all_projects = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or line.startswith('(') or any(k in line.lower() for k in ['page', 'agenda item']):
            continue
        if (len(line) > 5 and i < len(lines) - 1 and any(indicator in lines[i+1] for indicator in ['Updates:', 'Project Schedule:', '(cid:'])):
            if current_project:
                all_projects.append({'project_name': current_project, 'info': info, 'source_file': doc.get('filename', '')})
            current_project = line
            info = {'is_disaster': False, 'has_2022_date': False, 'start_date_mention': None}
        
        if current_project:
            if any(k in line.upper() for k in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'RECOVERY', 'WOOLSEY']):
                info['is_disaster'] = True
            if '2022' in line and any(s in line.upper() for s in ['COMPLETE DESIGN', 'BEGIN', 'CONSTRUCTION', 'DESIGN', 'SCHEDULE']):
                info['has_2022_date'] = True
                info['start_date_mention'] = line
    
    if current_project:
        all_projects.append({'project_name': current_project, 'info': info, 'source_file': doc.get('filename', '')})

# Filter disaster projects
 disaster_2022 = [p for p in all_projects if p['info']['is_disaster'] and p['info']['has_2022_date']]
print('Found', len(disaster_2022), 'disaster projects with 2022 dates')

# Map funding
funding_map = {}
for r in funding_data:
    name = r.get('Project_Name', '')
    funding_map[name] = funding_map.get(name, 0) + int(r.get('Amount', 0))

# Calculate total funding
total_funding = 0
for p in disaster_2022:
    proj_name = p['project_name']
    for fund_name, amount in funding_map.items():
        if proj_name in fund_name or fund_name in proj_name or any(token in fund_name for token in proj_name.split() if len(token) > 5):
            total_funding += amount
            break

print('Total funding:', total_funding)
print('__RESULT__:', json.dumps({'total_funding': total_funding, 'disaster_projects_count': len(disaster_2022)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
