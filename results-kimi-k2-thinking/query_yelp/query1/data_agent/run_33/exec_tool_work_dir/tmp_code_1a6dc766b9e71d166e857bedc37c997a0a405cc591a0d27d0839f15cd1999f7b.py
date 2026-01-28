code = """# Read the full result from file
result_file = locals()['var_functions.query_db:2']
print('File path:', result_file)"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
