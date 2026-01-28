code = """import json, os, re

# Debug: check what files exist
files = os.listdir('/tmp')
civic_files = [f for f in files if 'civic' in f.lower() or 'query_db' in f]

result = {'files': files[:10], 'civic_related': civic_files}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:56': [], 'var_functions.execute_python:60': {'has_civic_file': False, 'has_funding_file': False}, 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
