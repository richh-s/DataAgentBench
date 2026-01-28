code = """import json
import re

print('Loading data files...')

# Load funding data
funding_path = locals()['var_functions.query_db:66']
with open(funding_path) as f:
    funding = json.load(f)

# Load civic documents  
civic_path = locals()['var_functions.query_db:67']
with open(civic_path) as f:
    civic_docs = json.load(f)

print(f'Loaded {len(funding)} funding records and {len(civic_docs)} civic documents')

# Build funding map: project name to total amount
fund_map = {}
for record in funding:
    proj_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    if proj_name:
        fund_map[proj_name] = fund_map.get(proj_name, 0) + amount

print(f'Funding map has {len(fund_map)} entries')

# Find disaster projects with 2022 dates in civic documents
disaster_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('
')
    
    for i in range(len(lines) - 1):
        line = lines[i].strip()
        if not line or line.startswith('(') or 'page' in line.lower():
            continue
            
        next_line = lines[i+1].strip() if i+1 < len(lines) else ''
        if 'Updates:' in next_line or 'Project Schedule:' in next_line:
            project_name = line
            is_disaster = False
            has_2022 = False
            
            for j in range(i+1, min(i+12, len(lines))):
                cl = lines[j].upper()
                # Check for disaster indicators
                if 'FEMA' in cl or 'CALOES' in cl or 'CALJPIA' in cl or 'DISASTER' in cl or 'WOOLSEY' in cl:
                    is_disaster = True
                # Check for 2022 dates with project context
                if '2022' in cl and ('DESIGN' in cl or 'CONSTRUCTION' in cl or 'BEGIN' in cl or 'COMPLETE' in cl):
                    has_2022 = True
            
            if is_disaster and has_2022 and project_name:
                disaster_projects.append(project_name)

# Remove duplicates
disaster_projects = list(set(disaster_projects))
print(f'Found {len(disaster_projects)} disaster projects with 2022 dates')

# Calculate funding for these projects
total_funding = 0
matched_projects = []

for proj in disaster_projects:
    for fund_proj, amount in fund_map.items():
        if proj in fund_proj or fund_proj in proj:
            total_funding += amount
            matched_projects.append(proj)
            break

print(f'Matched {len(matched_projects)} projects with funding')
print(f'Total funding: ${total_funding:,}')

result = {
    'total_funding_for_disaster_projects_started_2022': total_funding,
    'number_of_disaster_projects': len(disaster_projects),
    'number_of_matched_projects': len(matched_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json'}

exec(code, env_args)
