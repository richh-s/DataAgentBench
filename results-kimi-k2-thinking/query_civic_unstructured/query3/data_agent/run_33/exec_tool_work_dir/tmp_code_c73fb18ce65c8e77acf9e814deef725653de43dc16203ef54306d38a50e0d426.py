code = """import json

civic_path = locals()['var_functions.query_db:0']
funding_path = locals()['var_functions.query_db:5']

with open(civic_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding_data = json.load(f)

fema_projects = []

for f in funding_data:
    project_name = f['Project_Name']
    if 'fema' in project_name.lower():
        fema_projects.append({
            'Project_Name': project_name,
            'Funding_Source': f['Funding_Source'],
            'Amount': int(f['Amount']),
            'Status': 'Not specified'
        })

fema_projects.sort(key=lambda x: x['Amount'], reverse=True)

print('__RESULT__:')
print(json.dumps(fema_projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
