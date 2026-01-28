code = """import json, os

# Let's check what's in the storage
target_key = 'var_functions.query_db:5'
print('Target storage key:', target_key)
print('Type of target_key:', type(target_key))
print('String value:', str(target_key))

# Check if it's directly accessible as a variable
try:
    print('Direct access attempt...')
    data = target_key
    print('Direct access successful:', type(data))
    if isinstance(data, str) and '.json' in data:
        if os.path.exists(data):
            with open(data, 'r') as f:
                loaded_data = json.load(f)
            print('Loaded JSON successfully, type:', type(loaded_data))
            print('Length:', len(loaded_data))
        else:
            print('File does not exist:', data)
    else:
        print('Data is not a JSON file path or does not exist')
        print('Data preview:', str(data)[:200])
except Exception as e:
    print('Error in direct access:', e)

# Let's try reading the variable from locals or globals
print('\nChecking local variables:')
for key in list(locals().keys()):
    if 'query_db' in key or 'german' in key:
        print(f'  {key}: {type(locals()[key])}')

print('\nChecking globals:')
for key in list(globals().keys()):
    if 'query_db' in key or 'german' in key:
        print(f'  {key}: {type(globals()[key])}')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
