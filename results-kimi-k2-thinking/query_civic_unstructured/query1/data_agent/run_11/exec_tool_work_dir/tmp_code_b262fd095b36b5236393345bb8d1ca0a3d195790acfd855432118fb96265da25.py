code = """import json
import os
import re

# Find all json files that might contain our data
json_files = []
for file in os.listdir('.'):
    if file.endswith('.json'):
        json_files.append(file)

# Check which variables are available
available_vars = []
for var_name in list(locals().keys()):
    if var_name.startswith('var_'):
        available_vars.append(var_name)

print('__RESULT__:')
print(json.dumps({
    'json_files': json_files,
    'available_vars': available_vars,
    'current_dir_files': os.listdir('.')[:20]  # First 20 files to avoid too much output
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'civic_docs_count': 0, 'civic_docs_sample': None, 'funding_data_count': 0, 'funding_data_sample': None}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 38, 'sample_doc': 'f'}}

exec(code, env_args)
