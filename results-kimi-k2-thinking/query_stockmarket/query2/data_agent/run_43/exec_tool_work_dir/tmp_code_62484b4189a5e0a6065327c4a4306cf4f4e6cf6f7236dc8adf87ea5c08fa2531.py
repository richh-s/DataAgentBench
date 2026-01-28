code = """import json

# Inspect the stored variable
stored_var = locals()['var_functions.query_db:0']
result_dict = {'type': str(type(stored_var)), 'value': str(stored_var)}
print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
