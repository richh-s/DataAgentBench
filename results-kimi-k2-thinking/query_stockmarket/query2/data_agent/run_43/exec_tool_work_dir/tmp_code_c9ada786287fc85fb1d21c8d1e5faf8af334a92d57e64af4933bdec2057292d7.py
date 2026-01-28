code = """# Let's inspect the variable first
stored_var = locals()['var_functions.query_db:0']
print('__RESULT__:')
print(json.dumps({'type': str(type(stored_var)), 'value': str(stored_var)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
