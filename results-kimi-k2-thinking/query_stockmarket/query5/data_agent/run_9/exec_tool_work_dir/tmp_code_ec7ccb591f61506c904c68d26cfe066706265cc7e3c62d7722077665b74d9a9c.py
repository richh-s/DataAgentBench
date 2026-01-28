code = """import json
import os

# Read NASDAQ Capital Market tickers
nasdaq_file_path = '/tmp/tmp_query_result_nasdaq_cap.json'
with open(nasdaq_file_path, 'r') as f:
    nasdaq_stocks = json.load(f)

# Read available trade tables
trade_file_path = '/tmp/tmp_trade_tables_list.json'
with open(trade_file_path, 'r') as f:
    trade_tables = json.load(f)

# Create mapping of ticker to company name
nasdaq_tickers = {}
for stock in nasdaq_stocks:
    symbol = stock['Symbol']
    desc = stock['Company Description']
    # Extract company name
    company_name = desc.split(' specializes in')[0].split(' is ')[0].split(' provides')[0].split(' operates')[0].rstrip('.')
    nasdaq_tickers[symbol] = company_name

# Find intersection with available trade data
available_tickers = list(set(nasdaq_tickers.keys()) & set(trade_tables))
print(f'Total NASDAQ Capital stocks: {len(nasdaq_tickers)}')
print(f'Available with trade data: {len(available_tickers)}')
print('Sample tickers:', available_tickers[:10])

# Save for next step
with open('/tmp/nasdaq_cap_tickers_with_data.json', 'w') as f:
    json.dump(available_tickers, f)"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:24': {'nasdaq_path': 'var_functions.query_db:4', 'trade_path': 'var_functions.list_db:8'}, 'var_functions.query_db:32': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.list_db:42': 'file_storage/functions.list_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
