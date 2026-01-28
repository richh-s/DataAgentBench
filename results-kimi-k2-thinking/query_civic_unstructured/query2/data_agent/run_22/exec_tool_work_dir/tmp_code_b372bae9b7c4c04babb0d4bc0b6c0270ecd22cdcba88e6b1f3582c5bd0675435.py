code = """# Get the file path from the storage variable
filepath = var_functions.query_db_0

print('__RESULT__:')
print(f'filepath: {filepath}')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
