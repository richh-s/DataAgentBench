code = """import json

# Get NYSE Arca ETF symbols from the first query
result_file_1 = var_functions.query_db:0
with open(result_file_1, 'r') as f:
    etf_list = json.load(f)

nyse_arca_etfs = [etf['Symbol'] for etf in etf_list]

# Get all available tables from stocktrade_database
result_file_2 = var_functions.list_db:6
with open(result_file_2, 'r') as f:
    all_tables = json.load(f)

# Find intersection (ETFs that have price data)
etfs_with_data = [symbol for symbol in nyse_arca_etfs if symbol in all_tables]

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_etfs),
    'etfs_with_price_data': len(etfs_with_data),
    'sample_etfs': etfs_with_data[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
