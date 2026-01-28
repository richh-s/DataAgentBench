code = """import json

# Let's get all variables with 'query_db' in the name
query_db_vars = {}
for key, value in globals().items():
    if 'query_db' in key:
        query_db_vars[key] = value

print('Found query_db variables:', list(query_db_vars.keys()))

# Process each variable
for var_name, var_value in query_db_vars.items():
    print(f"\n{var_name}:")
    print(f"  Type: {type(var_value)}")
    
    if isinstance(var_value, list):
        print(f"  Direct data with {len(var_value)} records")
        # Check if this is funding or civic data
        if len(var_value) > 0:
            sample = var_value[0]
            print(f"  Sample keys: {list(sample.keys())}")
    elif isinstance(var_value, str):
        if 'file_storage' in var_value:
            print(f"  File path: {var_value}")
            try:
                with open(var_value, 'r') as f:
                    data = json.load(f)
                    print(f"  Loaded data with {len(data)} records")
                    # Store in a more convenient variable
                    globals()[var_name.replace(':', '_') + '_data'] = data
            except Exception as e:
                print(f"  Error loading file: {e}")
    else:
        print(f"  Unhandled type: {type(var_value)}")"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
