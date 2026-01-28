code = """# Check available storage keys more carefully
import json

# Get all available keys
all_keys = sorted([k for k in globals().keys() if k.startswith('var_functions')])
print('Available storage keys:', all_keys)

# Let's try different approaches to access the data
for key in all_keys:
    try:
        value = globals()[key]
        print(f"{key}: {type(value)}")
        if isinstance(value, str) and 'file_storage' in value:
            print(f"  File path: {value}")
            # Load the file
            with open(value, 'r') as f:
                data = json.load(f)
                print(f"  Loaded {len(data)} records")
            # Store it in a more accessible variable
            globals()[key + '_data'] = data
        elif isinstance(value, list):
            print(f"  Direct data with {len(value)} records")
    except Exception as e:
        print(f"  Error accessing {key}: {e}")"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
