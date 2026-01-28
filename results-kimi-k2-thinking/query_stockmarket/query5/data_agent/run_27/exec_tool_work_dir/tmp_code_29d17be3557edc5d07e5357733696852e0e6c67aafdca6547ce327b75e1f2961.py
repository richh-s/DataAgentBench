code = """import json
result_key = 'var_functions.query_db:22'
print('Result key type:', type(locals().get(result_key)))
print('Result key value:', locals().get(result_key)[:200] if locals().get(result_key) else 'None')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.list_db:7': ['stockinfo'], 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.list_db:24': 'file_storage/functions.list_db:24.json'}

exec(code, env_args)
