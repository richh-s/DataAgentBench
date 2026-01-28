code = """import json
import os

# The stored variables are the file paths
nasdaq_file_path = var_functions.query_db:4
trade_file_path = var_functions.list_db:8

print("Opening NASDAQ Capital Market data...")
with open(nasdaq_file_path, 'r') as f:
    nasdaq_caps = json.load(f)

print("Opening trade tables list...")
with open(trade_file_path, 'r') as f:
    trade_tables = json.load(f)

print(f"Found {len(nasdaq_caps)} NASDAQ Capital Market stocks")
print(f"Found {len(trade_tables)} total trade tables")

# Extract tickers that exist in both
nasdaq_tickers = [item['Symbol'] for item in nasdaq_caps]
available_tickers = list(set(nasdaq_tickers) & set(trade_tables))

print(f"Found {len(available_tickers)} NASDAQ Capital Market stocks with trade data")
print("Sample:", available_tickers[:5])"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:24': {'nasdaq_path': 'var_functions.query_db:4', 'trade_path': 'var_functions.list_db:8'}}

exec(code, env_args)
