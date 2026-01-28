code = """import json

# Read the NYSE Arca symbols from the file
with open(var_functions.query_db:0, 'r') as f:
    arca_symbols_data = json.load(f)

# Read all available symbols in stocktrade_database
with open(var_functions.list_db:6, 'r') as f:
    all_trade_symbols = json.load(f)

# Extract just the symbol strings from arca_symbols_data
arca_symbols = [item['Symbol'] for item in arca_symbols_data]

# Find the intersection (symbols that are both NYSE Arca ETFs and have price data)
available_symbols = list(set(arca_symbols) & set(all_trade_symbols))

print('__RESULT__:')
print(json.dumps({
    'arca_etf_count': len(arca_symbols),
    'available_in_trade_db': len(available_symbols),
    'first_available': available_symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
