code = """import json

# Read the file for stockinfo query
with open(var_functions.query_db:0, 'r') as f:
    nasdaq_capital_stocks = json.load(f)

# Read the file for stocktrade list
with open(var_functions.list_db:2, 'r') as f:
    all_trade_tables = json.load(f)

# Find intersection - stocks that are both in NASDAQ Capital Market and have price data
nasdaq_symbols = set(stock['Symbol'] for stock in nasdaq_capital_stocks)
trade_symbols = set(all_trade_tables)

valid_symbols = nasdaq_symbols.intersection(trade_symbols)
print('__RESULT__:')
print(json.dumps({
    'nasdaq_capital_count': len(nasdaq_symbols),
    'trade_tables_count': len(trade_symbols),
    'valid_symbols_count': len(valid_symbols),
    'sample_valid_symbols': list(valid_symbols)[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
