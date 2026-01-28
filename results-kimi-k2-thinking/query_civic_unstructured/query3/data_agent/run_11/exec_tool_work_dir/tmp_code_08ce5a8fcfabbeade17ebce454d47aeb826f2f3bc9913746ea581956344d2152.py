code = """import json
import os

# Load civic documents
civic_docs_result = var_functions.query_db:10
if isinstance(civic_docs_result, str) and civic_docs_result.endswith('.json'):
    with open(civic_docs_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_result

# Load funding data  
funding_result = var_functions.query_db:11
if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_result

# Find all FEMA/emergency projects from funding data
fema_projects = []
for item in funding_data:
    name = item.get('Project_Name', '')
    if name and ('FEMA' in name.upper() or 'EMERGENCY' in name.upper() or 'WARNING' in name.upper()):
        fema_projects.append({
            'Project_Name': name,
            'Funding_Source': item.get('Funding_Source', ''),
            'Amount': item.get('Amount', 0)
        })

print('Found %d FEMA/emergency projects' % len(fema_projects))
print('__RESULT__:')
print(json.dumps(fema_projects))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
