code = """import json

# Load the ETF symbols from the file
etfs_file = var_functions.query_db:5
with open(etfs_file, 'r') as f:
    etfs_data = json.load(f)

# Extract symbols
nyse_arca_etfs = [item['Symbol'] for item in etfs_data]

# Read the tables list
tables_file = var_functions.list_db:2
with open(tables_file, 'r') as f:
    all_tables = json.load(f)

# Find intersection - ETFs that have price data tables
available_etfs = list(set(nyse_arca_etfs) & set(all_tables))

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_etfs),
    'available_etfs_count': len(available_etfs),
    'sample_available_etfs': available_etfs[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
