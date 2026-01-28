code = """import json
import os

# Debugging info
print('__RESULT__:')
print(json.dumps({
    'has_civic_file': os.path.exists('var_functions.query_db_36'),
    'has_funding_file': os.path.exists('var_functions.query_db_8')
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:56': []}

exec(code, env_args)
