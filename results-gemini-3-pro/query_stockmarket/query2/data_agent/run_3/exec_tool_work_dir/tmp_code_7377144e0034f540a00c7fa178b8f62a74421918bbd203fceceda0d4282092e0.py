code = """import json

# Get file paths from variables
etf_file_path = locals()['var_function-call-14301945511223140359']
table_file_path = locals()['var_function-call-6882633768806362112']

# Load data
with open(etf_file_path, 'r') as f:
    etf_list = json.load(f)

with open(table_file_path, 'r') as f:
    table_list = json.load(f)

# Extract symbols
etf_symbols = set([item['Symbol'] for item in etf_list])
available_tables = set(table_list)

# Intersection
valid_symbols = list(etf_symbols.intersection(available_tables))
valid_symbols.sort()

print("__RESULT__:")
print(json.dumps({"count": len(valid_symbols), "symbols": valid_symbols}))"""

env_args = {'var_function-call-14301945511223140359': 'file_storage/function-call-14301945511223140359.json', 'var_function-call-6882633768806362112': 'file_storage/function-call-6882633768806362112.json'}

exec(code, env_args)
