code = """import json

# Try to understand what variables are available
keys = [k for k in locals().keys() if k.startswith('var_')]
print('Available variables:', keys)

# Print type and value of one variable if exists
for key in keys:
    val = locals()[key]
    print(f'{key}: type={type(val)}, value={val[:100] if isinstance(val, str) else str(val)[:100]}')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
