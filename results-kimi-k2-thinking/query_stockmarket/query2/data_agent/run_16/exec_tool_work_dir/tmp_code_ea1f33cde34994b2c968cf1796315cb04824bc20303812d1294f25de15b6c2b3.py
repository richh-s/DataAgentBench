code = """import json

# Read files
with open(locals()['var_functions.query_db:0'], 'r') as f:
    nyse_arca_etfs_data = json.load(f)

with open(locals()['var_functions.list_db:5'], 'r') as f:
    trade_tables = json.load(f)

# Get NYSE Arca ETF symbols
nyse_arca_symbols = set([item['Symbol'] for item in nyse_arca_etfs_data])

# Get available tables as a set
trade_symbols = set(trade_tables)

# Find intersection - ETFs that are available for trade data
available_etfs = nyse_arca_symbols.intersection(trade_symbols)

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_symbols),
    'available_trade_tables': len(trade_symbols),
    'intersection_size': len(available_etfs),
    'sample_symbols': list(available_etfs)[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)
