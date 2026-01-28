code = """import json
import re

funding_data = var_functions.query_db__0
civic_docs_data = var_functions.query_db__4

print('Funding records:', len(funding_data))
print('Civic docs:', len(civic_docs_data))

emergency_fema_projects = []
for record in funding_data:
    project_name = record['Project_Name']
    if 'emergency' in project_name.lower() or 'fema' in project_name.lower():
        emergency_fema_projects.append(record)

print('Direct matches in funding:', len(emergency_fema_projects))

for proj in emergency_fema_projects[:10]:
    print(proj['Project_Name'], '-', proj['Funding_Source'], '-', proj['Amount'])

result = json.dumps(emergency_fema_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
