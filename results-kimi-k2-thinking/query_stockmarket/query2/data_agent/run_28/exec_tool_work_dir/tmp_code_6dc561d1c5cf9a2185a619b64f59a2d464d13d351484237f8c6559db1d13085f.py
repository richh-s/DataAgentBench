code = """# Check available local variables
available_vars = [name for name in locals().keys() if name.startswith('var_')]
print('__RESULT__:')
print(str(available_vars))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)
