code = """import json, os

# Assuming the variable is available and it contains a file path if too large
list_db_path = globals()['var_functions.list_db:0']
print('__RESULT__:')
print(json.dumps(list_db_path))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
