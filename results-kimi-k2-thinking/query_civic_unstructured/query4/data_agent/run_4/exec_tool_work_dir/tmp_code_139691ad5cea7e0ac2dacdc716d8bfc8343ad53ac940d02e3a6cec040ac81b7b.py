code = """import json
import re

# Load civic documents
civic_docs_path = var_functions.query_db:2
civic_docs = []
if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_path if isinstance(civic_docs_path, list) else []

# Load funding data
funding_path = var_functions.query_db:4
funding_data = []
if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_path if isinstance(funding_path, list) else []

print(f'Loaded {len(civic_docs)} civic documents and {len(funding_data)} funding records')

# Create funding lookup
funding_lookup = {}
for fund in funding_data:
    proj_name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    funding_lookup[proj_name] = funding_lookup.get(proj_name, 0) + amount

print(f'Created funding lookup with {len(funding_lookup)} projects')
print('__RESULT__:')
print(json.dumps({'status': 'data_loaded', 'civic_docs': len(civic_docs), 'funding_records': len(funding_data), 'funding_projects': len(funding_lookup)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
