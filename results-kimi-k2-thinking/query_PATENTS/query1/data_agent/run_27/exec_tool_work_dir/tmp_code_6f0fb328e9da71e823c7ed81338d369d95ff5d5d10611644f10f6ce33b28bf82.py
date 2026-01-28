code = """import json

# Read the result from the previous analysis
result_path = locals()['var_functions.execute_python:44']
with open(result_path, 'r') as f:
    result_data = json.load(f)

cpc_codes_2022 = result_data['cpc_codes_2022']

# Get unique codes
unique_codes = sorted(list(set(cpc_codes_2022)))

# Format output as requested - each code on a new line
output = '\n'.join(unique_codes)

print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.query_db:32': [], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.execute_python:44': 'file_storage/functions.execute_python:44.json'}

exec(code, env_args)
