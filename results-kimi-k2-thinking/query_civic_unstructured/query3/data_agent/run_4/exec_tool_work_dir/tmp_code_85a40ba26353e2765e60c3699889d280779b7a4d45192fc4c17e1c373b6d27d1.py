code = """import json
import re

# Read the MongoDB documents results
mongo_file = open('/var_functions.query_db:9', 'r')
mongo_docs = json.load(mongo_file)
mongo_file.close()

# Read the funding data results
funding_file = open('/var_functions.query_db:10', 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Create funding lookup dictionary
funding_lookup = {}
for record in funding_data:
    funding_lookup[record['Project_Name']] = {
        'Funding_Source': record['Funding_Source'],
        'Amount': int(record['Amount'])
    }

# Find projects related to emergency or FEMA
emergency_fema_projects = []

for record in funding_data:
    project_name = record['Project_Name']
    if 'emergency' in project_name.lower() or 'fema' in project_name.lower():
        funding_info = funding_lookup[project_name]
        emergency_fema_projects.append({
            'Project_Name': project_name,
            'Funding_Source': funding_info['Funding_Source'],
            'Amount': funding_info['Amount']
        })

# Sort by amount descending
emergency_fema_projects.sort(key=lambda x: x['Amount'], reverse=True)

print('__RESULT__:')
print(json.dumps(emergency_fema_projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
