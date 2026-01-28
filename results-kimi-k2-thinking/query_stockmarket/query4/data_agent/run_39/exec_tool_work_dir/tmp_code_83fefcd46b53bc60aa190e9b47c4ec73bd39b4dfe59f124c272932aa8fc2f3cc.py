code = """import json
# Read the file path stored in var_functions.query_db:0
file_path = locals()['var_functions.query_db:0']
with open(file_path, 'r') as f:
    data = json.load(f)
# Get count of entries
print('__RESULT__:')
print(json.dumps({'count': len(data)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
