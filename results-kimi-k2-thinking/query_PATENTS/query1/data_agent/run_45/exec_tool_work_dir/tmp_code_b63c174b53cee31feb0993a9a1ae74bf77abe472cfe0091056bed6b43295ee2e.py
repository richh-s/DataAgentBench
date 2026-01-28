code = """import json
import os

# Read the JSON file directly
file_path = 'file_storage/functions.query_db:6.json'

if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        publications = json.load(f)
    
    print('__RESULT__:')
    print(json.dumps({
        'file_exists': True,
        'num_records': len(publications),
        'first_record_keys': list(publications[0].keys()) if publications else []
    }))
else:
    print('__RESULT__:')
    print(json.dumps({
        'file_exists': False,
        'checked_path': file_path,
        'available_files': os.listdir('file_storage') if os.path.exists('file_storage') else 'dir_not_found'
    }))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:14': {'file_exists': False, 'checked_paths': ['/tmp/tmp_result_6.json', 'tmp_result_6.json', '/tmp/tmptmp_result_6.json']}}

exec(code, env_args)
