code = """import json
import re

# Read the funding data
with open(var_functions.query_db:0, 'r') as f:
    funding_data = json.load(f)

# Read the civic documents
with open(var_functions.query_db:6, 'r') as f:
    civic_docs = json.load(f)

print("Funding records:", len(funding_data))
print("Civic documents:", len(civic_docs))

# Look for FEMA/emergency related projects in funding data
fema_projects = []
for record in funding_data:
    project_name = record.get('Project_Name', '')
    if 'FEMA' in project_name.upper() or 'EMERGENCY' in project_name.upper():
        fema_projects.append(record)

print("FEMA/Emergency projects in funding data:", len(fema_projects))
for proj in fema_projects[:10]:
    print(f"  - {proj['Project_Name']}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
