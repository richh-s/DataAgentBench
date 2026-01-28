code = """import json
import re

# Access the stored data using locals()
funding_data = locals()["var_functions.query_db:0"]
civic_docs_data = locals()["var_functions.query_db:4"]

print('Funding records count:', len(funding_data))
print('Civic docs count:', len(civic_docs_data))

# Extract projects related to emergency or FEMA from funding data
emergency_fema_projects = []
for record in funding_data:
    project_name = record['Project_Name'].lower()
    if 'emergency' in project_name or 'fema' in project_name:
        emergency_fema_projects.append({
            'Project_Name': record['Project_Name'],
            'Funding_Source': record['Funding_Source'],
            'Amount': record['Amount']
        })

print('\nDirect matches from funding data:', len(emergency_fema_projects))

# Show some examples
for i, proj in enumerate(emergency_fema_projects[:10]):
    print(f"{i+1}. {proj['Project_Name']} - {proj['Funding_Source']} - ${proj['Amount']}")

result = json.dumps(emergency_fema_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
