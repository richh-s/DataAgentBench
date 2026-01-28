code = """packages_data = locals()['var_functions.query_db:0']
ppv_data = locals()['var_functions.query_db:2']

print('__RESULT__:')
print('ok')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
