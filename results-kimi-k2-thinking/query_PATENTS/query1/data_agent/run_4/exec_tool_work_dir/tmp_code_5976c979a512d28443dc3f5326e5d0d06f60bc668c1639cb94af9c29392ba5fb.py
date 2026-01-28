code = """# List all available variables
all_vars = dir()
print('All variables:')
for var in all_vars:
    if not var.startswith('_'):
        print(var)

# Now specifically look for query_db_6
if 'query_db_6' in locals():
    print('\nFound query_db_6 in locals')
elif 'var_functions.query_db_6' in locals():
    print('\nFound var_functions.query_db_6 in locals')
elif 'query_db_6' in globals():
    print('\nFound query_db_6 in globals')
elif 'var_functions.query_db_6' in globals():
    print('\nFound var_functions.query_db_6 in globals')
else:
    print('\nVariable not found directly')

# Let's check the storage information
print('\nChecking storage:')
storage_vars = [v for v in all_vars if 'storage' in v.lower() or 'json' in v.lower()]
print('Related vars:', storage_vars)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
