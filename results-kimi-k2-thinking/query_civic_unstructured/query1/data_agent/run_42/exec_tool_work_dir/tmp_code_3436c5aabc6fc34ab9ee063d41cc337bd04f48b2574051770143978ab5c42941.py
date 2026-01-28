code = """import json

# Debug what's available
all_vars = dir()
print('All variables:', all_vars)

# Try to access the stored results
for var_name in all_vars:
    if 'query_db' in var_name:
        print(f'Found: {var_name}')
        
__RESULT__ = json.dumps({'status': 'debug'})"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
