code = """import json

# Get the list of all tables in stocktrade_database
all_tables_path = locals()['var_functions.list_db:11']
if isinstance(all_tables_path, str):
    with open(all_tables_path, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = all_tables_path

# Get the list of NYSE Arca ETF symbols
etf_symbols_path = locals()['var_functions.query_db:0']
if isinstance(etf_symbols_path, str):
    with open(etf_symbols_path, 'r') as f:
        etf_symbols_data = json.load(f)
else:
    etf_symbols_data = etf_symbols_path

nyse_arca_etfs = [item['Symbol'] for item in etf_symbols_data]

# Find intersection (ETFs that exist as tables in stocktrade_database)
existing_etf_tables = list(set(nyse_arca_etfs) & set(all_tables))

print('__RESULT__:')
print(json.dumps({
    'nyse_arca_etf_count': len(nyse_arca_etfs),
    'existing_table_count': len(existing_etf_tables),
    'existing_tables': existing_etf_tables
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.list_db:11': 'file_storage/functions.list_db:11.json'}

exec(code, env_args)
