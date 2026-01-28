code = """import json

# Access the stored query result
symbols_data = locals()['var_functions.query_db:2']
print(f'Got symbols data of type: {type(symbols_data)}')

# Parse the data - it's stored as a list of dicts
if isinstance(symbols_data, list):
    symbols = symbols_data
else:
    symbols = []

print(f'Total NYSE non-ETF symbols: {len(symbols)}')

# Show first few symbols to verify
for i, sym in enumerate(symbols[:10]):
    print(f"  {i+1}. {sym['Symbol']}: {sym['Company Description'][:50]}...")

# Extract just the symbol list for the next step
symbol_list = [s['Symbol'] for s in symbols]
print(f'Extracted {len(symbol_list)} symbols')

# Store result for next step
result = {'symbols': symbol_list, 'metadata': symbols}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
