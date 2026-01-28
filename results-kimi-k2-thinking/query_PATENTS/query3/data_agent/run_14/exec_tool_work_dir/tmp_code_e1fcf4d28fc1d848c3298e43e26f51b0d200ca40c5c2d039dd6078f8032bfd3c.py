code = """# First check what the variable contains
storage_key = 'var_functions.query_db:2'
print('Storage key:', storage_key)
print('Type of value:', type(locals()[storage_key]))
print('Value:', locals()[storage_key])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
