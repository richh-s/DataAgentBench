code = """# First, let's see what data we have available
available_vars = [name for name in dir() if not name.startswith('_')]
print('Available variables:', available_vars)

# Try to find our data
for var_name in available_vars:
    if 'query_db' in var_name:
        print(f"\nFound: {var_name}")
        var_value = globals().get(var_name) or locals().get(var_name)
        print(f"Type: {type(var_value)}")
        if hasattr(var_value, '__len__'):
            print(f"Length: {len(var_value)}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
