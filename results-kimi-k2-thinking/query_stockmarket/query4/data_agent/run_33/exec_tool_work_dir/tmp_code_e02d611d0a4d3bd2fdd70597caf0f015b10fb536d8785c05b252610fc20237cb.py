code = """import json

# Read the stockinfo query result
with open('var_functions.query_db:0', 'r') as f:
    stockinfo_data = json.load(f)

# Read the list of tables from stocktrade database
with open('var_functions.list_db:2', 'r') as f:
    stocktrade_tables = json.load(f)

# Extract symbols from stockinfo that are NYSE non-ETF stocks
nyse_symbols = {item['Symbol'] for item in stockinfo_data}

# Convert stocktrade tables to a set for easy lookup
stocktrade_symbols = set(stocktrade_tables)

# Find intersection (stocks that exist in both)
available_stocks = nyse_symbols.intersection(stocktrade_symbols)

print('__RESULT__:')
print(json.dumps({
    'total_nyse_stocks': len(nyse_symbols),
    'total_stocktrade_tables': len(stocktrade_symbols),
    'available_for_analysis': len(available_stocks),
    'sample_stocks': list(available_stocks)[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
