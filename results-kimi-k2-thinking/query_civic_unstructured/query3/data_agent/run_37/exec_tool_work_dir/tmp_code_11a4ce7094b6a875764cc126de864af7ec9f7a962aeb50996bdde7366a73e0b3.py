code = """import json

# Load funding data
funding_path = locals()['var_functions.query_db:0']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Simple approach - just find projects with FEMA or emergency in their names
fema_projects = []
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    if 'FEMA' in proj_name.upper() or 'EMERGENCY' in proj_name.upper():
        fema_projects.append({
            'Project_Name': proj_name,
            'Funding_Source': record.get('Funding_Source', ''),
            'Amount': record.get('Amount', 0),
            'Status': 'Unknown'
        })

print('Found', len(fema_projects), 'FEMA/emergency projects')
print('Sample projects:')
for proj in fema_projects[:5]:
    print(json.dumps(proj))

__RESULT__ = json.dumps(fema_projects)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
