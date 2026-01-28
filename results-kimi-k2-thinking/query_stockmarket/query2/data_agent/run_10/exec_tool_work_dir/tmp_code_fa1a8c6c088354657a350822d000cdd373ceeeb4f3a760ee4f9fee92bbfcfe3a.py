code = """import json

# Get the list of NYSE Arca ETFs
nyse_arca_file = locals()['var_functions.query_db:2']
with open(nyse_arca_file, 'r') as f:
    nyse_arca_data = json.load(f)
nyse_arca_etfs = [etf['Symbol'] for etf in nyse_arca_data]

# Get all available tables in stocktrade database
stocktrade_tables_file = locals()['var_functions.list_db:8']
with open(stocktrade_tables_file, 'r') as f:
    all_tables = json.load(f)

# Find which NYSE Arca ETFs have data available
available_etfs = [etf for etf in nyse_arca_etfs if etf in all_tables]

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_etfs),
    'etfs_with_data': len(available_etfs)
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': {'total_nyse_arca_etfs': 1435, 'total_stocktrade_tables': 2753, 'etfs_with_price_data': 1435, 'sample_etfs': ['GSY', 'EMLP', 'MMIN', 'SCHI', 'IAT', 'IJS', 'SIJ', 'RWM', 'ULE', 'DBEF']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
