code = """# Get list of all tables in stocktrade_database
import json
tables_var = locals()['var_functions.list_db:2']
if isinstance(tables_var, str):
    with open(tables_var, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = tables_var

print('__RESULT__:')
print(json.dumps(f"Found {len(all_tables)} total tables in stocktrade_database"))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:9': 'Found 86 NASDAQ Capital Market tickers'}

exec(code, env_args)
