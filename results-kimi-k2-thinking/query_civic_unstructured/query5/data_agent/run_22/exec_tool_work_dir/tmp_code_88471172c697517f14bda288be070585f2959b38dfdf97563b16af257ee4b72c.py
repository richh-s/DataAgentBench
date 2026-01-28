code = """import json, re

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

# Total disaster-related funding
disaster_funding_total = 0
for name, amt in fund_map.items():
    if any(k in name.upper() for k in ['FEMA', 'CALOES', 'CALJPIA', 'WOOLSEY', 'DISASTER', 'RECOVERY']):
        disaster_funding_total += amt

result = {
    'total_disaster_related_funding': disaster_funding_total,
    'projects': len([n for n in fund_map.keys() if any(k in n.upper() for k in ['FEMA', 'CALOES', 'CALJPIA', 'WOOLSEY', 'DISASTER', 'RECOVERY'])])
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json', 'var_functions.execute_python:92': {'total_funding_for_disaster_related_projects': 1410000, 'number_of_disaster_projects': 27, 'sample_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}}

exec(code, env_args)
