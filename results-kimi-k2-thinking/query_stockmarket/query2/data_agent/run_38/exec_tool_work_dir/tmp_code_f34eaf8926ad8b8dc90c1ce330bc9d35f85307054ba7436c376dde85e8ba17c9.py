code = """import json

# Read the list of NYSE Arca ETFs from the previous query
with open('var_functions.query_db:2.json', 'r') as f:
    nyse_arca_etfs = json.load(f)

# Extract just the symbols
nyse_arca_symbols = set([etf['Symbol'] for etf in nyse_arca_etfs])

# Read the list of available tables from stocktrade_database
with open('var_functions.list_db:5.json', 'r') as f:
    all_tables = json.load(f)

# Find intersection (ETFs that have price data)
etfs_with_data = nyse_arca_symbols.intersection(all_tables)

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_symbols),
    'total_tables_in_db': len(all_tables),
    'etfs_with_price_data': len(etfs_with_data)
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)
