code = """import json
import os

# Try to locate the data files
data_files = []
for f in os.listdir('/tmp'):
    if f.endswith('.json'):
        data_files.append(f'/tmp/{f}')

print('__RESULT__:')
print(json.dumps({'files': data_files}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json'}

exec(code, env_args)
