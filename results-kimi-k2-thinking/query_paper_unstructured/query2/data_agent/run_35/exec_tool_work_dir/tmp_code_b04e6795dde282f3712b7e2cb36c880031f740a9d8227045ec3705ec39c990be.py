code = """import json
import os
import re

# Get the storage variables
storage_keys = [key for key in locals().keys() if key.startswith('var_')]
print('__RESULT__:')
print(json.dumps({'storage_keys': storage_keys, 'all_vars': list(locals().keys())}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:1': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
