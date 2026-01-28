code = """import json, os
# Load the full result from the file stored in var_functions.query_db:0
file_path = var_functions.query_db:0
with open(file_path, 'r') as f:
    symbols_data = json.load(f)
# Also load the list of tables from stocktrade_database
file_path2 = var_functions.list_db:2
with open(file_path2, 'r') as f2:
    trade_tables = json.load(f2)
# Extract symbols from symbols_data
symbols = [rec['Symbol'] for rec in symbols_data]
# Intersection with trade_tables
common_symbols = [s for s in symbols if s in trade_tables]
print('__RESULT__:')
print(json.dumps({'total_symbols': len(symbols), 'common_symbols_count': len(common_symbols), 'first_few_common': common_symbols[:10]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
