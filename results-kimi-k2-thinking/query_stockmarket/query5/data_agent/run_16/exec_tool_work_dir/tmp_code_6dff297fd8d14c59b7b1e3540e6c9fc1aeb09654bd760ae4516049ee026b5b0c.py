code = """import json
# Read the preview to understand the data structure
print(type(var_functions.query_db_2))
print(str(var_functions.query_db_2)[:200])"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)
