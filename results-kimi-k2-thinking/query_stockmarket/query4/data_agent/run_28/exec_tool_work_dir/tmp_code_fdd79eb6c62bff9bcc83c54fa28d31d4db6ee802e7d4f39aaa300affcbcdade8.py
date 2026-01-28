code = """import json
import os

# Load NYSE non-ETF stocks
nyse_file = locals()['var_functions.query_db:10']
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

# Get all available stock symbols from stocktrade database
trade_file = locals()['var_functions.list_db:8']
with open(trade_file, 'r') as f:
    all_trade_symbols = json.load(f)

# Convert to sets for intersection
nyse_symbols = {stock['Symbol'] for stock in nyse_stocks}
trade_symbols = set(all_trade_symbols)

# Find intersection
common_symbols = nyse_symbols.intersection(trade_symbols)

print('NYSE non-ETF stocks:', len(nyse_symbols))
print('Available in trade database:', len(trade_symbols))
print('Common symbols:', len(common_symbols))

# Create a lookup for company names
company_lookup = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}

result = json.dumps({
    'nyse_count': len(nyse_symbols),
    'trade_count': len(trade_symbols),
    'common_count': len(common_symbols),
    'sample_common': list(common_symbols)[:10],
    'lookup_sample': {k: company_lookup[k] for k in list(common_symbols)[:3]}
})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': [{'Listing Exchange': 'A', 'count': '28'}, {'Listing Exchange': 'N', 'count': '234'}, {'Listing Exchange': 'P', 'count': '1444'}, {'Listing Exchange': 'Q', 'count': '710'}, {'Listing Exchange': 'Z', 'count': '336'}], 'var_functions.query_db:2': [], 'var_functions.query_db:5': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:18': {'total_stocks': 234, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:22': [{'Date': '2017-01-03', 'Open': '69.29000091552734', 'High': '70.86000061035156', 'Low': '69.0', 'Close': '70.54000091552734', 'Adj Close': '70.54000091552734', 'Volume': '8112200'}, {'Date': '2017-01-04', 'Open': '71.08000183105469', 'High': '73.06999969482422', 'Low': '70.76000213623047', 'Close': '72.80000305175781', 'Adj Close': '72.80000305175781', 'Volume': '9289500'}, {'Date': '2017-01-05', 'Open': '72.80999755859375', 'High': '73.66000366210938', 'Low': '72.52999877929688', 'Close': '72.79000091552734', 'Adj Close': '72.79000091552734', 'Volume': '4695600'}, {'Date': '2017-01-06', 'Open': '72.88999938964844', 'High': '74.12999725341797', 'Low': '72.55000305175781', 'Close': '73.80000305175781', 'Adj Close': '73.80000305175781', 'Volume': '4466100'}, {'Date': '2017-01-09', 'Open': '74.05000305175781', 'High': '74.44000244140625', 'Low': '73.51000213623047', 'Close': '73.95999908447266', 'Adj Close': '73.95999908447266', 'Volume': '3933100'}], 'var_functions.execute_python:24': {'total_symbols': 2753, 'sample_symbols': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ', 'ABEQ', 'ABMD', 'ACAD', 'ACES', 'ACIO']}}

exec(code, env_args)
