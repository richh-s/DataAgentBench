code = """import json

# Read the full result from the file
result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    nyse_stocks = json.load(f)

print(f"Total NYSE non-ETF stocks: {len(nyse_stocks)}")
print(f"First few stocks: {nyse_stocks[:5]}")

# Extract just the symbols
symbols = [stock['Symbol'] for stock in nyse_stocks]
print(f"Sample symbols: {symbols[:10]}")

# Save the symbols list for further processing
print("__RESULT__:")
print(json.dumps(symbols))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
