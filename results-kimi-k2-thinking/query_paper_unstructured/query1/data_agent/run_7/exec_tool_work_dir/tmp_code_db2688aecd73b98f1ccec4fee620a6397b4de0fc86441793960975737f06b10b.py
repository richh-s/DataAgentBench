code = """import json

# Check what the variable contains
path = locals()['var_functions.query_db:2']
print('__RESULT__:')
print(json.dumps({'path_type': str(type(path)), 'path_value': str(path)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
