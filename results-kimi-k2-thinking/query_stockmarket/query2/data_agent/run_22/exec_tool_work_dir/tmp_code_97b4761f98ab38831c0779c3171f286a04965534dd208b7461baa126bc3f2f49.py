code = """import json

# Get the file paths from locals()
nyse_arca_file = 'var_functions.query_db:0' in locals() and locals()['var_functions.query_db:0'] or None
all_tables_file = 'var_functions.list_db:2' in locals() and locals()['var_functions.list_db:2'] or None

if nyse_arca_file:
    with open(nyse_arca_file, 'r') as f:
        nyse_arca_etfs = json.load(f)
else:
    nyse_arca_etfs = []

if all_tables_file:
    with open(all_tables_file, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = []

# Extract just the NYSE Arca ETF symbols
nyse_arca_symbols = {etf['Symbol'] for etf in nyse_arca_etfs}

# Find intersection - ETFs that have price data
common_symbols = nyse_arca_symbols.intersection(all_tables)

# Count how many symbols we need to check
total_to_check = len(common_symbols)

# Create result dict
result = {
    'nyse_arca_etf_count': len(nyse_arca_symbols),
    'total_tables': len(all_tables),
    'common_symbols_count': total_to_check,
    'sample_symbols': list(common_symbols)[:10]
}

# Print in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
