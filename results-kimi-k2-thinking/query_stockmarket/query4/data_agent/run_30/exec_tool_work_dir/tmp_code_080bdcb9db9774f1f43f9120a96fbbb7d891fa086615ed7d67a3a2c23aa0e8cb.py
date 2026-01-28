code = """import json, os

# Load the valid NYSE non-ETF tickers from files
all_tickers_path = globals()['var_functions.list_db:0']
nyse_records_path = globals()['var_functions.query_db:2']

with open(all_tickers_path, "r") as f:
    all_tickers = json.load(f)

with open(nyse_records_path, "r") as f:
    nyse_records = json.load(f)

nyse_tickers = {rec['Symbol'] for rec in nyse_records}
valid_tickers = [t for t in all_tickers if t in nyse_tickers]

print('__RESULT__:')
print(json.dumps(valid_tickers[:10]))  # Just print first 10 to verify"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': 'file_storage/functions.list_db:0.json', 'var_functions.execute_python:14': {'all_tickers_count': 2753, 'nyse_tickers_count': 234, 'valid_tickers_count': 234}}

exec(code, env_args)
