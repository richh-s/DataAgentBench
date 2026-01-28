code = """import json

# Get the file path for the list of tables
tables_file_path = locals()['var_functions.list_db:8']
print(f"Tables file path: {tables_file_path}")

# Read the tables list
with open(tables_file_path, 'r') as f:
    all_tables = json.load(f)

# Get the NASDAQ Capital Market symbols from previous result
nasdaq_cap_path = locals()['var_functions.execute_python:7']
print(f"Nasdaq cap file path: {nasdaq_cap_path}")

with open(nasdaq_cap_path, 'r') as f:
    nasdaq_data = json.load(f)

nasdaq_symbols = nasdaq_data['symbols']
symbol_to_desc = nasdaq_data['symbol_to_desc']

print(f"Total NASDAQ Capital Market symbols: {len(nasdaq_symbols)}")
print(f"Total tables in stocktrade_database: {len(all_tables)}")

# Find intersection
available_symbols = list(set(nasdaq_symbols) & set(all_tables))
print(f"Available NASDAQ Capital Market tables: {len(available_symbols)}")
print(f"Sample available symbols: {available_symbols[:10]}")

# Store for later use
result = {
    "available_symbols": available_symbols,
    "symbol_to_desc": symbol_to_desc,
    "count": len(available_symbols)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:7': 'file_storage/functions.execute_python:7.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json'}

exec(code, env_args)
