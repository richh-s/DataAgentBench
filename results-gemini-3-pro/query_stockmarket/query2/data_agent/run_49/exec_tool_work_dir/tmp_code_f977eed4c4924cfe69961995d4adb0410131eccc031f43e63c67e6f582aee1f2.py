code = """import json

# Get file paths from variables
etf_file_path = locals()['var_function-call-5139739992729438025']
table_file_path = locals()['var_function-call-8590673828826687227']

# Load ETFs on NYSE Arca
with open(etf_file_path, 'r') as f:
    etf_list = json.load(f)

etf_symbols = set([item['Symbol'] for item in etf_list])

# Load tables in stocktrade_database
with open(table_file_path, 'r') as f:
    table_list = json.load(f)

table_set = set(table_list)

# Find intersection
valid_symbols = list(etf_symbols.intersection(table_set))

print(f"Total ETFs on NYSE Arca: {len(etf_symbols)}")
print(f"Total tables: {len(table_set)}")
print(f"Intersecting symbols: {len(valid_symbols)}")

print("__RESULT__:")
print(json.dumps(valid_symbols))"""

env_args = {'var_function-call-5139739992729438025': 'file_storage/function-call-5139739992729438025.json', 'var_function-call-8590673828826687227': 'file_storage/function-call-8590673828826687227.json'}

exec(code, env_args)
