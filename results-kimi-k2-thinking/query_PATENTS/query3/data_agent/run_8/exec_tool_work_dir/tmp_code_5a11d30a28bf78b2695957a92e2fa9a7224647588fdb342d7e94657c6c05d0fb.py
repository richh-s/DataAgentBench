code = """import json
import os

# Find the JSON file from the storage
storage_keys = list(locals().keys())
print('__RESULT__:')
print(json.dumps({
    'storage_keys': [k for k in storage_keys if 'var_' in k],
    'current_dir': os.listdir('/tmp')
}, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
