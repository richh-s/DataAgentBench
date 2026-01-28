code = """import json

# Access the query results from storage
nyse_arca_etfs = locals()['var_functions.query_db:2']
nyse_arca_symbols = set([etf['Symbol'] for etf in nyse_arca_etfs])

# Access the list of tables from storage
all_tables = locals()['var_functions.list_db:5']

# Find intersection (ETFs that have price data)
etfs_with_data = nyse_arca_symbols.intersection(all_tables)

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_symbols),
    'total_tables_in_db': len(all_tables),
    'etfs_with_price_data': len(etfs_with_data),
    'sample_etfs': list(etfs_with_data)[:10]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)
