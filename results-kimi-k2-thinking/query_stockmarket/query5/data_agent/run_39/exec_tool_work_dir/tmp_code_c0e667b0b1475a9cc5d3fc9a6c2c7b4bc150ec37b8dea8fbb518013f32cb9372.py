code = """import json

# Read the file path from the variable
file_path = var_functions.query_db:0

# Read the full result from the file
with open(file_path, 'r') as f:
    nasdaq_capital_stocks = json.load(f)

# Extract tickers
tickers = [stock['Symbol'] for stock in nasdaq_capital_stocks]

print(f"__RESULT__:")
print(json.dumps({"tickers_count": len(tickers), "sample_tickers": tickers[:10]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
