code = """import json
import os

# Get the ETF symbols from NYSE Arca
etf_file = locals()['var_functions.query_db:0']
with open(etf_file, 'r') as f:
    etf_symbols_data = json.load(f)

etf_symbols = [etf['Symbol'] for etf in etf_symbols_data]

# Get the list of tables from stocktrade_database
tables_file = locals()['var_functions.list_db:10']
with open(tables_file, 'r') as f:
    all_tables = json.load(f)

# Find intersection
common_symbols = list(set(etf_symbols) & set(all_tables))

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(etf_symbols),
    'total_tables_in_db': len(all_tables),
    'common_symbols': len(common_symbols)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': {'type': "<class 'str'>", 'length': 38}, 'var_functions.execute_python:8': {'symbol_count': 1435, 'first_few': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json'}

exec(code, env_args)
