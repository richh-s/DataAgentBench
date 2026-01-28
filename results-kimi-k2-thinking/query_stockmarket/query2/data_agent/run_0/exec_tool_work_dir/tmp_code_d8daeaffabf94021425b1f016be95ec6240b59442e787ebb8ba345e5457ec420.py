code = """import json

# Read available tickers in stocktrade_database
tables_file = locals()['var_functions.list_db:20']
with open(tables_file, 'r') as f:
    available_tickers = json.load(f)

# Get NYSE Arca ETF symbols
nyse_file = locals()['var_functions.query_db:0']
with open(nyse_file, 'r') as f:
    nyse_etfs = json.load(f)

nyse_symbols = set(etf['Symbol'] for etf in nyse_etfs)
available_set = set(available_tickers)

# Find intersection
common_etfs = nyse_symbols & available_set

print('__RESULT__:')
print(json.dumps({
    'available_tickers_count': len(available_tickers),
    'nyse_arca_etfs_count': len(nyse_symbols),
    'common_with_data': len(common_etfs)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': 1435, 'var_functions.query_db:10': [], 'var_functions.query_db:12': [{'max_price': '193.3121490478516', 'record_count': '252'}], 'var_functions.query_db:14': [{'max_price': '125.2300033569336', 'record_count': '252'}], 'var_functions.query_db:16': [{'max_price': '24.036970138549805'}], 'var_functions.execute_python:18': 1435, 'var_functions.list_db:20': 'file_storage/functions.list_db:20.json', 'var_functions.execute_python:24': {'count': 1435, 'symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.query_db:26': [{'max_price': '24.036970138549805'}]}

exec(code, env_args)
