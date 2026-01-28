code = """import os
import glob

# Find all JSON files in tmp directories
all_files = []
for root, dirs, files in os.walk('/tmp'):
    for file in files:
        if file.endswith('.json'):
            all_files.append(os.path.join(root, file))

print('JSON files found:')
for f in all_files:
    print('  ' + f)

# Also check for temp directories
print('\nTemp directories:')
for root, dirs, files in os.walk('/tmp'):
    for dir in dirs:
        if dir.startswith('tmp'):
            print('  ' + os.path.join(root, dir))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
