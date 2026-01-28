code = """import json
print('__RESULT__:')
print(json.dumps(['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:5']))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)
