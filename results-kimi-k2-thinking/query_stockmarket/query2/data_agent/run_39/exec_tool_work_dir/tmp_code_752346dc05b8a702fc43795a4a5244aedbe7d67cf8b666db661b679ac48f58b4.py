code = """import json
import os

# Get ETF symbols from NYSE Arca (Listing Exchange = 'P')
etf_result = locals()['var_functions.query_db:0']

# Parse ETF symbols
if isinstance(etf_result, str) and os.path.exists(etf_result):
    with open(etf_result, 'r') as f:
        etf_data = json.load(f)
else:
    etf_data = etf_result

# Get all available tables from stocktrade database
tables_result = locals()['var_functions.list_db:12']

# Parse tables
if isinstance(tables_result, str) and os.path.exists(tables_result):
    with open(tables_result, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = tables_result

# Filter to only ETFs that have data tables
valid_etf_symbols = []
for item in etf_data:
    symbol = item['Symbol']
    if symbol in all_tables:
        valid_etf_symbols.append(symbol)

print('__RESULT__:')
print(json.dumps({
    'etfs_to_check': len(valid_etf_symbols),
    'first_50_symbols': valid_etf_symbols[:50]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.query_db:6': [], 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.query_db:10': [], 'var_functions.list_db:12': 'file_storage/functions.list_db:12.json', 'var_functions.execute_python:14': {'total_nyse_arca_etfs': 1435, 'available_in_stocktrade': 1435, 'available_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:16': {'total_etfs_to_check': 1435, 'test_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}, 'var_functions.query_db:20': [], 'var_functions.execute_python:22': {'total_nyse_arca_etfs': 1435, 'available_as_tables': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}}

exec(code, env_args)
