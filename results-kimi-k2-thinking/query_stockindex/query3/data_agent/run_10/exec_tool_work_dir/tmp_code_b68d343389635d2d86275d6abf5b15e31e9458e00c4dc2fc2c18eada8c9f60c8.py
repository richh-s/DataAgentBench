code = """import pandas as pd
import numpy as np
import json
from pathlib import Path

# Read the full data from the file path
file_path = '/tmp/tmpu4l8a_7i/index_trade_data.json'

# Check if file exists and load it
if Path(file_path).exists():
    with open(file_path, 'r') as f:
        index_trade_data = json.load(f)
else:
    # If file doesn't exist, we'll need to query the database differently
    print('__RESULT__:')
    print(json.dumps(f"Error: File not found at {file_path}"))
    exit()

# Convert to DataFrame
df = pd.DataFrame(index_trade_data)

# Convert data types
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])
df['Open'] = pd.to_numeric(df['Open'])

# Filter from year 2000 onwards
df_2000 = df[df['Date'] >= '2000-01-01'].copy()

print('__RESULT__:')
print(json.dumps(f"Data loaded. Shape: {df_2000.shape}, Date range: {df_2000['Date'].min()} to {df_2000['Date'].max()}, Indices: {sorted(df_2000['Index'].unique())}"))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
