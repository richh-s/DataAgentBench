code = """import json
import os

# Check what we have stored
result_path = str(locals()['var_functions.query_db:0'])
print('__RESULT__:')
print(json.dumps({'path': result_path, 'type': str(type(result_path))}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:7': ['test'], 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:12': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'var_functions.query_db:14': [], 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json'}

exec(code, env_args)
