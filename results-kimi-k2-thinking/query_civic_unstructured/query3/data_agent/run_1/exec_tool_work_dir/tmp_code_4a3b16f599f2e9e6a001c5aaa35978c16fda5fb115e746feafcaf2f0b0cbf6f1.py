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

# Sort by Amount descending
fema_projects.sort(key=lambda x: x['Amount'], reverse=True)

print(f"Found {len(fema_projects)} projects with FEMA or emergency in name")
for i, p in enumerate(fema_projects[:15], 1):
    print(f"{i}. {p['Project_Name']}")
    print(f"   Funding: {p['Funding_Source']}, Amount: ${p['Amount']:,}")
    
print("__RESULT__:")
print(json.dumps(fema_projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
