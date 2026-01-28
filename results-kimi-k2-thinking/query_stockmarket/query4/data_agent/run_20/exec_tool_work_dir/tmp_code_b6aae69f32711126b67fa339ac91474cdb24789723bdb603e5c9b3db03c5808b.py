code = """print('__RESULT__:')
print('Starting analysis...')"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'type': 'str', 'length': 38, 'first_item': 'f'}}

exec(code, env_args)
