code = """import json
import re

# Read the full funding data from the file stored in variable with ID var_functions.query_db:0
funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Filter for projects related to emergency or FEMA
emergency_fema_projects = []

for record in funding_data:
    project_name = record.get('Project_Name', '').lower()
    funding_source = record.get('Funding_Source', '').lower()
    
    # Check if project name or funding source contains emergency/FEMA related terms
    if any(term in project_name for term in ['fema', 'emergency', 'warning', 'siren', 'disaster', 'caloes', 'caljpia']):
        emergency_fema_projects.append(record)
    elif any(term in funding_source for term in ['fema', 'emergency', 'federal assistance', 'disaster']):
        emergency_fema_projects.append(record)

print('__RESULT__:')
print(json.dumps(emergency_fema_projects, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
