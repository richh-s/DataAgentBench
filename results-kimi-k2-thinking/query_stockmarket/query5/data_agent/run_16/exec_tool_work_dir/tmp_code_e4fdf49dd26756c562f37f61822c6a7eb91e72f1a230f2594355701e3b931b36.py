code = """# Let's check what variables are actually available
temp_vars = [k for k in locals().keys() if 'query_db' in k or 'list_db' in k]
print("Available variables:", temp_vars)"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)
