code = """# Directly access the stored variable
nyse_var = locals().get('var_functions.query_db:2')
print('__RESULT__:')
print(type(nyse_var).__name__ if nyse_var is not None else 'None')"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
