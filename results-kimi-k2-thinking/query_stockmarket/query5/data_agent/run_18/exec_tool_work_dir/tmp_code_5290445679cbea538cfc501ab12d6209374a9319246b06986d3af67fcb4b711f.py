code = """# Read the list of NASDAQ Capital Market tickers
nasdaq_capital_file = var_functions.query_db:0
nasdaq_capital_list = []
with open(nasdaq_capital_file, 'r') as f:
    import json
    nasdaq_capital_list = json.load(f)

# Extract ticker symbols
nasdaq_capital_tickers = [item['Symbol'] for item in nasdaq_capital_list]

# Read the list of available tables in stocktrade_database
stocktrade_tables_file = var_functions.list_db:2
stocktrade_tables = []
with open(stocktrade_tables_file, 'r') as f:
    import json
    stocktrade_tables = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'nasdaq_cap_count': len(nasdaq_capital_tickers),
    'stocktrade_table_count': len(stocktrade_tables),
    'first_10_nasdaq': nasdaq_capital_tickers[:10],
    'first_10_tables': stocktrade_tables[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
