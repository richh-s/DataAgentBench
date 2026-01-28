code = """# Access the variable directly from locals
data_var = locals()['var_functions.query_db:2']
print("Type of data_var:", type(data_var))
print("Content:", str(data_var)[:200])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
