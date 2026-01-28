code = """import json
import os
import re

# Access the storage variables - they're file paths
funding_file = 'var_functions.query_db:10'
civic_file = 'var_functions.query_db:22'

# Try to find the actual files in file_storage
try:
    # Read funding data
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
    
    # Read civic docs data
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
    
    print('__RESULT__:')
    print(json.dumps({
        'success': True,
        'funding_count': len(funding_data),
        'civic_docs_count': len(civic_docs),
        'sample_funding': funding_data[:3],
        'sample_civic': str(civic_docs[0])[:200] if civic_docs else 'No civic docs'
    }))
    
except Exception as e:
    print('__RESULT__:')
    print(json.dumps({
        'success': False,
        'error': str(e),
        'files_in_cwd': os.listdir('.')[:10]
    }))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:18': {'funding_path': 'file_storage/functions.query_db:10.json', 'civic_path': 'file_storage/functions.query_db:6.json', 'funding_path_type': "<class 'str'>", 'civic_path_type': "<class 'str'>"}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
