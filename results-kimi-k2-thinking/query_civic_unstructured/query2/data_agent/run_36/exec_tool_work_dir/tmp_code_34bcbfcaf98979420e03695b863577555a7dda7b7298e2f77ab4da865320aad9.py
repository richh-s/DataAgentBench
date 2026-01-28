code = """import json
import os
import re

# Get all files from tmp
tmp_files = os.listdir('/tmp')
print('Files found:', tmp_files)

# Try to find our data files
results = {}
for fname in tmp_files:
    if fname.endswith('.json'):
        path = os.path.join('/tmp', fname)
        try:
            with open(path, 'r') as f:
                data = json.load(f)
                results[fname] = {
                    'records': len(data),
                    'first_record': data[0] if data else None
                }
        except:
            results[fname] = {'error': 'Could not parse'}

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.execute_python:34': {'files': []}}

exec(code, env_args)
