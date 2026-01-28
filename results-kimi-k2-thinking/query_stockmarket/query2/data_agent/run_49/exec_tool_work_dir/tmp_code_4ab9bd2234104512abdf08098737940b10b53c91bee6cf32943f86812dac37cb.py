code = """import pandas as pd, json, os

# Load NYSE Arca ETFs
etf_file = locals()['var_functions.query_db:0']
if isinstance(etf_file, str) and os.path.exists(etf_file):
    with open(etf_file, 'r') as f:
        nyse_arca_etfs = json.load(f)
else:
    nyse_arca_etfs = etf_file

# Load all available tables from stocktrade_database
tables_file = locals()['var_functions.list_db:6']
if isinstance(tables_file, str) and os.path.exists(tables_file):
    with open(tables_file, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = tables_file

# Extract symbols
nyse_arca_symbols = set([item['Symbol'] for item in nyse_arca_etfs])
available_symbols = set(all_tables)

# Find intersection
common_symbols = nyse_arca_symbols.intersection(available_symbols)

print('__RESULT__:')
print(json.dumps({
    'nyse_arca_etf_count': len(nyse_arca_symbols),
    'available_tables_count': len(available_symbols),
    'common_symbols_count': len(common_symbols),
    'common_symbols_sample': list(common_symbols)[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'count': 1435, 'head': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}, {'Symbol': 'AFK'}, {'Symbol': 'AFLG'}, {'Symbol': 'AFMC'}, {'Symbol': 'AFSM'}, {'Symbol': 'AFTY'}]}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
