code = """import json

# First, let's see what we have available
import sys
print('Checking storage variables...')

# Check what variables are available from storage
storage_vars = []
for var_name in dir():
    if var_name.startswith('var_'):
        storage_vars.append(var_name)
        print(f"Found storage variable: {var_name}")

# Check if we have our funding and civic data
funding_key = None
civic_key = None

for var in storage_vars:
    if 'query_db' in var and ':5' in var:
        funding_key = var
    elif 'query_db' in var and ':2' in var:
        civic_key = var

print(f"\nFunding data key: {funding_key}")
print(f"Civic data key: {civic_key}")

# Now load the data if we found the keys
funding_data = []
civic_docs_data = []

if funding_key:
    funding_path = locals()[funding_key]
    print(f"Funding data path: {funding_path}")
    if isinstance(funding_path, str) and '.json' in funding_path:
        try:
            print("Loading funding data from file...")
            with open(funding_path, 'r') as f:
                funding_data = json.load(f)
            print(f"Loaded {len(funding_data)} funding records")
        except Exception as e:
            print(f"Error loading funding: {e}")
    else:
        print("Funding data is in memory")
        funding_data = funding_path

if civic_key:
    civic_path = locals()[civic_key]
    print(f"Civic data path: {civic_path}")
    if isinstance(civic_path, str) and '.json' in civic_path:
        try:
            print("Loading civic data from file...")
            with open(civic_path, 'r') as f:
                civic_docs_data = json.load(f)
            print(f"Loaded {len(civic_docs_data)} civic records")
        except Exception as e:
            print(f"Error loading civic: {e}")
    else:
        print("Civic data is in memory")
        civic_docs_data = civic_path

print('\n__RESULT__:')
result = {
    'funding_records': len(funding_data),
    'civic_records': len(civic_docs_data)
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
