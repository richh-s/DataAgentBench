code = """import json
import os

# Read the list of ETF symbols from the file
result_file = var_functions.query_db:0
with open(result_file, 'r') as f:
    etf_symbols = json.load(f)

# Extract just the symbols
symbols = [item['Symbol'] for item in etf_symbols]

print(f"Total NYSE Arca ETFs to check: {len(symbols)}")
print(f"First few symbols: {symbols[:5]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
