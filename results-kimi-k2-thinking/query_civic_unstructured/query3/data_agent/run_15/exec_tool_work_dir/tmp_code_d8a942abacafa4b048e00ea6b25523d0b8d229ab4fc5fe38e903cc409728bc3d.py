code = """import json

# Load the data from files
funding_path = 'var_functions.query_db:0'
civic_path = 'var_functions.query_db:2'

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print('Funding records count:', len(funding_records))
print('Civic documents count:', len(civic_docs))

# Identify FEMA/emergency projects from funding data
fema_projects = []
keywords = ['fema', 'emergency', 'disaster', 'caloes', 'caljpia']

for record in funding_records:
    project_name = record['Project_Name'].lower()
    funding_source = record['Funding_Source'].lower()
    
    is_match = False
    for keyword in keywords:
        if keyword in project_name:
            is_match = True
            break
    
    if 'federal' in funding_source:
        is_match = True
    
    if is_match:
        fema_projects.append(record)

print('\nFEMA/emergency projects found:', len(fema_projects))

# Extract project information
result_data = []
for proj in fema_projects:
    amount = int(proj['Amount'])
    info = {
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': amount
    }
    result_data.append(info)
    print('Project:', proj['Project_Name'])
    print('Funding_Source:', proj['Funding_Source'])
    print('Amount:', amount)
    print('---')

print('\nTotal projects:', len(result_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
