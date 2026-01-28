code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:0']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data  
civic_docs_path = locals()['var_functions.query_db:4']
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

print('Found', len(funding_data), 'funding records')
print('Found', len(civic_docs_data), 'civic documents containing emergency or FEMA')

# Create funding lookup by project name
funding_by_project = {}
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    if proj_name:
        funding_by_project[proj_name] = {
            'Funding_Source': record.get('Funding_Source', ''),
            'Amount': record.get('Amount', 0)
        }

# Find projects with FEMA/emergency in name from funding data
fema_projects = []
for proj_name, funding_info in funding_by_project.items():
    if 'FEMA' in proj_name.upper() or 'EMERGENCY' in proj_name.upper():
        fema_projects.append({
            'Project_Name': proj_name,
            'Funding_Source': funding_info['Funding_Source'],
            'Amount': funding_info['Amount'],
            'Status': 'Unknown'
        })

print('\nFound', len(fema_projects), 'projects with FEMA/emergency in name')

# Show first few projects
print('\nSample projects:')
for proj in fema_projects[:10]:
    print(' -', proj['Project_Name'])

__RESULT__ = json.dumps(fema_projects)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
