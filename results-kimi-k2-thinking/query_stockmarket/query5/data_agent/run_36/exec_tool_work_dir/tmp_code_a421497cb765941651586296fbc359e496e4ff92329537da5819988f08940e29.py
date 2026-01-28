code = """import json

# Read the result from the first query
with open('var_functions.query_db:0', 'r') as f:
    nasdaq_capital_stocks = json.load(f)

# Extract symbols
symbols = [stock['Symbol'] for stock in nasdaq_capital_stocks]
print(f"Total NASDAQ Capital Market symbols: {len(symbols)}")
print(f"First 10 symbols: {symbols[:10]}")

# Read the list of tables from stocktrade_database
with open('var_functions.list_db:2', 'r') as f:
    all_tables = json.load(f)

# Find intersection
available_symbols = list(set(symbols) & set(all_tables))
print(f"Available symbols in stocktrade_database: {len(available_symbols)}")
print(f"First 10 available symbols: {available_symbols[:10]}")

# Store results for next step
result = {
    'nasdaq_capital_symbols': symbols,
    'available_symbols': available_symbols
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
