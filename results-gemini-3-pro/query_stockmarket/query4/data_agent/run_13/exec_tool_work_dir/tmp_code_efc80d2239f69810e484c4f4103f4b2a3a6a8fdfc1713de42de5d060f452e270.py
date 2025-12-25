code = """import json

# Load stockinfo results
with open('var_function-call-17115240639510319133.json', 'r') as f:
    stock_candidates = json.load(f)

# Load stocktrade table names
with open('var_function-call-16575260045984015324.json', 'r') as f:
    trade_tables = json.load(f)

# Extract symbols
candidate_symbols = set(item['Symbol'] for item in stock_candidates)
available_tables = set(trade_tables)

# Find intersection
valid_symbols = list(candidate_symbols.intersection(available_tables))
valid_symbols.sort()

print(f"Number of valid symbols: {len(valid_symbols)}")
print("__RESULT__:")
print(json.dumps(valid_symbols))"""

env_args = {'var_function-call-17115240639510319133': 'file_storage/function-call-17115240639510319133.json', 'var_function-call-16575260045984015324': 'file_storage/function-call-16575260045984015324.json'}

exec(code, env_args)
