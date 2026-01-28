code = """import json

# Read the NYSE Arca ETFs list
nyse_arca_file = locals()['var_functions.query_db:2']
with open(nyse_arca_file, 'r') as f:
    nyse_arca_data = json.load(f)
nyse_arca_etfs = [etf['Symbol'] for etf in nyse_arca_data]

# Read the stocktrade database tables list
stocktrade_tables_file = locals()['var_functions.list_db:8']
with open(stocktrade_tables_file, 'r') as f:
    all_tables = json.load(f)

# Find intersection (ETFs that have price data)
etfs_with_data = list(set(nyse_arca_etfs) & set(all_tables))

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_etfs),
    'total_stocktrade_tables': len(all_tables),
    'etfs_with_price_data': len(etfs_with_data),
    'sample_etfs': etfs_with_data[:10]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json'}

exec(code, env_args)
