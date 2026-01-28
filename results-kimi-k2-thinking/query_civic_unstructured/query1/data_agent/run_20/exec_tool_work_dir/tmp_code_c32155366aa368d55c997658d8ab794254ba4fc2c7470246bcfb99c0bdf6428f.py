code = """import json, os
# Load funding data
key0 = 'var_functions.query_db:0'
with open(locals()[key0], 'r') as f:
    funding_data = json.load(f)
print('__RESULT__:')
print('Funding records loaded')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
