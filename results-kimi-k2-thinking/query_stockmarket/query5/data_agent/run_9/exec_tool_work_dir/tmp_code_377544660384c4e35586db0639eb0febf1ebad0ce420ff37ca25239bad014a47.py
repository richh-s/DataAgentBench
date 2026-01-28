code = """import json
import os

# Get NASDAQ Capital Market stocks
nasdaq_file = '/tmp/tmps5y2f4r1.json'  # This should be the file path for query_db:54
with open(nasdaq_file, 'r') as f:
    nasdaq_stocks = json.load(f)

# Get trade tables
trade_file = '/tmp/tmp0q5z5u2h.json'  # This should be the file path for list_db:42
with open(trade_file, 'r') as f:
    trade_tables = json.load(f)

print(f"NASDAQ Capital stocks: {len(nasdaq_stocks)}")
print(f"Trade tables: {len(trade_tables)}")

# Extract tickers from NASDAQ stocks
nasdaq_tickers = [stock['Symbol'] for stock in nasdaq_stocks]
print(f"NASDAQ tickers: {len(nasdaq_tickers)}")
print(f"Sample: {nasdaq_tickers[:10]}")

# Check if files are accessible
print(f"NASDAQ file exists: {os.path.exists(nasdaq_file)}")
print(f"Trade file exists: {os.path.exists(trade_file)}")"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:24': {'nasdaq_path': 'var_functions.query_db:4', 'trade_path': 'var_functions.list_db:8'}, 'var_functions.query_db:32': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.list_db:42': 'file_storage/functions.list_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:50': ['AGMH', 'BCLI', 'BLFS', 'BOTJ', 'BWEN', 'CBAT', 'CEMI', 'HRTX'], 'var_functions.query_db:52': [{'high_vol_days': '13'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json'}

exec(code, env_args)
