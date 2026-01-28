code = """import json, os, sys

# Get all variables that start with var_functions.query_db
all_vars = [k for k in globals().keys() if 'var_functions.query_db' in k]
print('Available query_db variables:', all_vars)

# Check if we can access the full data through any variable
if 'var_functions.query_db:5' in globals():
    data = globals()['var_functions.query_db:5']
    print('Type of data:', type(data))
    if isinstance(data, list):
        print('Number of documents:', len(data))
        if len(data) > 0:
            print('First doc keys:', list(data[0].keys()))

result = {'available_vars': all_vars}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'status': 'error', 'message': "[Errno 2] No such file or directory: '/tmp/tmpub7z9f6a.json'"}}

exec(code, env_args)
