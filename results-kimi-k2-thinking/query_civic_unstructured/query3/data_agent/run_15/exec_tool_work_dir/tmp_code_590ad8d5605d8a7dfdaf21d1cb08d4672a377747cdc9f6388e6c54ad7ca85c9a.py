code = """import json

# Get the funding data file path
funding_path = var_functions.query_db_28

# Load the funding data
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

print('Total funding records:', len(funding_records))

# Define emergency-related keywords
emergency_keywords = ['fema', 'emergency', 'disaster', 'caloes', 'caljpia', 'warning', 'siren']
federal_sources = ['federal assistance', 'government grant', 'state development grant']

# Filter FEMA/emergency related projects
fema_emergency_projects = []

for record in funding_records:
    project_name = record['Project_Name'].lower()
    funding_source = record['Funding_Source'].lower()
    funding_id = record['Funding_ID']
    amount = int(record['Amount'])
    
    # Check if project name contains emergency keywords
    has_emergency_keyword = any(keyword in project_name for keyword in emergency_keywords)
    
    # Check if funding source suggests federal/disaster assistance
    has_federal_source = any(source in funding_source for source in federal_sources)
    
    # Check for specific federal agencies in project name
    has_federal_agency = 'caloes' in project_name or 'caljpia' in project_name
    
    if has_emergency_keyword or has_federal_source or has_federal_agency:
        fema_emergency_projects.append({
            'Funding_ID': funding_id,
            'Project_Name': record['Project_Name'],
            'Funding_Source': record['Funding_Source'],
            'Amount': amount
        })

print('FEMA/emergency projects found:', len(fema_emergency_projects))
print('\nFEMA Emergency Projects List:')
print('=' * 80)

for proj in fema_emergency_projects:
    print(f"Project: {proj['Project_Name']}")
    print(f"Funding Source: {proj['Funding_Source']}")
    print(f"Amount: ${proj['Amount']:,}")
    print('-' * 60)

# Format output for final answer
print('\n__RESULT__:')
print(json.dumps(fema_emergency_projects, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
