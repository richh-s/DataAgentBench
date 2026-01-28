code = """import json

# Read the actual data from the files
nyse_arca_etfs_file = locals()['var_functions.query_db:2']
all_tables_file = locals()['var_functions.list_db:5']

with open(nyse_arca_etfs_file, 'r') as f:
    nyse_arca_etfs = json.load(f)

with open(all_tables_file, 'r') as f:
    all_tables = json.load(f)

nyse_arca_symbols = set([etf['Symbol'] for etf in nyse_arca_etfs])

# Find intersection (ETFs that have price data)
etfs_with_data = nyse_arca_symbols.intersection(all_tables)

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_symbols),
    'total_tables_in_db': len(all_tables),
    'etfs_with_price_data': len(etfs_with_data),
    'sample_etfs': list(etfs_with_data)[:10]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:10': {'nyse_arca_etfs_type': "<class 'str'>", 'nyse_arca_etfs_length': 38, 'nyse_arca_etfs_sample': 'fil', 'all_tables_type': "<class 'str'>", 'all_tables_length': 37, 'all_tables_sample': 'fil'}}

exec(code, env_args)
