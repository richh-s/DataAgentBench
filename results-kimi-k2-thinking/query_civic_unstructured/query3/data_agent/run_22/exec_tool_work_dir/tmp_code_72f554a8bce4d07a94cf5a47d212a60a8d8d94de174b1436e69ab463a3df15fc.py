code = """import json

# Read the full funding data
funding_file_path = locals()['var_functions.query_db:2']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Filter projects related to 'emergency' or 'FEMA'
filtered_projects = []
for project in funding_data:
    project_name = project['Project_Name'].lower()
    if 'emergency' in project_name or 'fema' in project_name:
        filtered_projects.append({
            'Project_Name': project['Project_Name'],
            'Funding_Source': project['Funding_Source'],
            'Amount': int(project['Amount'])
        })

print('__RESULT__:')
print(json.dumps(filtered_projects))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
