code = """import json
import os

# Get stored results
funding_raw = locals()['var_functions.query_db:2']
civic_raw = locals()['var_functions.query_db:0']

print("Funding raw type:", type(funding_raw))
print("Civic raw type:", type(civic_raw))

print('__RESULT__:')
print(json.dumps({'funding_type': str(type(funding_raw)), 'civic_type': str(type(civic_raw))}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
