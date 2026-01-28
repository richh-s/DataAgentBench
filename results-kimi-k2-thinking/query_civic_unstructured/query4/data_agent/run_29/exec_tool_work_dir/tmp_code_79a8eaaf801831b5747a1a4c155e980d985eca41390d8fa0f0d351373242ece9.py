code = """import json
import os

print('Testing file access...')

# Try to open funding data
funding_path = None
civic_path = None

# Check for files that might contain our data
for filename in os.listdir('.'):
    if 'query_db' in filename:
        print(f'Found file: {filename}')
        if '14' in filename or 'funding' in filename:
            funding_path = filename
        elif '24' in filename or 'civic' in filename:
            civic_path = filename

print(f'Funding file: {funding_path}')
print(f'Civic file: {civic_path}')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
