code = """import json
# load storage variables created by previous query_db and list_db calls
with open(var_call_dXlfw7PBbNWvRB8DrF5zCYoo, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_7bDFcW723n8AK6WYWmUMLAlr, 'r') as f:
    stocktrade_tables = json.load(f)
# extract symbols from stockinfo result
symbols = [row['Symbol'] for row in stockinfo]
# intersection with available tables in stocktrade_database
available = set(stocktrade_tables)
query_symbols = [s for s in symbols if s in available]
# build mapping symbol -> company description
sym2desc = {row['Symbol']: row['Company Description'] for row in stockinfo if row['Symbol'] in query_symbols}
# output the list and mapping as JSON
out = {'symbols': query_symbols, 'sym2desc': sym2desc}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_dXlfw7PBbNWvRB8DrF5zCYoo': 'file_storage/call_dXlfw7PBbNWvRB8DrF5zCYoo.json', 'var_call_7bDFcW723n8AK6WYWmUMLAlr': 'file_storage/call_7bDFcW723n8AK6WYWmUMLAlr.json'}

exec(code, env_args)
