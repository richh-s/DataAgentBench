code = """import json

# Get the list of all tables in stocktrade database
all_tables_file = locals()['var_functions.list_db:6']

with open(all_tables_file, 'r') as f:
    all_tables = json.load(f)

# Get the NYSE Arca ETF symbols from previous result
nyse_arca_file = locals()['var_functions.execute_python:8']
with open(nyse_arca_file, 'r') as f:
    nyse_arca_symbols = json.load(f)

# Find which NYSE Arca ETFs actually exist in stocktrade database
existing_symbols = [symbol for symbol in nyse_arca_symbols if symbol in all_tables]

print('__RESULT__:')
print(json.dumps({
    'nyse_arca_etf_count': len(nyse_arca_symbols),
    'existing_in_stocktrade_count': len(existing_symbols),
    'sample_existing': existing_symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'total_etfs': 1435, 'first_few_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
