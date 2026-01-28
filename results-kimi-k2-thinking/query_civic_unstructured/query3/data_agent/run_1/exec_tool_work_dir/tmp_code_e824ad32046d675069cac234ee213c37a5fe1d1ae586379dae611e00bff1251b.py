code = """import json
import re

# Load the funding data
funding_file = var_functions.query_db:0
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

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

print(f"Found {len(fema_projects)} projects with 'FEMA' or 'emergency' in name")
print("\nFirst 10 projects:")
for p in fema_projects[:10]:
    print(f"  - {p['Project_Name']}: {p['Funding_Source']}, ${p['Amount']:,}")
    
print("\n__RESULT__:")
print(json.dumps(fema_projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
