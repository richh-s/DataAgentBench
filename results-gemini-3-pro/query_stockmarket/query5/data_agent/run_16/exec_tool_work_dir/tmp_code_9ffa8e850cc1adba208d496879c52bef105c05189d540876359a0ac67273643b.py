code = """import json

# Get file paths from local variables
path1 = locals()['var_function-call-4309411817698627857']
path2 = locals()['var_function-call-2225053238657252843']

# Load the result from step 1
with open(path1, 'r') as f:
    symbols_data = json.load(f)

# Load the result from step 2
with open(path2, 'r') as f:
    tables_list = json.load(f)

# Extract symbols
target_symbols = [item['Symbol'] for item in symbols_data]
tables_set = set(tables_list)

# Find intersection
valid_symbols = [s for s in target_symbols if s in tables_set]

# Store valid symbols and their descriptions for later use
valid_companies = [item for item in symbols_data if item['Symbol'] in tables_set]

print(f"Total target symbols: {len(target_symbols)}")
print(f"Valid symbols in DB: {len(valid_symbols)}")

print("__RESULT__:")
print(json.dumps(valid_companies))"""

env_args = {'var_function-call-4309411817698627857': 'file_storage/function-call-4309411817698627857.json', 'var_function-call-2225053238657252843': 'file_storage/function-call-2225053238657252843.json'}

exec(code, env_args)
