code = """import json
result_path = 'var_functions.query_db:0'
print(result_path)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
