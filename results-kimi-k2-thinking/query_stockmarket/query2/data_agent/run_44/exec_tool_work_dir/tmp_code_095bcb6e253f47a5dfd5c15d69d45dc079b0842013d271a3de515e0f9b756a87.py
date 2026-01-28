code = """import json

# Read the list of all tables from stocktrade_database
all_tables_data = locals()['var_functions.list_db:6']

# If it's a file path, read from file
if isinstance(all_tables_data, str):
    with open(all_tables_data, 'r') as f:
        all_tables_data = json.load(f)

# Get ETF symbols from previous query
etf_data = locals()['var_functions.query_db:0']
if isinstance(etf_data, str):
    with open(etf_data, 'r') as f:
        etf_data = json.load(f)

etf_symbols = [etf['Symbol'] for etf in etf_data]

# Check which ETFs exist in the stocktrade_database
existing_etfs = [symbol for symbol in etf_symbols if symbol in all_tables_data]

non_existing_etfs = [symbol for symbol in etf_symbols if symbol not in all_tables_data]

print('__RESULT__:')
print(json.dumps({
    "total_nyse_arca_etfs": len(etf_symbols),
    "existing_in_trade_db": len(existing_etfs),
    "missing_from_trade_db": len(non_existing_etfs),
    "first_few_existing": existing_etfs[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.execute_python:5': {'total_nyse_arca_etfs': 1435}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
