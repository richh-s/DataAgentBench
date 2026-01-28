code = """import json

# Access the stored file paths
funding_path = locals()['var_functions.query_db:0']
civic_path = locals()['var_functions.query_db:2']

print('Loading funding data from:', funding_path)
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

print('Loading civic documents from:', civic_path)
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print('Data loaded successfully')
print('Funding records:', len(funding_records))
print('Civic documents:', len(civic_docs))

# Find FEMA/emergency projects
fema_projects = []
for record in funding_records:
    project_name = record['Project_Name'].lower()
    funding_source = record['Funding_Source'].lower()
    
    # Check for emergency-related keywords
    if ('fema' in project_name or 'emergency' in project_name or 
        'disaster' in project_name or 'caloes' in project_name or 
        'caljpia' in project_name or 'siren' in project_name or
        'federal' in funding_source):
        fema_projects.append(record)

print('\nFEMA/emergency projects found:', len(fema_projects))

# Prepare results
results = []
for proj in fema_projects:
    result = {
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': int(proj['Amount'])
    }
    results.append(result)

# Format output
output = json.dumps(results, indent=2)
print('\n__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
