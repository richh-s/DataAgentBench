code = """import json

# Read ETF list and table names
with open('file_storage/functions.query_db:0.json', 'r') as f:
    nyse_arca_etfs = json.load(f)
    
with open('file_storage/functions.query_db:26.json', 'r') as f:
    all_tables = json.load(f)

# Get sets for fast lookup
nyse_arca_symbols = {etf['Symbol'] for etf in nyse_arca_etfs}
all_table_names = {table['name'] for table in all_tables}

# Find intersection - these are ETFs we can check
valid_etfs = nyse_arca_symbols.intersection(all_table_names)

print('__RESULT__:')
print(json.dumps({
    'nyse_arca_etfs': len(nyse_arca_symbols),
    'total_tables': len(all_table_names),
    'valid_etfs_to_check': len(valid_etfs),
    'sample_valid_etfs': list(sorted(valid_etfs))[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:12': {'total_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:16': {'total_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:34': [{'max_price': '163.6190185546875'}], 'var_functions.execute_python:36': {'total_nyse_arca_etfs': 1435, 'total_tables': 2753, 'common_etfs_to_check': 1435, 'checking_symbols': ['SPY', 'DIA', 'IVV', 'VOO', 'SSO', 'QLD', 'IVV', 'URE', 'RWL', 'USDU', 'UUP', 'FXE']}, 'var_functions.query_db:38': [{'max_price': '193.3121490478516'}]}

exec(code, env_args)
