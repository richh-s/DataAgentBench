code = """import json

# Read the file from the stored path
file_path = locals()['var_functions.query_db:0']
print(f"File path: {file_path}")

with open(file_path, 'r') as f:
    nyse_stocks = json.load(f)

print(f"Total NYSE non-ETF stocks loaded: {len(nyse_stocks)}")
print(f"First 5 records: {nyse_stocks[:5]}")

# Extract symbols
symbols = [stock['Symbol'] for stock in nyse_stocks]
result = {"symbols": symbols, "count": len(symbols), "file_path": file_path}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
