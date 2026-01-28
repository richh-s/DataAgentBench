code = """import json
import os

# Get all variables
all_vars = dir()
print('All variables:', [v for v in all_vars if 'functions' in v])

# Check what files exist
print('\nFiles in /tmp:')
tmp_files = os.listdir('/tmp')
print([f for f in tmp_files if f.startswith('tmp')])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
