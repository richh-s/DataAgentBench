code = """import json
import os

# Check the storage variable
filepath = locals()['var_functions.query_db:2']
print('Filepath:', type(filepath))
print('Filepath value (first 200 chars):', str(filepath)[:200])

if isinstance(filepath, str) and os.path.exists(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
        result = {
            'record_count': len(data),
            'sample_record': data[0] if data else None
        }
else:
    result = {'error': 'File not found or invalid path'}

print('__RESULT__:')
print(json.dumps(result)[:1000])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'available_keys': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json']}}

exec(code, env_args)
