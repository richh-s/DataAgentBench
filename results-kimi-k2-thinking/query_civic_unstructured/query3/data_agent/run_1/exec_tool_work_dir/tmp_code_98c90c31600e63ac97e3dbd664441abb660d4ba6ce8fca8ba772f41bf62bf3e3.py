code = """import json
import re

# Access the variable safely
funding_file = locals()['var_functions.query_db:0']

# Load the funding data
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

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

# Display summary
print("FEMA/EMERGENCY PROJECTS:")
print("=" * 50)
for i, p in enumerate(fema_projects, 1):
    amount_str = "${:,}".format(p['Amount'])
    print("{}. {}".format(i, p['Project_Name']))
    print("   Source: {}".format(p['Funding_Source']))
    print("   Amount: {}".format(amount_str))
    print()

print("__RESULT__:")
print(json.dumps(fema_projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
