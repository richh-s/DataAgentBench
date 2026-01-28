code = """import json
import re

# Load data from file paths
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
        fund_map[name] = fund_map.get(name, 0) + int(r.get('Amount', 0))

# Find disaster projects with 2022 dates from civic documents
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
                # Disaster indicators
                disaster_indicators = ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'WOOLSEY']
                for ind in disaster_indicators:
                    if ind in cl:
                        is_disaster = True
                        break
                # 2022 date indicators
                if '2022' in cl and ('DESIGN' in cl or 'CONSTRUCTION' in cl or 'BEGIN' in cl or 'COMPLETE' in cl):
                    has_2022 = True
            
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

result = {
    'total_funding': total_funding,
    'disaster_projects_count': len(disaster_projects),
    'sample_projects': disaster_projects[:5]
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json', 'var_functions.execute_python:92': {'total_funding_for_disaster_related_projects': 1410000, 'number_of_disaster_projects': 27, 'sample_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.execute_python:96': {'total_disaster_related_funding': 1410000, 'projects': 27}, 'var_functions.execute_python:100': {'total_funding_for_disaster_projects': 1410000, 'disaster_projects_count': 27}}

exec(code, env_args)
