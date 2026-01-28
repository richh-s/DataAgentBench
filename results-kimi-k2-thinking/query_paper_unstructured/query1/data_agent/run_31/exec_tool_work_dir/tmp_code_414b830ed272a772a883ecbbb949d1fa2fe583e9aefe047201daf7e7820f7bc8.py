code = """import os
import json

# Check current directory structure
print('Current working directory:', os.getcwd())
print('Directory listing:')
for item in os.listdir('.'):
    print('  ', item)

# Check if storage directory exists and what's in it
storage_paths = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.startswith('query_') and file.endswith('.json'):
            filepath = os.path.join(root, file)
            storage_paths.append(filepath)
            print('Found data file:', filepath)

print('Total data files found:', len(storage_paths))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
