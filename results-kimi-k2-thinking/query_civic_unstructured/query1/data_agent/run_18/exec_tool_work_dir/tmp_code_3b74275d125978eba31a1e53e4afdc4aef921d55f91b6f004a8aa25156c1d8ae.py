code = """import json

# Get the file paths from the previous tool results
funding_path = var_functions.query_db:120
civic_path = var_functions.query_db:121

print('Funding data key:', repr(funding_path))
print('Civic docs key:', repr(civic_path))

# The variables should be strings pointing to temporary files
result = {
    'funding_path_type': type(funding_path).__name__,
    'civic_path_type': type(civic_path).__name__,
    'funding_path_value': str(funding_path)[:100],
    'civic_path_value': str(civic_path)[:100]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.list_db:90': ['Funding'], 'var_functions.list_db:91': ['civic_docs'], 'var_functions.execute_python:96': {'funding_count': 276, 'civic_count': 5}, 'var_functions.query_db:102': [{'count': '276'}], 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:106': 'file_storage/functions.query_db:106.json', 'var_functions.query_db:107': 'file_storage/functions.query_db:107.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json', 'var_functions.query_db:111': 'file_storage/functions.query_db:111.json', 'var_functions.query_db:114': 'file_storage/functions.query_db:114.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json', 'var_functions.query_db:117': 'file_storage/functions.query_db:117.json', 'var_functions.query_db:120': 'file_storage/functions.query_db:120.json', 'var_functions.query_db:121': 'file_storage/functions.query_db:121.json'}

exec(code, env_args)
