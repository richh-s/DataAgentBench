code = """import os, json

# List files in /tmp to find actual paths
tmp_files = []
for root, dirs, files in os.walk('/tmp'):
    for file in files:
        if file.endswith('.json'):
            full_path = os.path.join(root, file)
            tmp_files.append(full_path)

print('__RESULT__:')
print(json.dumps(tmp_files))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
