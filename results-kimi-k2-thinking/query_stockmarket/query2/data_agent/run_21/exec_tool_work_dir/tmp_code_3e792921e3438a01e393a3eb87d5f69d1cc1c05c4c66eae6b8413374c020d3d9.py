code = """import json

# Get NYSE Arca ETFs from previous query
result_key = 'var_functions.query_db:0'
etf_data = locals()[result_key]

# If it's a string (file path), read from file
if isinstance(etf_data, str):
    with open(etf_data, 'r') as f:
        nyse_arca_etfs = json.load(f)
else:
    nyse_arca_etfs = etf_data

# Extract symbols
nyse_arca_symbols = [item['Symbol'] for item in nyse_arca_etfs]

# Get all tickers from stocktrade database
result_key2 = 'var_functions.list_db:6'
all_tickers_data = locals()[result_key2]

if isinstance(all_tickers_data, str):
    with open(all_tickers_data, 'r') as f:
        all_tickers = json.load(f)
else:
    all_tickers = all_tickers_data

# Find intersection (ETFs that have data)
etfs_with_data = list(set(nyse_arca_symbols) & set(all_tickers))

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_symbols),
    'total_tickers_in_trade_db': len(all_tickers),
    'etfs_with_data': len(ets_with_data)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY'], 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': 'Found 2753 tickers total'}

exec(code, env_args)
