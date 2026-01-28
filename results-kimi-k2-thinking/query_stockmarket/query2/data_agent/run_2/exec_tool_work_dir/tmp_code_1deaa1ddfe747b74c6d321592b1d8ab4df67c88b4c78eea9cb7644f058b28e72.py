code = """import json
import os

# Read ETF symbols from first query result
etf_file = 'file_storage/functions.query_db:0.json'
if os.path.exists(etf_file):
    with open(etf_file, 'r') as f:
        nyse_arca_etfs = json.load(f)
    arca_symbols = set(etf['Symbol'] for etf in nyse_arca_etfs)
    print(f'NYSE Arca ETFs: {len(arca_symbols)}')
else:
    print('ETF file not found')
    arca_symbols = set()

# Read all ticker symbols from second database (tables list)
tickers_file = 'file_storage/functions.list_db:16.json'
if os.path.exists(tickers_file):
    with open(tickers_file, 'r') as f:
        all_tickers = json.load(f)
    all_symbols = set(all_tickers)
    print(f'All tickers in price DB: {len(all_symbols)}')
else:
    print('Tickers file not found')
    all_symbols = set()

# Find intersection
common_symbols = arca_symbols.intersection(all_symbols)
print(f'Common symbols: {len(common_symbols)}')
print(f'First 10: {list(common_symbols)[:10]}')

print('__RESULT__:')
print(json.dumps(sorted(list(common_symbols))))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.list_db:16': 'file_storage/functions.list_db:16.json'}

exec(code, env_args)
