code = """import json
import os

# Get the full list of ETFs
nysearca_file = locals()['var_functions.execute_python:10']
with open(nysearca_file, 'r') as f:
    etfs = json.load(f)

print(f"Total ETFs to check: {len(etfs)}")
print(f"First few: {etfs[:10]}")

# We'll check a sample first to see which ones might have prices > $200 in 2015
# Based on historical data, some candidates might include:
# - SPY, IVV, VTI (around $180-210 in 2015)
# - Some leveraged/inverse ETFs could be higher or have splits

# Let's create a test list of popular ETFs first
test_etfs = ['SPY', 'IVV', 'VTI', 'QQQ', 'VUG', 'VTV', 'VWO', 'VEA', 'EFA', 'EEM', 'BND', 'AGG', 'TLT', 'GLD']
test_etfs = [etf for etf in test_etfs if etf in etfs]

print(f"\nTesting popular ETFs first: {test_etfs}")

# For now, return the full list for systematic checking
result = json.dumps(etfs)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': [{'Date': '1993-01-29', 'Open': '43.96875', 'High': '43.96875', 'Low': '43.75', 'Close': '43.9375', 'Adj Close': '26.299287796020508', 'Volume': '1003200'}, {'Date': '1993-02-01', 'Open': '43.96875', 'High': '44.25', 'Low': '43.96875', 'Close': '44.25', 'Adj Close': '26.48632431030273', 'Volume': '480500'}, {'Date': '1993-02-02', 'Open': '44.21875', 'High': '44.375', 'Low': '44.125', 'Close': '44.34375', 'Adj Close': '26.54244804382324', 'Volume': '201300'}], 'var_functions.execute_python:14': {'etf_count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:16': []}

exec(code, env_args)
