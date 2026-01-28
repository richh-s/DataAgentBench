code = """import json

# Read ETF symbols
etf_file = globals().get('var_functions.query_db:2', None)
if isinstance(etf_file, str):
    with open(etf_file, 'r') as f:
        etf_data = json.load(f)
else:
    etf_data = etf_file if isinstance(etf_file, list) else []
etf_symbols = set([item['Symbol'] for item in etf_data])

# Read tables from stocktrade_database
tables_file = globals().get('var_functions.list_db:10', None)
if isinstance(tables_file, str):
    with open(tables_file, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = tables_file if isinstance(tables_file, list) else []

# Find intersection (tables that are both in stocktrade and are NYSE Arca ETFs)
etf_tables = etf_symbols.intersection(set(all_tables))
print('__RESULT__:')
print(json.dumps({
    'total_etfs': len(etf_symbols),
    'total_tables': len(all_tables),
    'intersection': len(etf_tables),
    'sample_tables': list(etf_tables)[:20]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'count': 1435, 'symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.execute_python:12': {'count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}}

exec(code, env_args)
