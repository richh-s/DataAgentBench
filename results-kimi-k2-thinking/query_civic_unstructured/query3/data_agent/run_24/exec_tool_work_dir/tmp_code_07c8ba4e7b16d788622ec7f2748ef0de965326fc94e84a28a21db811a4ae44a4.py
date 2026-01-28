code = """import json

# Load funding data
funding_file = var_functions.query_db:18
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('Total funding records loaded:', len(funding_data))

# Filter for FEMA and Emergency related projects
fema_emergency_projects = []
for rec in funding_data:
    project_name = rec['Project_Name'].lower()
    if 'fema' in project_name or 'emergency' in project_name:
        fema_emergency_projects.append({
            'Project_Name': rec['Project_Name'],
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount'])
        })

print('FEMA/Emergency projects found:', len(fema_emergency_projects))
print('\nDetailed list:')
for proj in fema_emergency_projects:
    print(f"- {proj['Project_Name']} | Amount: ${proj['Amount']:,} | Source: {proj['Funding_Source']}")

# Calculate summary statistics
if fema_emergency_projects:
    total_amount = sum(p['Amount'] for p in fema_emergency_projects)
    print(f'\nTotal funding for FEMA/Emergency projects: ${total_amount:,}')

result = fema_emergency_projects
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
