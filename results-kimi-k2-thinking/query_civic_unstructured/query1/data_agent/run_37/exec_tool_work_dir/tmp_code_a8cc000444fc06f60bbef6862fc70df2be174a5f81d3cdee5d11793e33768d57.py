code = """# Let's see what variables are available in the global namespace
available_vars = [k for k in globals().keys() if not k.startswith('__')]
print('Available variables:', available_vars[:20])

# Also check locals
local_vars = [k for k in locals().keys() if not k.startswith('__')]
print('Local variables:', local_vars[:20])

# Check if we have any mongo or sql results
for var in available_vars:
    if 'query' in var.lower() or 'db' in var.lower():
        print(f"{var}: {type(globals()[var])}")"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
