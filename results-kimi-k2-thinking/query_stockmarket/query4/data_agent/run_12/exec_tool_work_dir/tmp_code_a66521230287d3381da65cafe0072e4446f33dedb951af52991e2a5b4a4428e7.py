code = """import json
import sqlite3
import os

# Load the stockinfo results
stockinfo_path = var_functions.query_db:0
if isinstance(stockinfo_path, str) and stockinfo_path.endswith('.json'):
    with open(stockinfo_path, 'r') as f:
        stockinfo_data = json.load(f)
else:
    stockinfo_data = var_functions.query_db:0

# Also load the list of tables from stocktrade_database
tables_path = var_functions.query_db:4
if isinstance(tables_path, str) and tables_path.endswith('.json'):
    with open(tables_path, 'r') as f:
        tables_data = json.load(f)
else:
    tables_data = var_functions.query_db:4

# Extract symbols from both datasets
stockinfo_symbols = {item['Symbol'] for item in stockinfo_data}
trade_tables = {item['table_name'] for item in tables_data}

# Find intersection - symbols that exist in both databases
common_symbols = stockinfo_symbols.intersection(trade_tables)

print('__RESULT__:')
print(json.dumps({
    'total_stockinfo_symbols': len(stockinfo_symbols),
    'total_trade_tables': len(trade_tables),
    'common_symbols_count': len(common_symbols),
    'sample_common_symbols': list(common_symbols)[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
