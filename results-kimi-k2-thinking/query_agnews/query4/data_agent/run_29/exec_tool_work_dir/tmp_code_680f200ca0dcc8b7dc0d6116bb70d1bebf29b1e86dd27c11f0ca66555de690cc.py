code = """# Let's see what's stored in the variable
print('__RESULT__:')
print(str(var_functions.query_db_2))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
