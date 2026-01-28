code = """import json
import os
from collections import defaultdict

# Try to find the file
possible_paths = [
    '/tmp/tmp_result_6.json',
    'tmp_result_6.json',
    '/tmp/tmptmp_result_6.json'
]

for path in possible_paths:
    if os.path.exists(path):
        print('__RESULT__:')
        print(json.dumps({'file_exists': True, 'path': path}))
        break
else:
    print('__RESULT__:')
    print(json.dumps({'file_exists': False, 'checked_paths': possible_paths}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
