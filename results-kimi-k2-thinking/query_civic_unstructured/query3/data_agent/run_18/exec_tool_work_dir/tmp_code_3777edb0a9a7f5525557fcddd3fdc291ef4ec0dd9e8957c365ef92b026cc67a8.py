code = """import json

# Get the data from the stored variables
funding_data = locals()['var_functions.query_db:2']
civic_docs = locals()['var_functions.query_db:0']

print('Funding records count:', len(funding_data))
print('Civic docs count:', len(civic_docs))

# Step 1: Find emergency/FEMA projects in funding data
emergency_funding = []
for record in funding_data:
    project_name = record['Project_Name'].lower()
    if 'emergency' in project_name or 'fema' in project_name:
        emergency_funding.append(record)

print('\nFound', len(emergency_funding), 'emergency/FEMA projects in funding:')
for proj in emergency_funding:
    print(json.dumps(proj))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
