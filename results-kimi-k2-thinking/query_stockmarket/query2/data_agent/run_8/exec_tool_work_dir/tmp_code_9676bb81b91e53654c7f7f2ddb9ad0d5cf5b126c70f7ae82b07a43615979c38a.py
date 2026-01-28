code = """import json

# Load the symbols from the previous query
symbols_file = var_functions.query_db:6
if isinstance(symbols_file, str) and symbols_file.endswith('.json'):
    with open(symbols_file, 'r') as f:
        symbols_data = json.load(f)
else:
    symbols_data = var_functions.query_db:6

# Extract just the symbol values
symbols = [item['Symbol'] for item in symbols_data]

print(f"Total NYSE Arca ETFs to check: {len(symbols)}")
print("First 10 symbols:", symbols[:10])

# Store results
qualifying_etfs = []
error_symbols = []

# We'll need to query each symbol's table
# For simplicity, let's check a few first to see if the approach works
for i, symbol in enumerate(symbols[:50]):  # Test with first 50
    print(f"Checking {i+1}/{len(symbols)}: {symbol}")

print("__RESULT__:")
print(json.dumps({"total_symbols": len(symbols), "sample_symbols": symbols[:10]}))"""

env_args = {'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
