code = """import json
import os

# Read the result from the previous query
result_file = var_functions.query_db:0
with open(result_file, 'r') as f:
    stocks_data = json.load(f)

print(f"Number of NASDAQ Capital Market stocks: {len(stocks_data)}")
print(f"First few records: {stocks_data[:5]}")

# Extract symbols and company names
symbols = [stock['Symbol'] for stock in stocks_data]
company_names = {stock['Symbol']: stock['Company Description'] for stock in stocks_data}

print(f"Sample symbols: {symbols[:10]}")

# Prepare data for next step
print('__RESULT__:')
print(json.dumps({
    'symbols': symbols,
    'company_names': company_names,
    'count': len(symbols)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
