code = """import json

# Get all stock symbols from the stocktrade database
all_trade_symbols_result = locals()['var_functions.list_db:4']

# Read the file
with open(all_trade_symbols_result, 'r') as f:
    all_trade_symbols = json.load(f)

# Get NASDAQ Capital Market symbols
nasdaq_cap_file_path = locals()['var_functions.query_db:0']
with open(nasdaq_cap_file_path, 'r') as f:
    nasdaq_cap_stocks = json.load(f)

nasdaq_cap_symbols = [stock['Symbol'] for stock in nasdaq_cap_stocks]

# Find intersection (symbols that exist in both)
existing_symbols = [symbol for symbol in nasdaq_cap_symbols if symbol in all_trade_symbols]

print('__RESULT__:')
print(json.dumps({
    'nasdaq_cap_count': len(nasdaq_cap_symbols),
    'trade_db_count': len(all_trade_symbols),
    'intersection_count': len(existing_symbols),
    'existing_symbols_sample': existing_symbols[:20]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:4': 'file_storage/functions.list_db:4.json', 'var_functions.execute_python:14': {'file_path': 'file_storage/functions.query_db:0.json', 'count': 86, 'symbols_sample': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}}

exec(code, env_args)
