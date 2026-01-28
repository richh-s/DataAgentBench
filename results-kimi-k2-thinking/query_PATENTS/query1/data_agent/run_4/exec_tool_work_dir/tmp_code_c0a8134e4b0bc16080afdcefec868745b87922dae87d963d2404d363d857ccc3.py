code = """# Check what variables are available
print('Available variables:')
for key in dir():
    if not key.startswith('_'):
        print(f'  {key}')

# Try to access the variable directly
try:
    print('\nvar_functions.query_db_6 type:', type(var_functions.query_db_6))
    print('Length:', len(var_functions.query_db_6))
except Exception as e:
    print('\nError accessing var_functions.query_db_6:', e)

# Try with locals()
try:
    data = locals()['var_functions.query_db_6']
    print('\nUsing locals(), length:', len(data))
except Exception as e:
    print('\nError using locals():', e)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
