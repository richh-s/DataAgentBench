code = """import json
import os

# Load ETF symbols from NYSE Arca
etf_symbols_result = locals()['var_functions.query_db:0']

# Parse the result
if isinstance(etf_symbols_result, str) and os.path.exists(etf_symbols_result):
    with open(etf_symbols_result, 'r') as f:
        etf_symbols_data = json.load(f)
else:
    etf_symbols_data = etf_symbols_result

# Extract symbols
symbols_to_check = [item['Symbol'] for item in etf_symbols_data]

# Load available tables from stocktrade database
all_tables_result = locals()['var_functions.list_db:12']

# Parse the result
if isinstance(all_tables_result, str) and os.path.exists(all_tables_result):
    with open(all_tables_result, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = all_tables_result

# Filter symbols to only include those that exist as tables
valid_symbols = [symbol for symbol in symbols_to_check if symbol in all_tables]

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(symbols_to_check),
    'available_as_tables': len(valid_symbols),
    'sample_symbols': valid_symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.query_db:6': [], 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.query_db:10': [], 'var_functions.list_db:12': 'file_storage/functions.list_db:12.json', 'var_functions.execute_python:14': {'total_nyse_arca_etfs': 1435, 'available_in_stocktrade': 1435, 'available_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:16': {'total_etfs_to_check': 1435, 'test_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}, 'var_functions.query_db:20': []}

exec(code, env_args)
