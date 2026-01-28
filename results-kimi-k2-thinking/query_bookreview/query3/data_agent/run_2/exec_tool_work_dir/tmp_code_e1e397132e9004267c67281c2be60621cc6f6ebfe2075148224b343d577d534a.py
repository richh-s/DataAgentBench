code = """table_names = locals()['var_functions.list_db:0']
print('__RESULT__:')
print(str(table_names))"""

env_args = {'var_functions.list_db:0': ['review']}

exec(code, env_args)
