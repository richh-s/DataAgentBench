code = """import json
import pandas as pd

# Load NYSE non-ETF stocks
nyse_stocks_file = var_functions.query_db:2
with open(nyse_stocks_file, 'r') as f:
    nyse_stocks = json.load(f)

# Load available tables in stocktrade_database
stocktrade_tables_file = var_functions.list_db:5
with open(stocktrade_tables_file, 'r') as f:
    stocktrade_tables = json.load(f)

# Create a set of available table names for quick lookup
available_tables = set(stocktrade_tables)

# Filter NYSE stocks that have data in stocktrade_database
valid_stocks = []
for stock in nyse_stocks:
    symbol = stock['Symbol']
    if symbol in available_tables:
        valid_stocks.append(stock)

print(f"Found {len(valid_stocks)} NYSE non-ETF stocks with trade data")
print(f"First few: {[s['Symbol'] for s in valid_stocks[:10]]}")

# Store for next step
result = {
    'valid_stocks': valid_stocks,
    'available_tables': list(available_tables)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.query_db:6': [{'name': 'AAAU'}, {'name': 'AADR'}, {'name': 'AAME'}, {'name': 'AAWW'}, {'name': 'AAXJ'}, {'name': 'ABEQ'}, {'name': 'ABMD'}, {'name': 'ACAD'}, {'name': 'ACES'}, {'name': 'ACIO'}]}

exec(code, env_args)
