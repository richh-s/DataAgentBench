code = """# Access the ETF symbols from the query result
etf_symbols_data = var_functions.query_db_2

# Extract just the symbols
etf_symbols = [item['Symbol'] for item in etf_symbols_data]

# Check how many we have
print('__RESULT__:')
print(json.dumps({'count': len(etf_symbols), 'symbols': etf_symbols[:10]}))  # Just show first 10 for preview"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
