code = """import json

# Load the stored file paths
nyse_file = 'var_functions.query_db:22'
tickers_file = 'var_functions.list_db:6'

# Read files
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

with open(tickers_file, 'r') as f:
    available_tickers = json.load(f)

print(f'Loaded {len(nyse_stocks)} NYSE non-ETF stocks from stockinfo')
print(f'Loaded {len(available_tickers)} tickers from stocktrade database')

# Create lookup dictionaries
symbol_to_desc = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}
nyse_symbols = set(symbol_to_desc.keys())
available_set = set(available_tickers)

# Find common symbols (NYSE stocks with price data)
common_symbols = list(nyse_symbols.intersection(available_set))
print(f'Found {len(common_symbols)} common symbols to analyze')

# Show first 10
print('\nFirst 10 stocks to analyze:')
for sym in sorted(common_symbols)[:10]:
    print(f'  {sym}: {symbol_to_desc[sym][:60]}...')

# Return the common symbols and description mapping
result = {
    'common_symbols': common_symbols,
    'symbol_to_desc': symbol_to_desc,
    'count': len(common_symbols)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:28': [{'Date': '2017-01-03', 'Open': '34.66999816894531', 'High': '35.220001220703125', 'Low': '34.52000045776367', 'Close': '35.15999984741211', 'Adj Close': '33.58498001098633', 'Volume': '631900'}, {'Date': '2017-01-04', 'Open': '35.06999969482422', 'High': '35.9900016784668', 'Low': '34.970001220703125', 'Close': '35.93000030517578', 'Adj Close': '34.320491790771484', 'Volume': '840900'}, {'Date': '2017-01-05', 'Open': '35.81999969482422', 'High': '36.29999923706055', 'Low': '35.43000030517578', 'Close': '36.02999877929688', 'Adj Close': '34.4160041809082', 'Volume': '918000'}, {'Date': '2017-01-06', 'Open': '36.18000030517578', 'High': '36.27999877929688', 'Low': '35.529998779296875', 'Close': '35.540000915527344', 'Adj Close': '33.94796371459961', 'Volume': '663000'}, {'Date': '2017-01-09', 'Open': '35.459999084472656', 'High': '35.459999084472656', 'Low': '34.70000076293945', 'Close': '34.72999954223633', 'Adj Close': '33.17424011230469', 'Volume': '659700'}], 'var_functions.execute_python:30': {'status': 'analysis_started', 'message': 'Need to query 2017 data for NYSE stocks'}}

exec(code, env_args)
