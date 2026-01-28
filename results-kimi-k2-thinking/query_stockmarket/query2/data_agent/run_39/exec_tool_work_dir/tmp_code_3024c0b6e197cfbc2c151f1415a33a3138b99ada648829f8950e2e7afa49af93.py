code = """import json
import os

# Get all ETF symbols that are available in stocktrade database
etf_symbols_result = locals()['var_functions.query_db:0']
all_tables_result = locals()['var_functions.list_db:12']

# Parse ETF symbols
if isinstance(etf_symbols_result, str) and os.path.exists(etf_symbols_result):
    with open(etf_symbols_result, 'r') as f:
        etf_symbols_data = json.load(f)
else:
    etf_symbols_data = etf_symbols_result

# Parse all tables
if isinstance(all_tables_result, str) and os.path.exists(all_tables_result):
    with open(all_tables_result, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = all_tables_result

# Create list of ETF symbols to check
symbols_to_check = []
for item in etf_symbols_data:
    symbol = item['Symbol']
    if symbol in all_tables:
        symbols_to_check.append(symbol)

# For testing, let's start with a small batch first
batch_size = 50
test_symbols = symbols_to_check[:batch_size]

print('__RESULT__:')
print(json.dumps({
    'total_etfs_to_check': len(symbols_to_check),
    'test_batch': test_symbols
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.query_db:6': [], 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.query_db:10': [], 'var_functions.list_db:12': 'file_storage/functions.list_db:12.json', 'var_functions.execute_python:14': {'total_nyse_arca_etfs': 1435, 'available_in_stocktrade': 1435, 'available_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}}

exec(code, env_args)
