code = """import json
import re

# Load the funding data from the file path stored in the variable
funding_file = var_functions.query_db:0
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Total funding records: {len(funding_data)}")
print("Sample records:")
for i, record in enumerate(funding_data[:3], 1):
    print(f"{i}. {record.get('Project_Name')}")

# Filter projects related to 'emergency' or 'FEMA'
fema_projects = []
for record in funding_data:
    project_name = record.get('Project_Name', '').lower()
    if 'fema' in project_name or 'emergency' in project_name:
        fema_projects.append({
            'Project_Name': record.get('Project_Name'),
            'Funding_Source': record.get('Funding_Source'),
            'Amount': int(record.get('Amount', 0))
        })

print(f"\nFound {len(fema_projects)} FEMA/emergency projects")
for p in fema_projects[:10]:
    print(f"  - {p['Project_Name']}")

result = fema_projects
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
