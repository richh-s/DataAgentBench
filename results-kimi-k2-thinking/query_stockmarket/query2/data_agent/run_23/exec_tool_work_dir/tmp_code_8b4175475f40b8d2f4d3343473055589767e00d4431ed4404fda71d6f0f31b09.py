code = """import json

# Read ETF symbols from NYSE Arca
etf_file_path = locals()['var_functions.query_db:2']
with open(etf_file_path, 'r') as f:
    etf_list = json.load(f)

# Read all symbols from stocktrade database (table names)
tables_file_path = locals()['var_functions.list_db:8']
with open(tables_file_path, 'r') as f:
    all_tables = json.load(f)

nyse_arka_etf_symbols = set([item['Symbol'] for item in etf_list])
all_table_symbols = set(all_tables)

# Find intersection (ETFs that have price data tables)
common_symbols = nyse_arka_etf_symbols.intersection(all_table_symbols)

print(f"Total ETFs listed: {len(nyse_arka_etf_symbols)}")
print(f"Total tables available: {len(all_table_symbols)}")
print(f"Common symbols (ETFs with price data): {len(common_symbols)}")
print('__RESULT__:')
print(json.dumps(list(common_symbols)))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': 'file_storage/functions.execute_python:9.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json'}

exec(code, env_args)
