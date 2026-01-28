code = """import json
import os

# Read the full result from the file
result_file = var_functions.query_db:0
with open(result_file, 'r') as f:
    nasdaq_capital_stocks = json.load(f)

print(f"Total NASDAQ Capital Market stocks: {len(nasdaq_capital_stocks)}")
print("First 10 symbols:", [s['Symbol'] for s in nasdaq_capital_stocks[:10]])
print("__RESULT__:")
print(json.dumps(nasdaq_capital_stocks[:100]))  # Return first 100 as preview"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
