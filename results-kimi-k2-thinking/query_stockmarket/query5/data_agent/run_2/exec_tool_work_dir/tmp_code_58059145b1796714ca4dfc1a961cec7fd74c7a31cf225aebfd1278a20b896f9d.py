code = """import json

# Read the symbols data from storage
symbols_result = locals()['var_functions.query_db:0']

# If it's a file path, read it
if isinstance(symbols_result, str):
    with open(symbols_result, 'r') as f:
        symbols_data = json.load(f)
else:
    symbols_data = symbols_result

# Extract all symbols from NASDAQ Capital Market
nasdaq_cap_symbols = [item['Symbol'] for item in symbols_data]

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(nasdaq_cap_symbols),
    'sample_symbols': nasdaq_cap_symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
