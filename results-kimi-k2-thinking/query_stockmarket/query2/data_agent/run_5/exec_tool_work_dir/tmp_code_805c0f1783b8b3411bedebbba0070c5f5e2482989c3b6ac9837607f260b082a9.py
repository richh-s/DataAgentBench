code = """import json
import os

# Get ticker lists from storage
nyse_arca_etfs_key = 'var_functions.query_db:0'
all_tickers_key = 'var_functions.list_db:9'

nyse_arca_etfs_file = locals().get(nyse_arca_etfs_key)
all_tickers_file = locals().get(all_tickers_key)

# Load NYSE Arca ETFs
nyse_arca_etfs = []
if isinstance(nyse_arca_etfs_file, str) and os.path.exists(nyse_arca_etfs_file):
    with open(nyse_arca_etfs_file, 'r') as f:
        nyse_arca_etfs = [item['Symbol'] for item in json.load(f)]
elif isinstance(nyse_arca_etfs_file, list):
    nyse_arca_etfs = [item['Symbol'] for item in nyse_arca_etfs_file]

# Load all tickers from stocktrade database
all_tickers = []
if isinstance(all_tickers_file, str) and os.path.exists(all_tickers_file):
    with open(all_tickers_file, 'r') as f:
        all_tickers = json.load(f)
elif isinstance(all_tickers_file, list):
    all_tickers = all_tickers_file

# Find intersection (ETFs on NYSE Arca that have price data)
etf_tickers_with_data = list(set(nyse_arca_etfs) & set(all_tickers))

result = {
    'nyse_arca_etfs_count': len(nyse_arca_etfs),
    'all_tickers_count': len(all_tickers),
    'etf_intersection_count': len(etf_tickers_with_data),
    'first_10_intersection': sorted(etf_tickers_with_data)[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'tickers_count': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.list_db:9': 'file_storage/functions.list_db:9.json'}

exec(code, env_args)
