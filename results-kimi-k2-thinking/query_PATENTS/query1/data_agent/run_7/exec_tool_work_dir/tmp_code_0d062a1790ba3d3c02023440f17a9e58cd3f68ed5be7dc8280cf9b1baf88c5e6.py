code = """# Check what type of data is stored in the key
key_data = var_functions.query_db:2
print(f"Type of storage data: {type(key_data)}")
print(f"Storage data content: {str(key_data)[:200]}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
