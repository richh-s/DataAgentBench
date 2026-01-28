code = """import json
metadata_path = locals()['var_functions.query_db:2']
with open(metadata_path, 'r') as f:
    metadata = json.load(f)
print('__RESULT__:')
print(json.dumps(len(metadata)))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json'}

exec(code, env_args)
