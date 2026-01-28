code = """import json
import os

# Access the file paths from stored variables
nasdaq_file_path = locals()['var_functions.query_db:4']
trade_file_path = locals()['var_functions.list_db:8']

print("NASDAQ file:", nasdaq_file_path)
print("Trade file:", trade_file_path)

# Load the data
with open(nasdaq_file_path, 'r') as f:
    nasdaq_caps = json.load(f)

with open(trade_file_path, 'r') as f:
    trade_tables = json.load(f)

print(f"NASDAQ Capital stocks: {len(nasdaq_caps)}")
print(f"Trade tables: {len(trade_tables)}")

# Find intersection
nasdaq_tickers = [item['Symbol'] for item in nasdaq_caps]
available_tickers = list(set(nasdaq_tickers) & set(trade_tables))

print(f"Available NASDAQ Cap stocks: {len(available_tickers)}")
print("Sample:", available_tickers[:10])"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:24': {'nasdaq_path': 'var_functions.query_db:4', 'trade_path': 'var_functions.list_db:8'}}

exec(code, env_args)
