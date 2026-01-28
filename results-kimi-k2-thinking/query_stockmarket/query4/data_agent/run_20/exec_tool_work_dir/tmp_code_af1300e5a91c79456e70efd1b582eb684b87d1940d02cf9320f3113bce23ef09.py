code = """# First, let's see what variables are available
available = [k for k in locals().keys() if k.startswith('var_')]
print('__RESULT__:')
print(str(available))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'type': 'str', 'length': 38, 'first_item': 'f'}}

exec(code, env_args)
