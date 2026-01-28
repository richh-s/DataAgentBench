code = """import json
import re

# Load funding data
funding_file_path = locals()['var_functions.query_db:0']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
civic_docs_file_path = locals()['var_functions.query_db:4']
with open(civic_docs_file_path, 'r') as f:
    civic_docs_data = json.load(f)

print("Found {} funding records".format(len(funding_data)))
print("Found {} civic documents containing 'emergency' or 'FEMA'".format(len(civic_docs_data)))

# Create a dictionary of funding records by project name for easy lookup
funding_by_project = {}
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    if proj_name:
        funding_by_project[proj_name] = {
            'Funding_Source': record.get('Funding_Source', ''),
            'Amount': record.get('Amount', 0)
        }

# First, let's check which projects in funding data have 'FEMA' or 'emergency' in their names
fema_related_projects = []
for proj_name, funding_info in funding_by_project.items():
    if 'FEMA' in proj_name.upper() or 'EMERGENCY' in proj_name.upper():
        fema_related_projects.append({
            'Project_Name': proj_name,
            'Funding_Source': funding_info['Funding_Source'],
            'Amount': funding_info['Amount'],
            'Status': 'Unknown (from funding data only)'
        })

print("\nFound {} projects with FEMA/emergency in name from funding data".format(len(fema_related_projects)))

# Check if we have any projects with FEMA/emergency in name
print("\nSample projects from funding data:")
for i, proj in enumerate(fema_related_projects[:10]):
    print("  {}. {}".format(i+1, proj['Project_Name']))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
