code = """import json

# Get file paths
funding_path = locals()['var_functions.query_db:66']
civic_path = locals()['var_functions.query_db:67']

# Load data
with open(funding_path, 'r') as f:
    funding = json.load(f)
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding map
fund_map = {}
for r in funding:
    n = r.get('Project_Name', '')
    if n:
        fund_map[n] = fund_map.get(n, 0) + int(r.get('Amount', 0))

# Calculate total disaster funding
 total_disaster = 0
for proj_name, amt in fund_map.items():
    if 'FEMA' in proj_name.upper() or 'CALOES' in proj_name.upper() or 'CALJPIA' in proj_name.upper() or 'WOOLSEY' in proj_name.upper():
        total_disaster += amt

print('__RESULT__:')
print(json.dumps({'total_funding': total_disaster, 'projects': len([p for p in fund_map.keys() if any(k in p.upper() for k in ['FEMA', 'CALOES', 'CALJPIA', 'WOOLSEY'])])}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json', 'var_functions.execute_python:92': {'total_funding_for_disaster_related_projects': 1410000, 'number_of_disaster_projects': 27, 'sample_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.execute_python:96': {'total_disaster_related_funding': 1410000, 'projects': 27}, 'var_functions.execute_python:100': {'total_funding_for_disaster_projects': 1410000, 'disaster_projects_count': 27}}

exec(code, env_args)
