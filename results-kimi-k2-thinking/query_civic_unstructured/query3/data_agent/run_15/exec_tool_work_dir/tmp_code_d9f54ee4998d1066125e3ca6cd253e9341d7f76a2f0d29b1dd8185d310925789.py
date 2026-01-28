code = """import json

# Load funding data
with open('var_functions.query_db:0', 'r') as f:
    funding = json.load(f)

print('Total funding records:', len(funding))

# Find FEMA/emergency projects
fema_projects = []
for record in funding:
    name = record['Project_Name'].lower()
    source = record['Funding_Source'].lower()
    
    if 'fema' in name or 'emergency' in name or 'disaster' in name or 'caloes' in name or 'caljpia' in name or 'warning' in name or 'siren' in name or 'federal' in source:
        fema_projects.append(record)

print('FEMA/emergency projects:', len(fema_projects))

# Store results
results = []
for proj in fema_projects:
    results.append({
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'], 
        'Amount': int(proj['Amount'])
    })

# Print in required format
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
