code = """import json
import os

# Access the stored results
nasdaq_stocks = var_functions.query_db:54
trade_tables = var_functions.list_db:42

# Create ticker to company name mapping
nasdaq_tickers = {}
for stock in nasdaq_stocks:
    symbol = stock['Symbol']
    desc = stock['Company Description']
    # Extract company name - split at common separators
    company_name = desc.split(' specializes in')[0].split(' is ')[0].split(' provides')[0].split(' operates')[0].rstrip('.')
    nasdaq_tickers[symbol] = company_name

# Find intersection with available trade data
available_tickers = list(set(nasdaq_tickers.keys()) & set(trade_tables))

print(f'NASDAQ Capital Market stocks: {len(nasdaq_tickers)}')
print(f'With trade data: {len(available_tickers)}')

# Process first 100 tickers to find high volatility days in 2019
results = []
for ticker in available_tickers[:100]:  # Limit to first 100 for now
    try:
        # Get 2019 data for this ticker
        query_db('stocktrade_database', f'SELECT COUNT(*) as count FROM "{ticker}" WHERE Date >= "2019-01-01" AND Date <= "2019-12-31" AND ((High - Low) / Low) > 0.20')
    except:
        continue

print('Processing complete')"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:24': {'nasdaq_path': 'var_functions.query_db:4', 'trade_path': 'var_functions.list_db:8'}, 'var_functions.query_db:32': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.list_db:42': 'file_storage/functions.list_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:50': ['AGMH', 'BCLI', 'BLFS', 'BOTJ', 'BWEN', 'CBAT', 'CEMI', 'HRTX'], 'var_functions.query_db:52': [{'high_vol_days': '13'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json'}

exec(code, env_args)
