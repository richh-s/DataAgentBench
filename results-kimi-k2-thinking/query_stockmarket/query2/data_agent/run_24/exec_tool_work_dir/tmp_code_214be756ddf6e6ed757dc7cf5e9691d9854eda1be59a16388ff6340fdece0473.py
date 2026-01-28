code = """import json

# Read the list of all tables from stocktrade database
if isinstance(var_functions.list_db_14, str) and '.json' in var_functions.list_db_14:
    with open(var_functions.list_db_14, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = var_functions.list_db_14

print('__RESULT__:')
print(json.dumps({'total_tables': len(all_tables), 'sample_tables': all_tables[:10]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:14': 'file_storage/functions.list_db:14.json'}

exec(code, env_args)
