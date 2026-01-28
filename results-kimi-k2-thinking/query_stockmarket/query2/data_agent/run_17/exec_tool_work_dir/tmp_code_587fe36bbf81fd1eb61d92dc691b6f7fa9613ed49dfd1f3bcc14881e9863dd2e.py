code = """import json

# Read the ETF symbols from the first query
with open(locals()['var_functions.query_db:0'], 'r') as f:
    etf_data = json.load(f)

# Read all tables from the stocktrade_database
with open(locals()['var_functions.list_db:8'], 'r') as f:
    all_tables = json.load(f)

# Extract symbols
etf_symbols = set(s['Symbol'] for s in etf_data)
available_tables = set(all_tables)

# Find intersection (symbols that exist in both)
valid_symbols = list(etf_symbols.intersection(available_tables))
valid_symbols.sort()

print('__RESULT__:')
print(json.dumps({
    'total_etf_symbols': len(etf_symbols),
    'total_available_tables': len(available_tables),
    'valid_symbols_count': len(valid_symbols),
    'valid_symbols': valid_symbols
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:7': 'file_storage/functions.execute_python:7.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json'}

exec(code, env_args)
