code = """# Access the file path stored in the variable
citations_file_path = var_functions.query_db:2
print(f"File path: {citations_file_path}")"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
