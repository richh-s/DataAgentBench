code = """# Access the NASDAQ Capital Market stocks from the query result
nasdaq_cap_stocks = locals()['var_functions.query_db:0']

# Extract just the symbols
nasdaq_cap_symbols = [stock['Symbol'] for stock in nasdaq_cap_stocks]

print('__RESULT__:')
print(json.dumps({
    'count': len(nasdaq_cap_symbols),
    'symbols_sample': nasdaq_cap_symbols[:20]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:4': 'file_storage/functions.list_db:4.json'}

exec(code, env_args)
