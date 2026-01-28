code = """import json

# Access the query result from storage
nyse_stockinfo = locals()['var_functions.query_db:0']

# Extract symbols and company descriptions
symbols = [stock['Symbol'] for stock in nyse_stockinfo]
company_descriptions = {stock['Symbol']: stock['Company Description'] for stock in nyse_stockinfo}

print('__RESULT__:')
print(json.dumps({
    'total_stocks': len(symbols),
    'first_10_symbols': symbols[:10],
    'total_stocks_info': len(nyse_stockinfo)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': ['stockinfo']}

exec(code, env_args)
