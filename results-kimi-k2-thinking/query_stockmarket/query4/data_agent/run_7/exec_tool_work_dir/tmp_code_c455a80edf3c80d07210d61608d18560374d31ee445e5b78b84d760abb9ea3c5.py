code = """import json, os

# The result is stored in var_functions.query_db:0
result = var_functions.query_db:0

# If it's a file path, read it; otherwise, use it directly
if isinstance(result, str) and result.endswith('.json'):
    with open(result, 'r') as f:
        data = json.load(f)
else:
    data = result

print('__RESULT__:')
print(json.dumps({'count': len(data), 'sample': data[:3]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
