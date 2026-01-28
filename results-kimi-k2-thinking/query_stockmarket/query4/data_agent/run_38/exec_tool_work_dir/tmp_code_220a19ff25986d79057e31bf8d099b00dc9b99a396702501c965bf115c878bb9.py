code = """import json

# Get the file path from storage
file_path = locals()['var_functions.query_db:0']
print('__RESULT__:')
print(json.dumps({'file_path': file_path, 'type': str(type(file_path))}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
