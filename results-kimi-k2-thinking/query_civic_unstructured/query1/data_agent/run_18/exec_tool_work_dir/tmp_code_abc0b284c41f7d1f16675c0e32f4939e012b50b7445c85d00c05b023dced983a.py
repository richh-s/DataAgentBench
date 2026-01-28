code = """import json
import re

# Get file paths (these should be strings pointing to temporary files)
funding_result = var_functions.query_db:70
civic_result = var_functions.query_db:71

print('Funding result type:', type(funding_result))
print('Civic result type:', type(civic_result))

# Load the actual data
with open(funding_result) as f:
    funding_data = json.load(f)

with open(civic_result) as f:
    civic_docs = json.load(f)

print('Loaded', len(funding_data), 'funding records')
print('Loaded', len(civic_docs), 'civic documents')

# Show first few funding records
print('First 3 funding records:', funding_data[:3])

# Show first civic doc structure
if civic_docs:
    print('First civic doc keys:', civic_docs[0].keys())
    print('Civic doc text preview:', civic_docs[0].get('text', '')[:200])

print('__RESULT__:')
print(json.dumps({'status': 'data_loaded'}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.list_db:90': ['Funding'], 'var_functions.list_db:91': ['civic_docs'], 'var_functions.execute_python:96': {'funding_count': 276, 'civic_count': 5}}

exec(code, env_args)
