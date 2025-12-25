code = """import json

# Load the result from step 1
with open('var_function-call-4309411817698627857.json', 'r') as f:
    symbols_data = json.load(f)

# Load the result from step 2
with open('var_function-call-2225053238657252843.json', 'r') as f:
    tables_list = json.load(f)

# Extract symbols
target_symbols = [item['Symbol'] for item in symbols_data]
tables_set = set(tables_list)

# Find intersection
valid_symbols = [s for s in target_symbols if s in tables_set]

print(f"Total target symbols: {len(target_symbols)}")
print(f"Valid symbols in DB: {len(valid_symbols)}")

# Store valid symbols and their descriptions for later use
valid_companies = [item for item in symbols_data if item['Symbol'] in tables_set]

print("__RESULT__:")
print(json.dumps(valid_companies))"""

env_args = {'var_function-call-4309411817698627857': 'file_storage/function-call-4309411817698627857.json', 'var_function-call-2225053238657252843': 'file_storage/function-call-2225053238657252843.json'}

exec(code, env_args)
