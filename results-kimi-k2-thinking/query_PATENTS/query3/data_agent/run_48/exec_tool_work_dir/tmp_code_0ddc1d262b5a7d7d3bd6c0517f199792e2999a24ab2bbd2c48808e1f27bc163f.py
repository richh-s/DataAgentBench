code = """import json

# Check what the variable contains
result_var = var_functions.query_db:2
print(f"Type of result_var: {type(result_var)}")
print(f"Value of result_var: {result_var}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
