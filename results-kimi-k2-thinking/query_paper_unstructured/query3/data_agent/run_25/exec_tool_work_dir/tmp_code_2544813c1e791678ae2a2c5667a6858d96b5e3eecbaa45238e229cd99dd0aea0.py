code = """print('__RESULT__:')  
print('[]')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': []}

exec(code, env_args)
