code = """import json
import os
import re

# Get storage keys
storage_keys = list(locals().keys())
print('Available storage keys:', storage_keys)

# Try to access the funding and civic doc data
# The keys from previous queries should be available
funding_key = 'var_functions.query_db:70'
civic_key = 'var_functions.query_db:71'

# Check if they exist in locals
if funding_key in locals():
    print('Found funding data')
    funding_data = locals()[funding_key]
else:
    print('Funding data not found in locals')
    funding_data = []

if civic_key in locals():
    print('Found civic docs')
    civic_docs = locals()[civic_key]
else:
    print('Civic docs not found in locals')
    civic_docs = []

# Also check if they are file paths
if isinstance(funding_data, str) and os.path.exists(funding_data):
    print('Loading funding from file')
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

if isinstance(civic_docs, str) and os.path.exists(civic_docs):
    print('Loading civic docs from file')
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

print('Funding records:', len(funding_data) if isinstance(funding_data, list) else 0)
print('Civic docs:', len(civic_docs) if isinstance(civic_docs, list) else 0)

# Show first few items
if funding_data:
    print('First funding item:', funding_data[0])
if civic_docs:
    print('First civic doc item type:', type(civic_docs[0]))

result = {'funding_count': len(funding_data), 'civic_count': len(civic_docs)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.list_db:90': ['Funding'], 'var_functions.list_db:91': ['civic_docs']}

exec(code, env_args)
