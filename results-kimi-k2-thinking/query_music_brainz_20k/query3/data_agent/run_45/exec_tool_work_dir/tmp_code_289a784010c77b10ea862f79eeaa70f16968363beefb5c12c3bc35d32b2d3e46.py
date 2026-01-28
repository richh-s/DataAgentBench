code = """import json
with open(var_functions.query_db:5, 'r') as f:
    tracks = json.load(f)
print('__RESULT__:')
print(json.dumps({'count': len(tracks)}))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:1': ['sales'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'test': 123}}

exec(code, env_args)
