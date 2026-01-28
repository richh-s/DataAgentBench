code = """import json

# Load stockinfo query result (list of dicts)
with open(var_functions.query_db:0, 'r') as f:
    stockinfo_data = json.load(f)
symbols = [rec['Symbol'] for rec in stockinfo_data]

# Load table list from stocktrade_database
with open(var_functions.list_db:2, 'r') as f:
    tables = json.load(f)

# Intersection
common = [s for s in symbols if s in tables]
print('__RESULT__:')
print(json.dumps({'symbol_count': len(symbols), 'table_count': len(tables), 'common_count': len(common)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
