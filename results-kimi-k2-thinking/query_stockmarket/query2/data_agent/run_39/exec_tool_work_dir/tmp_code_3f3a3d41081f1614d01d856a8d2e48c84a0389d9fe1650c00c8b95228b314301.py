code = """import json
import os

# Get the ETF symbols from the first query
etf_symbols_result = locals()['var_functions.query_db:0']

# Parse the result
if isinstance(etf_symbols_result, str) and os.path.exists(etf_symbols_result):
    with open(etf_symbols_result, 'r') as f:
        etf_symbols_data = json.load(f)
else:
    etf_symbols_data = etf_symbols_result

# Extract symbols into a list
etf_symbols = [item['Symbol'] for item in etf_symbols_data]

# Also get all available tables from the stocktrade database
all_tables_result = locals()['var_functions.list_db:12']

# Parse the all_tables result
if isinstance(all_tables_result, str) and os.path.exists(all_tables_result):
    with open(all_tables_result, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = all_tables_result

# Filter to only include ETFS that exist as tables in stocktrade database
available_etf_symbols = [symbol for symbol in etf_symbols if symbol in all_tables]

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(etf_symbols),
    'available_in_stocktrade': len(available_etf_symbols),
    'available_symbols': available_etf_symbols[:20]  # Preview first 20
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.query_db:6': [], 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.query_db:10': [], 'var_functions.list_db:12': 'file_storage/functions.list_db:12.json'}

exec(code, env_args)
