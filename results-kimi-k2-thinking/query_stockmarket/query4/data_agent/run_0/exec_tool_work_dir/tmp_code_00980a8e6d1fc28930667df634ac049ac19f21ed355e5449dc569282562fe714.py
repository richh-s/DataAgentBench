code = """import json
import os

# Load the NYSE non-ETF symbols from the SQLite query
result_file = var_functions.query_db:0

if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        nyse_stocks = json.load(f)
else:
    nyse_stocks = var_functions.query_db:0

# Extract symbols
symbols = [stock['Symbol'] for stock in nyse_stocks]
print(f"Found {len(symbols)} NYSE non-ETF symbols")

# Print first few symbols
print(f"First 10 symbols: {symbols[:10]}")

# Check which symbols exist as tables in stocktrade_database
# For DuckDB, we can use the tables_list result
stocktrade_tables = var_functions.list_db:2

if isinstance(stocktrade_tables, str) and stocktrade_tables.endswith('.json'):
    with open(stocktrade_tables, 'r') as f:
        trade_symbols = json.load(f)
else:
    trade_symbols = var_functions.list_db:2

# Convert to set for faster lookup
trade_symbols_set = set(trade_symbols)

# Find intersection
common_symbols = [symbol for symbol in symbols if symbol in trade_symbols_set]
print(f"Found {len(common_symbols)} symbols with trading data")
print(f"First 10 common symbols: {common_symbols[:10]}")

# Now analyze 2017 data for each common symbol to find those with more up days than down days
print("Analyzing 2017 trading data...")

# We need to query DuckDB for each symbol
# But we can't query all at once - we'll need to do this in batches or iteratively
# For now, let's store the common symbols and their analysis results will be done

# Return the list of common symbols for further processing
result = {
    'nyse_symbols_count': len(symbols),
    'common_symbols_count': len(common_symbols),
    'common_symbols': common_symbols
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
