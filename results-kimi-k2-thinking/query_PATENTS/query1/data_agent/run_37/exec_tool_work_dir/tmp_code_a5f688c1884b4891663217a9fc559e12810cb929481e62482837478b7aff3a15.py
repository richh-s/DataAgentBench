code = """import json

# Check what variables are available
available_vars = [k for k in locals().keys() if k.startswith('var_')]
print('Available variables:', available_vars)

# Try to access the stored result
if 'var_functions.query_db:6' in locals():
    result = locals()['var_functions.query_db:6']
    print('Result type:', type(result))
    print('Result preview:', str(result)[:200])
else:
    print('var_functions.query_db:6 not found')

print('__RESULT__:')
print('test')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
