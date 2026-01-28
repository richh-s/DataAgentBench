code = """import pprint
# Just check what type of data we have
print('__RESULT__:')
print('Variables types:')
print(f"var_functions.query_db:10 type: {type(var_functions.query_db:10)}")
print(f"var_functions.query_db:8 type: {type(var_functions.query_db:8)}")"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
