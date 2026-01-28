code = """import pandas as pd
import json
import os

# Check what temporary directory exists and what files are there
tmp_files = []
for root, dirs, files in os.walk('/tmp'):
    for file in files:
        if file.endswith('.json'):
            tmp_files.append(os.path.join(root, file))

result_path = None
if tmp_files:
    # Find the most recent file that might contain our query result
    for f in sorted(tmp_files, key=os.path.getmtime, reverse=True):
        if 'publicationinfo' in f or len(f) > 20:
            result_path = f
            break

print('__RESULT__:')
print(json.dumps({
    'tmp_files': tmp_files[:10],
    'result_path': result_path,
    'pwd': os.getcwd()
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'available_vars': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', '__builtins__', 'json']}, 'var_functions.list_db:14': ['cpc_definition'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
