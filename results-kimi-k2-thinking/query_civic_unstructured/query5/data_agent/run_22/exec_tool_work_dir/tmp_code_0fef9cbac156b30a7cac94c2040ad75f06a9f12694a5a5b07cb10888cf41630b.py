code = """import json
import re

# Load funding data
with open(locals()['var_functions.query_db:66'], 'r') as f:
    funding = json.load(f)

# Load civic documents  
with open(locals()['var_functions.query_db:67'], 'r') as f:
    civic_docs = json.load(f)

# Build funding map
fund_map = {}
for record in funding:
    proj_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    if proj_name:
        fund_map[proj_name] = amount

# Find disaster projects with 2022 dates
disaster_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
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
                # Check disaster indicators
                for ind in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'WOOLSEY']:
                    if ind in cl:
                        is_disaster = True
                        break
                
                # Check 2022 date indicators
                if '2022' in cl:
                    for sw in ['DESIGN', 'CONSTRUCTION', 'BEGIN', 'COMPLETE']:
                        if sw in cl:
                            has_2022 = True
                            break
            
            if is_disaster and has_2022 and project_name:
                disaster_projects.append(project_name)

# Remove duplicates
disaster_projects = list(set(disaster_projects))

# Calculate total funding
total_funding = 0
for proj in disaster_projects:
    for fund_proj, amount in fund_map.items():
        if proj in fund_proj or fund_proj in proj:
            total_funding += amount
            break

result = {
    'total_funding_for_disaster_projects_2022': total_funding,
    'disaster_projects': len(disaster_projects),
    'samples': disaster_projects[:3]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json'}

exec(code, env_args)
