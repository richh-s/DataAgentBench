code = """import json

# Read NYSE stocks
f = open('var_functions.query_db:22', 'r')
nyse_data = json.load(f)
f.close()

# Read available tickers
f = open('var_functions.list_db:6', 'r')
tickers_data = json.load(f)
f.close()

# Create symbol-description mapping and find intersection
symbol_desc = {}
for item in nyse_data:
    symbol_desc[item['Symbol']] = item['Company Description']

nyse_set = set(symbol_desc.keys())
available_set = set(tickers_data)
common = list(nyse_set.intersection(available_set))

print('Analysis setup complete:')
print(f'  NYSE stocks: {len(nyse_data)}')
print(f'  Available tickers: {len(tickers_data)}')
print(f'  Common for analysis: {len(common)}')

result = {
    'common_symbols': common,
    'symbol_desc': symbol_desc,
    'count': len(common)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:28': [{'Date': '2017-01-03', 'Open': '34.66999816894531', 'High': '35.220001220703125', 'Low': '34.52000045776367', 'Close': '35.15999984741211', 'Adj Close': '33.58498001098633', 'Volume': '631900'}, {'Date': '2017-01-04', 'Open': '35.06999969482422', 'High': '35.9900016784668', 'Low': '34.970001220703125', 'Close': '35.93000030517578', 'Adj Close': '34.320491790771484', 'Volume': '840900'}, {'Date': '2017-01-05', 'Open': '35.81999969482422', 'High': '36.29999923706055', 'Low': '35.43000030517578', 'Close': '36.02999877929688', 'Adj Close': '34.4160041809082', 'Volume': '918000'}, {'Date': '2017-01-06', 'Open': '36.18000030517578', 'High': '36.27999877929688', 'Low': '35.529998779296875', 'Close': '35.540000915527344', 'Adj Close': '33.94796371459961', 'Volume': '663000'}, {'Date': '2017-01-09', 'Open': '35.459999084472656', 'High': '35.459999084472656', 'Low': '34.70000076293945', 'Close': '34.72999954223633', 'Adj Close': '33.17424011230469', 'Volume': '659700'}], 'var_functions.execute_python:30': {'status': 'analysis_started', 'message': 'Need to query 2017 data for NYSE stocks'}}

exec(code, env_args)
