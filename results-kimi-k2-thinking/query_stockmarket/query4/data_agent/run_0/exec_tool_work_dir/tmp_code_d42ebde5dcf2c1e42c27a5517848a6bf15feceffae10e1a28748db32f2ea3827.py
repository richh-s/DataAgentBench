code = """import json

# Get NYSE non-ETF symbols from SQLite query
nyse_result = locals().get('var_functions.query_db:0')
if isinstance(nyse_result, str) and nyse_result.endswith('.json'):
    with open(nyse_result, 'r') as f:
        nyse_stocks = json.load(f)
else:
    nyse_stocks = nyse_result

# Extract symbols
symbols = [stock['Symbol'] for stock in nyse_stocks]
print(f"Found {len(symbols)} NYSE non-ETF symbols")
print(f"First 10 symbols: {symbols[:10]}")

# Get available trade tables from DuckDB
trade_tables = locals().get('var_functions.list_db:2')
if isinstance(trade_tables, str) and trade_tables.endswith('.json'):
    with open(trade_tables, 'r') as f:
        trade_symbols = json.load(f)
else:
    trade_symbols = trade_tables

# Convert to set for faster lookup
trade_symbols_set = set(trade_symbols)

# Find common symbols (in both NYSE list and have trade data)
common_symbols = [symbol for symbol in symbols if symbol in trade_symbols_set]
print(f"Found {len(common_symbols)} symbols with trading data")
print(f"First 10 common symbols: {common_symbols[:10]}")

# Return the result
result = {
    'nyse_symbols_count': len(symbols),
    'common_symbols_count': len(common_symbols),
    'common_symbols_preview': common_symbols[:20]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
