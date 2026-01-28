code = """import json

# Load data from files
f_path = locals()['var_functions.query_db:2']
c_path = locals()['var_functions.query_db:0']

with open(f_path, 'r') as f:
    funding_data = json.load(f)

with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Find FEMA and emergency projects
fema_projects = []
for rec in funding_data:
    name = rec.get('Project_Name', '')
    if 'FEMA' in name or 'fema' in name or 'emergency' in name.lower():
        fema_projects.append({
            'Project_Name': name,
            'Funding_Source': rec.get('Funding_Source', ''),
            'Amount': int(rec.get('Amount', 0))
        })

# For now, return the funding data without status extraction
# (will add status extraction in next step)
result = json.dumps(fema_projects, indent=2)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
