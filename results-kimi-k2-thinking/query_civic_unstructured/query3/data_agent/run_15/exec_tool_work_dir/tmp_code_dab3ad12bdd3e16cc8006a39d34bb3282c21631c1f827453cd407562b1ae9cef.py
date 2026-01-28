code = """import json

# The funding data is stored in the variable var_functions.query_db:0
# The civic documents data is stored in the variable var_functions.query_db:2

print('Loading data from stored variables...')

# Get the funding data - it's a JSON file path string
funding_data_path = var_functions.query_db_0
print('Funding data path:', funding_data_path)

with open(funding_data_path, 'r') as f:
    funding_records = json.load(f)

# Get the civic documents data - it's a JSON file path string
civic_data_path = var_functions.query_db_2
print('Civic documents path:', civic_data_path)

with open(civic_data_path, 'r') as f:
    civic_docs = json.load(f)

print('Successfully loaded:')
print('- Funding records:', len(funding_records))
print('- Civic documents:', len(civic_docs))

# Look for FEMA/emergency projects in funding data
fema_projects = []
keywords = ['fema', 'emergency', 'disaster', 'caloes', 'caljpia', 'warning', 'siren']

for record in funding_records:
    project_name_lower = record['Project_Name'].lower()
    funding_source_lower = record['Funding_Source'].lower()
    
    # Check if project is FEMA/emergency related
    is_emergency = any(keyword in project_name_lower for keyword in keywords)
    is_federal = 'federal' in funding_source_lower
    
    if is_emergency or is_federal:
        fema_projects.append(record)

print('\nFound', len(fema_projects), 'FEMA/emergency related projects')

# Prepare results with project names, funding sources, and amounts
results = []
for proj in fema_projects:
    result = {
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': int(proj['Amount'])
    }
    results.append(result)

print('First 5 projects:')
for proj in results[:5]:
    print('-', proj['Project_Name'])

# Output results in required format
print('\n__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
