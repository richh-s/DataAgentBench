code = """import json

# Read the full result from the file
with open('stockinfo_nyse_non_etf.json', 'r') as f:
    nyse_stocks = json.load(f)

print(f"Number of NYSE non-ETF stocks: {len(nyse_stocks)}")
print("First 10 stocks:", nyse_stocks[:10])
print("__RESULT__:")
print(json.dumps(nyse_stocks))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
