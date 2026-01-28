code = """import json
import pandas as pd

uni_california_patents_file = locals().get('var_functions.query_db:5', '')
print('File path:', uni_california_patents_file)

if uni_california_patents_file.endswith('.json'):
    with open(uni_california_patents_file, 'r') as f:
        data = json.load(f)
    print('Loaded', len(data), 'UNIV CALIFORNIA patents')
    
    # Show first record
    first_record = data[0]
    print('\nFirst record keys:', first_record.keys())
    print('Patents_info:', first_record.get('Patents_info', '')[:200])
    print('Citation field (first 500 chars):', str(first_record.get('citation', ''))[:500])
else:
    print('Unexpected file format')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
