code = """import json
import os

# Load NYSE stocks data
nyse_file = 'var_functions.query_db:22'
tickers_file = 'var_functions.list_db:6'

# Read and parse the files
nyse_stocks = []
with open(nyse_file, 'r') as f:
    content = f.read().strip()
    # Handle JSON array format
    if content.startswith('['):
        nyse_stocks = json.loads(content)
    else:
        # Line by line JSON objects
        for line in content.split('\n'):
            if line.strip():
                nyse_stocks.append(json.loads(line))

# Load available tickers
available_tickers = []
with open(tickers_file, 'r') as f:
    content = f.read().strip()
    if content.startswith('['):
        available_tickers = json.loads(content)
    else:
        for line in content.split('\n'):
            if line.strip():
                available_tickers.append(json.loads(line) if line.startswith('{') else line.strip('"'))

# Create symbol to description mapping
symbol_desc = {}
for stock in nyse_stocks:
    if isinstance(stock, dict) and 'Symbol' in stock:
        symbol_desc[stock['Symbol']] = stock['Company Description']

# Find common symbols
nyse_symbols = set(symbol_desc.keys())
available_set = set(available_tickers) if available_tickers and isinstance(available_tickers[0], str) else set()
common = list(nyse_symbols.intersection(available_set))

print(f'Loaded {len(nyse_stocks)} NYSE stocks')
print(f'Found {len(available_tickers)} tickers in trade DB')
print(f'Common symbols: {len(common)}')

result_data = {
    'common_symbols': common[:20],  # Return sample for verification
    'symbol_desc_sample': {k: symbol_desc[k][:50] for k in list(symbol_desc.keys())[:5]},
    'total_common': len(common)
}

print('\n__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:28': [{'Date': '2017-01-03', 'Open': '34.66999816894531', 'High': '35.220001220703125', 'Low': '34.52000045776367', 'Close': '35.15999984741211', 'Adj Close': '33.58498001098633', 'Volume': '631900'}, {'Date': '2017-01-04', 'Open': '35.06999969482422', 'High': '35.9900016784668', 'Low': '34.970001220703125', 'Close': '35.93000030517578', 'Adj Close': '34.320491790771484', 'Volume': '840900'}, {'Date': '2017-01-05', 'Open': '35.81999969482422', 'High': '36.29999923706055', 'Low': '35.43000030517578', 'Close': '36.02999877929688', 'Adj Close': '34.4160041809082', 'Volume': '918000'}, {'Date': '2017-01-06', 'Open': '36.18000030517578', 'High': '36.27999877929688', 'Low': '35.529998779296875', 'Close': '35.540000915527344', 'Adj Close': '33.94796371459961', 'Volume': '663000'}, {'Date': '2017-01-09', 'Open': '35.459999084472656', 'High': '35.459999084472656', 'Low': '34.70000076293945', 'Close': '34.72999954223633', 'Adj Close': '33.17424011230469', 'Volume': '659700'}], 'var_functions.execute_python:30': {'status': 'analysis_started', 'message': 'Need to query 2017 data for NYSE stocks'}}

exec(code, env_args)
