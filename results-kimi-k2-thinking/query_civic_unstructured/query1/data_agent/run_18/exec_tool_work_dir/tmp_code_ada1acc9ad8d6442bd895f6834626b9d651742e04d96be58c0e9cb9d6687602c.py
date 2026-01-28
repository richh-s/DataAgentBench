code = """import json

# Get the file paths from the previous queries
# The tool results are stored in variables with specific names
funding_path = var_functions.query_db_120
civic_path = var_functions.query_db_121

print('Funding file path:', funding_path)
print('Civic file path:', civic_path)

# Check if files exist
import os
print('Funding file exists?', os.path.exists(funding_path))
print('Civic file exists?', os.path.exists(civic_path))

result = {'funding_path': funding_path, 'civic_path': civic_path}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.list_db:90': ['Funding'], 'var_functions.list_db:91': ['civic_docs'], 'var_functions.execute_python:96': {'funding_count': 276, 'civic_count': 5}, 'var_functions.query_db:102': [{'count': '276'}], 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:106': 'file_storage/functions.query_db:106.json', 'var_functions.query_db:107': 'file_storage/functions.query_db:107.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json', 'var_functions.query_db:111': 'file_storage/functions.query_db:111.json', 'var_functions.query_db:114': 'file_storage/functions.query_db:114.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json', 'var_functions.query_db:117': 'file_storage/functions.query_db:117.json', 'var_functions.query_db:120': 'file_storage/functions.query_db:120.json', 'var_functions.query_db:121': 'file_storage/functions.query_db:121.json'}

exec(code, env_args)
