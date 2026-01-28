code = """import json, os

# Read the all_tickers file
all_tickers_path = globals()['var_functions.list_db:0']
with open(all_tickers_path, "r") as f:
    all_tickers = json.load(f)

# Read the nyse_records file
nyse_records_path = globals()['var_functions.query_db:2']
with open(nyse_records_path, "r") as f:
    nyse_records = json.load(f)

nyse_tickers = {rec['Symbol'] for rec in nyse_records}

# Intersection (tickers that exist in stocktrade_database and are NYSE non-ETF)
valid_tickers = [t for t in all_tickers if t in nyse_tickers]

print('__RESULT__:')
print(json.dumps({'all_tickers_count': len(all_tickers), 'nyse_tickers_count': len(nyse_tickers), 'valid_tickers_count': len(valid_tickers)}))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': 'file_storage/functions.list_db:0.json'}

exec(code, env_args)
