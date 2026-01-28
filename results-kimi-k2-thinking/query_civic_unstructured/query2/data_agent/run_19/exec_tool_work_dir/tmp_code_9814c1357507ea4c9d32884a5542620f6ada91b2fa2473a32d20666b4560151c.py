code = """import json
import sys

# Check what variables we have
locals_keys = list(locals().keys())
print('Available variables:', locals_keys[:10])

# Get the actual data
funding_data = locals().get('var_functions.query_db:0')
civic_docs = locals().get('var_functions.query_db:4')

print('Funding data type:', type(funding_data))
print('Civic docs type:', type(civic_docs))

# Check if they are lists
if isinstance(funding_data, list):
    print('Funding records:', len(funding_data))
    if funding_data:
        print('First funding record:', funding_data[0])

if isinstance(civic_docs, list):
    print('Civic docs records:', len(civic_docs))
    if civic_docs:
        print('First civic doc keys:', civic_docs[0].keys() if isinstance(civic_docs[0], dict) else type(civic_docs[0]))

print('__RESULT__:')
print(json.dumps({'status': 'inspection_complete'}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
