code = """import json
import re

# Access the variable safely
funding_file = locals()['var_functions.query_db:0']

# Load the funding data
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
            'Project_Name': record.get('Project_Name', ''),
            'Funding_Source': record.get('Funding_Source', ''),
            'Amount': int(record.get('Amount', 0)) if record.get('Amount') else 0
        })

# Sort by amount descending
fema_projects.sort(key=lambda x: x['Amount'], reverse=True)

print(f"\nFound {len(fema_projects)} FEMA/emergency projects")
print("\nTOP 10 projects by funding amount:")
for i, p in enumerate(fema_projects[:10], 1):
    print(f"{i}. {p['Project_Name']}")
    print(f"   Funding: {p['Funding_Source']}, Amount: ${p['Amount']:,}")

print("\n__RESULT__:")
print(json.dumps(fema_projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
