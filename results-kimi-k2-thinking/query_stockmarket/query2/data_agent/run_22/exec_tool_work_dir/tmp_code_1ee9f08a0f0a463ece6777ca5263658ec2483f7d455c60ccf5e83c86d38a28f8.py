code = """import json

# Read the NYSE Arca ETFs from the first query
with open(var_functions.query_db:0, 'r') as f:
    nyse_arca_etfs = json.load(f)

# Extract just the symbols
nyse_arca_symbols = {etf['Symbol'] for etf in nyse_arca_etfs}

# Read the list of all tables from the second query
with open(var_functions.list_db:2, 'r') as f:
    all_tables = json.load(f)

# Find intersection - ETFs that have price data
common_symbols = nyse_arca_symbols.intersection(all_tables)

# Count how many symbols we need to check
total_to_check = len(common_symbols)

print('__RESULT__:')
print(json.dumps({
    'nyse_arca_etf_count': len(nyse_arca_symbols),
    'total_tables': len(all_tables),
    'common_symbols_count': total_to_check,
    'sample_symbols': list(common_symbols)[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
