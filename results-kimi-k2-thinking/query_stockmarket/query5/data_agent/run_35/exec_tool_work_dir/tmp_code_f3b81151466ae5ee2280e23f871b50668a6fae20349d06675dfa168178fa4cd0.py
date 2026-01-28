code = """import json
import pandas as pd

# Read the result from the previous query
with open('var_functions.query_db:0', 'r') as f:
    companies = json.load(f)

symbols = [company['Symbol'] for company in companies]
print(f"Total NASDAQ Capital Market companies: {len(symbols)}")
print(f"First 10 symbols: {symbols[:10]}")

# Create a mapping of symbol to company description
symbol_to_desc = {company['Symbol']: company['Company Description'] for company in companies}

# Print result in required format
result = {
    "total_companies": len(symbols),
    "sample_symbols": symbols[:10],
    "symbol_to_desc": symbol_to_desc
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
