code = """import json

# Access the NYSE non-ETF stocks from the previous query
nyse_stocks = locals()['var_functions.query_db:0']

# Extract symbols from NYSE stocks
nyse_symbols = {stock['Symbol'] for stock in nyse_stocks}

# Access the available tables from stocktrade_database
available_tables = locals()['var_functions.list_db:2']

# Find intersection - stocks that are both NYSE non-ETF and have data available
common_stocks = nyse_symbols.intersection(available_tables)

print('__RESULT__:')
print(json.dumps({
    'total_nyse_stocks': len(nyse_stocks),
    'total_available_tables': len(available_tables),
    'common_stocks_count': len(common_stocks),
    'sample_common_stocks': list(common_stocks)[:10],
    'nyse_symbols_sample': list(nyse_symbols)[:10],
    'available_tables_sample': available_tables[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
