code = """import json

result_path = var_functions.execute_python:20

with open(result_path, 'r') as f:
    result_data = json.load(f)

cpc_codes = result_data['cpc_codes']

for code in cpc_codes:
    print(code)

print('__RESULT__:')
print(json.dumps(cpc_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json'}

exec(code, env_args)
