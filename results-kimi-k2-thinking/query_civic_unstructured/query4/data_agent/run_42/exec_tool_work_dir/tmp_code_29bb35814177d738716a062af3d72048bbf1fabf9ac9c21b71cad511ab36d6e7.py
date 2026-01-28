code = """import json
import os

# Check what files exist in /tmp
print('Files in /tmp:')
for f in os.listdir('/tmp'):
    if f.startswith('tmp'):
        print(f)

# Also check the variables
print('\nVariable names:')
for key in locals().keys():
    if key.startswith('var_functions'):
        print(key, '=', locals()[key])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
