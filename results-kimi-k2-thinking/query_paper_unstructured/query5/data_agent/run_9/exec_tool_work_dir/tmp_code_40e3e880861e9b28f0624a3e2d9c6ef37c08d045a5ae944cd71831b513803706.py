code = """# First, let's check what the storage keys contain
result_keys = [key for key in locals().keys() if 'var_' in key]
print('__RESULT__:')
print(result_keys)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
