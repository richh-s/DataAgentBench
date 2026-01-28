code = """import json

# Check what the variable contains
print('__RESULT__:')
print(json.dumps({'type': str(type(var_functions.query_db:0)), 'value': str(var_functions.query_db:0)[:1000]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
