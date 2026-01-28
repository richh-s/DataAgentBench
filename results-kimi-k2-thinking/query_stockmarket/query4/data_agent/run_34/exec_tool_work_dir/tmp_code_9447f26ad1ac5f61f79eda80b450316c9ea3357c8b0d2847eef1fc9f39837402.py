code = """import json
import os

# Read the full result from the previous query
result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    nyse_stocks = json.load(f)

# Print the count of NYSE stocks
print(f"Total NYSE non-ETF stocks: {len(nyse_stocks)}")

# Show first 5 stocks as sample
for i, stock in enumerate(nyse_stocks[:5]):
    print(f"{i+1}. {stock['Symbol']} - {stock['Company Description']}")

print(f"... and {len(nyse_stocks) - 5} more")"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
