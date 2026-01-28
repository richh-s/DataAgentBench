code = """# Access the file path from the stored variable
file_path = locals()['var_functions.query_db:2']
print('File path:', file_path)"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
