code = """import json

# Get the list of NYSE Arca ETFs
etf_file_path = 'file_storage/functions.query_db:8.json'
with open(etf_file_path, 'r') as f:
    etf_list = json.load(f)

# Get the list of all tables in stocktrade_database  
tables_file_path = 'file_storage/functions.query_db:20.json'
with open(tables_file_path, 'r') as f:
    tables_list = json.load(f)

# Extract symbols
etf_symbols = set([item['Symbol'] for item in etf_list])
table_symbols = set([item['symbol'] for item in tables_list])

# Find intersection (ETFs that have price data)
available_etf_symbols = sorted(list(etf_symbols.intersection(table_symbols)))

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(etf_symbols),
    'tables_in_trade_db': len(table_symbols),
    'available_for_query': len(available_etf_symbols),
    'sample_symbols': available_etf_symbols[:10]
}))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'file_path': 'file_storage/functions.query_db:8.json', 'type': "<class 'str'>"}, 'var_functions.execute_python:16': {'total_symbols': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
