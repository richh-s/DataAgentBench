code = """import json
import os

# Get the NYSE Arca ETFs from the file
etf_file = locals().get('var_functions.query_db:0')
with open(etf_file, 'r') as f:
    nyse_arca_etfs = json.load(f)

# Get all table names from stocktrade database
tables_file = locals().get('var_functions.list_db:5')
with open(tables_file, 'r') as f:
    all_tables = json.load(f)

# Extract just the symbols from the ETF list
etf_symbols = [etf['Symbol'] for etf in nyse_arca_etfs]

# Find intersection (ETFs that have price data tables)
valid_etf_symbols = [symbol for symbol in etf_symbols if symbol in all_tables]

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(etf_symbols),
    'etfs_with_price_data': len(valid_etf_symbols),
    'sample_etfs': valid_etf_symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'count': 1435, 'sample': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}, {'Symbol': 'AFK'}, {'Symbol': 'AFLG'}, {'Symbol': 'AFMC'}, {'Symbol': 'AFSM'}, {'Symbol': 'AFTY'}]}, 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)
