code = """import json, os, re

# Get list of files
files = os.listdir('.')
print('Files:', files)

# Find our data files
for f in files:
    if 'query_db' in f:
        size = os.path.getsize(f)
        print(f'File: {f}, Size: {size}')
        
        with open(f, 'r') as file:
            data = json.load(file)
            print(f'  Records: {len(data)}')
            if data:
                print(f'  First record keys: {list(data[0].keys())}')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
