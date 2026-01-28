code = """import json
import re

# Load data files
f_path = locals()['var_functions.query_db:66']
c_path = locals()['var_functions.query_db:67']

with open(f_path, 'r') as f:
    funding = json.load(f)
with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding map
fund_map = {}
for r in funding:
    name = r.get('Project_Name', '')
    if name:
        amount = int(r.get('Amount', 0))
        fund_map[name] = fund_map.get(name, 0) + amount

# Find disaster projects with 2022 dates from civic documents
disaster_projects_2022 = set()

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
            
            # Check next few lines
            for j in range(i+1, min(i+15, len(lines))):
                cl = lines[j].upper()
                # Disaster indicators
                for ind in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'WOOLSEY']:
                    if ind in cl:
                        is_disaster = True
                        break
                # 2022 schedule indicators
                if '2022' in cl:
                    for sw in ['DESIGN', 'CONSTRUCTION', 'BEGIN', 'COMPLETE']:
                        if sw in cl:
                            has_2022 = True
                            break
            
            if is_disaster and has_2022:
                disaster_projects_2022.add(project_name)

# Match with funding data
total_funding = 0
matched_projects = []

for proj in disaster_projects_2022:
    # Try exact match and common variations
    variations = [
        proj,
        proj + ' (FEMA Project)',
        proj + ' (FEMA/CalOES Project)',
        proj + ' (CalOES Project)',
        proj + ' (CalJPIA Project)',
        proj.replace('Project', '(FEMA Project)'),
        proj.replace('Improvements', 'Improvements (FEMA Project)')
    ]
    
    for var in variations:
        if var in fund_map:
            total_funding += fund_map[var]
            matched_projects.append((proj, var, fund_map[var]))
            break
    else:
        # Try substring matching
        for fund_name, amount in fund_map.items():
            if proj.lower() in fund_name.lower() or fund_name.lower() in proj.lower():
                total_funding += amount
                matched_projects.append((proj, fund_name, amount))
                break

# Also include projects with 2022 in name and disaster indicators
for fund_name, amount in fund_map.items():
    if '2022' in fund_name and any(ind in fund_name.upper() for ind in ['FEMA', 'CALOES', 'CALJPIA', 'WOOLSEY']):
        if fund_name not in [p[1] for p in matched_projects]:
            total_funding += amount
            matched_projects = [(fund_name, fund_name, amount)] + matched_projects

result = {
    'total_funding': total_funding,
    'disaster_projects_2022_count': len(disaster_projects_2022),
    'matched_projects': len(matched_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json', 'var_functions.execute_python:92': {'total_funding_for_disaster_related_projects': 1410000, 'number_of_disaster_projects': 27, 'sample_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.execute_python:96': {'total_disaster_related_funding': 1410000, 'projects': 27}, 'var_functions.execute_python:100': {'total_funding_for_disaster_projects': 1410000, 'disaster_projects_count': 27}}

exec(code, env_args)
