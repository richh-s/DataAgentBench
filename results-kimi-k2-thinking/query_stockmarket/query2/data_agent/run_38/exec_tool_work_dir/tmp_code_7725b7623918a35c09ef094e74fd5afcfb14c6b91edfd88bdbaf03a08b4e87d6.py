code = """import json

# Load the NYSE Arca ETF symbols
nyse_arca_file = locals()['var_functions.query_db:2']
with open(nyse_arca_file, 'r') as f:
    nyse_arca_etfs = json.load(f)

nyse_arca_symbols = set([etf['Symbol'] for etf in nyse_arca_etfs])

# Load all table names from stocktrade_database
all_tables_file = locals()['var_functions.list_db:5']
with open(all_tables_file, 'r') as f:
    all_tables = json.load(f)

# Find ETFs that have price data
avail_etf_symbols = nyse_arca_symbols.intersection(all_tables)

# Test a sample first - let's see the first 10 ETFs
sample_symbols = list(avail_etf_symbols)[:10]

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_symbols),
    'etfs_with_price_data': len(avail_etf_symbols),
    'sample_symbols': sample_symbols
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:10': {'nyse_arca_etfs_type': "<class 'str'>", 'nyse_arca_etfs_length': 38, 'nyse_arca_etfs_sample': 'fil', 'all_tables_type': "<class 'str'>", 'all_tables_length': 37, 'all_tables_sample': 'fil'}, 'var_functions.execute_python:12': {'total_nyse_arca_etfs': 1435, 'total_tables_in_db': 2753, 'etfs_with_price_data': 1435, 'sample_etfs': ['CGW', 'EZA', 'AIIQ', 'CORN', 'HDMV', 'MDY', 'VB', 'TIPX', 'EDIV', 'TLH']}}

exec(code, env_args)
