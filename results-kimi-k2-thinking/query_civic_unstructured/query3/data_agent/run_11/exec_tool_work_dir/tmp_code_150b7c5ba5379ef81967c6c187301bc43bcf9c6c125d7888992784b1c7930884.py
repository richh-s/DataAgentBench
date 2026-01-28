code = """import json

# Read the civic documents
civic_docs_path = var_functions.query_db:10
if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:10

# Read the funding data
funding_path = var_functions.query_db:11
if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db:11

print('Found %d civic documents and %d funding records' % (len(civic_docs), len(funding_data)))

# Simple extraction of FEMA/emergency projects
target_projects = []

# First, find funding records for FEMA/emergency projects
for fund in funding_data:
    project_name = fund.get('Project_Name', '')
    if 'FEMA' in project_name.upper() or 'EMERGENCY' in project_name.upper() or 'WARNING' in project_name.upper():
        target_projects.append({
            'Project_Name': project_name,
            'Funding_Source': fund['Funding_Source'],
            'Amount': fund['Amount'],
            'Status': 'unknown',
            'Topic': 'emergency, FEMA',
            'Type': 'disaster'
        })

print('Found %d FEMA/emergency projects in funding data' % len(target_projects))

# Convert to JSON result
result = json.dumps(target_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
