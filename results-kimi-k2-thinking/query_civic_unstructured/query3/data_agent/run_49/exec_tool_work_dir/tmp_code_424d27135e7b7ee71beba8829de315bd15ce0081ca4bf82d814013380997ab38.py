code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:0
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = var_functions.query_db:2
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Filter funding data for emergency/FEMA related projects
emergency_fema_projects = []
for item in funding_data:
    project_name = item.get('Project_Name', '').lower()
    funding_source = item.get('Funding_Source', '').lower()
    
    if 'emergency' in project_name or 'fema' in project_name or 'emergency' in funding_source or 'fema' in funding_source:
        emergency_fema_projects.append({
            'Project_Name': item.get('Project_Name'),
            'Funding_Source': item.get('Funding_Source'),
            'Amount': int(item.get('Amount', 0))
        })

print('__RESULT__:')
print(json.dumps(emergency_fema_projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
