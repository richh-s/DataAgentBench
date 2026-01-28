code = """import json

# Load the actual data from the stored file paths
with open('file_storage/functions.query_db:0.json', 'r') as f:
    nasdaq_cap_symbols = json.load(f)

with open('file_storage/functions.list_db:2.json', 'r') as f:
    available_tables = json.load(f)

# Create a set of available symbols for quick lookup
available_symbols = set(available_tables)

# Filter to only include symbols that have data tables
valid_symbols = []
for item in nasdaq_cap_symbols:
    symbol = item['Symbol']
    if symbol in available_symbols:
        valid_symbols.append({
            'symbol': symbol,
            'description': item['Company Description']
        })

print('__RESULT__:')
print(json.dumps({
    'total_nasdaq_cap_symbols': len(nasdaq_cap_symbols),
    'symbols_with_data': len(valid_symbols),
    'sample_symbols': valid_symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:10': {'nasdaq_cap_type': "<class 'str'>", 'nasdaq_cap_len': 38, 'nasdaq_cap_sample': 'file_storage/functions.query_db:0.json', 'available_tables_type': "<class 'str'>", 'available_tables_len': 37, 'available_tables_sample': 'file_storage/functions.list_db:2.json'}}

exec(code, env_args)
