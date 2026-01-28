code = """import json
import re

# Load funding data from the file path stored in the variable
funding_path = locals()['var_functions.query_db:0']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic docs data from the file path stored in the variable  
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Funding records loaded: {len(funding_data)}")
print(f"Civic documents loaded: {len(civic_docs)}")

# Extract all project names from funding data
funding_projects = {item['Project_Name'].strip().lower() for item in funding_data}
print(f"Unique funding projects: {len(funding_projects)}")

# Look for FEMA and emergency related projects in funding data directly
fema_funding_projects = []
for item in funding_data:
    project_name = item['Project_Name'].lower()
    if 'fema' in project_name or 'emergency' in project_name:
        fema_funding_projects.append(item)

print(f"FEMA/Emergency projects in funding data: {len(fema_funding_projects)}")
print("__RESULT__:")
print(json.dumps(fema_funding_projects[:10]))  # Show first 10"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
