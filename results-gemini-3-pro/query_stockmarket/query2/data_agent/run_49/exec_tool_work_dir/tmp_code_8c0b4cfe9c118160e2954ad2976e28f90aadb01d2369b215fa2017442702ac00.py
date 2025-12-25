code = """import json

# Load ETFs on NYSE Arca
with open('var_function-call-5139739992729438025.json', 'r') as f:
    etf_list = json.load(f)

etf_symbols = set([item['Symbol'] for item in etf_list])

# Load tables in stocktrade_database
with open('var_function-call-8590673828826687227.json', 'r') as f:
    table_list = json.load(f)

table_set = set(table_list)

# Find intersection
valid_symbols = list(etf_symbols.intersection(table_set))

print(f"Total ETFs on NYSE Arca: {len(etf_symbols)}")
print(f"Total tables: {len(table_set)}")
print(f"Intersecting symbols: {len(valid_symbols)}")

# Check if we can construct a massive UNION query
# Or if we should query them in batches.
# Let's print the first 20 symbols to see.
print(f"Sample symbols: {valid_symbols[:20]}")

print("__RESULT__:")
print(json.dumps(valid_symbols))"""

env_args = {'var_function-call-5139739992729438025': 'file_storage/function-call-5139739992729438025.json', 'var_function-call-8590673828826687227': 'file_storage/function-call-8590673828826687227.json'}

exec(code, env_args)
