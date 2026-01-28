code = """import json
import re

# Read the funding data using locals() to access the variables
funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Look for FEMA/emergency related projects in funding data
fema_projects = []
for record in funding_data:
    project_name = record.get('Project_Name', '')
    if 'FEMA' in project_name.upper() or 'EMERGENCY' in project_name.upper():
        fema_projects.append(record)

# Print result in required format
result = {
    'funding_fema_projects': fema_projects,
    'count': len(fema_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
