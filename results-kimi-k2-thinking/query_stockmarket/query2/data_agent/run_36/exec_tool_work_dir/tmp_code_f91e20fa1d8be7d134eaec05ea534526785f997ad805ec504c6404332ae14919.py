code = """import json

# Get the full list of NYSE Arca ETFs
nysearca_file = locals()['var_functions.execute_python:10']
with open(nysearca_file, 'r') as f:
    etfs = json.load(f)

print(f"Total NYSE Arca ETFs to check: {len(etfs)}")

# Create a batch checking script - let's start with common broad market ETFs that might exceed $200
# Based on 2015 market data: S&P 500 ranged from ~1860-2130 (points, roughly equals ETF price)
# So SPY/IVV/VOO might have been close to or above $200
broad_market = ['SPY', 'IVV', 'VOO', 'VTI', 'QQQ', 'VUG', 'VTV']
broad_market = [etf for etf in broad_market if etf in etfs]

print(f"Broad market ETF candidates: {broad_market}")

# We'll need to systematically query each of the 1435 ETFs
# For performance, let's check likely candidates first, then batch process
likely_etfs = broad_market
batch1 = etfs[:100]  # First 100 for initial test

result = {"total": len(etfs), "candidates": likely_etfs, "batch1_count": len(batch1)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': [{'Date': '1993-01-29', 'Open': '43.96875', 'High': '43.96875', 'Low': '43.75', 'Close': '43.9375', 'Adj Close': '26.299287796020508', 'Volume': '1003200'}, {'Date': '1993-02-01', 'Open': '43.96875', 'High': '44.25', 'Low': '43.96875', 'Close': '44.25', 'Adj Close': '26.48632431030273', 'Volume': '480500'}, {'Date': '1993-02-02', 'Open': '44.21875', 'High': '44.375', 'Low': '44.125', 'Close': '44.34375', 'Adj Close': '26.54244804382324', 'Volume': '201300'}], 'var_functions.execute_python:14': {'etf_count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:16': [], 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.query_db:22': [{'max_adj_close': '193.3121490478516'}], 'var_functions.query_db:24': [{'max_adj_close': '193.5270538330078'}]}

exec(code, env_args)
