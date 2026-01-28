code = """import json

# Read funding data from the provided path
funding_path = locals()['var_functions.query_db:16']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Filter for projects containing "emergency" or "FEMA" (case insensitive)
emergency_fema_projects = []
for record in funding_data:
    project_name = record['Project_Name'].lower()
    if 'emergency' in project_name or 'fema' in project_name:
        emergency_fema_projects.append(record)

# Prepare result
result = {
    'total_projects': len(funding_data),
    'emergency_fema_count': len(emergency_fema_projects),
    'projects': emergency_fema_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
