code = """import json
import sqlite3
import duckdb

# Storage keys
stockinfo_key = 'var_functions.query_db:2'
stocktables_key = 'var_functions.list_db:5'

# Read the stockinfo query result (symbols on NYSE ARCA ETFs)
with open(stockinfo_key, 'r') as f:
    nyse_arca_etfs = json.load(f)

# Read the stocktrade tables list
with open(stocktables_key, 'r') as f:
    stocktrade_tables = json.load(f)

# Convert to sets for easier comparison
nyse_arca_etfs_set = set([item['Symbol'] for item in nyse_arca_etfs])
stocktrade_tables_set = set(stocktrade_tables)

# Find intersection
common_symbols = nyse_arca_etfs_set.intersection(stocktrade_tables_set)

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_etfs_set),
    'total_stocktrade_tables': len(stocktrade_tables_set),
    'common_symbols': len(common_symbols)
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)
