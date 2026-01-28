code = """import json
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

# Load the data
file_path = var_functions.query_db:8
if isinstance(file_path, str) and (file_path.endswith('.json') or '/' in file_path or '\\' in file_path):
    # It's a file path
    with open(file_path, 'r') as f:
        data = json.load(f)
else:
    # It's already a Python object
    data = var_functions.query_db:8

# Create DataFrame
df = pd.DataFrame(data)
print("__DATA_LOADED__:")
print(f"Loaded {len(df)} records")
print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
print(f"Indices available: {sorted(df['Index'].unique())}")

# Fix CloseUSD type
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'])

# Group by month and get monthly closing prices
monthly_data = df.groupby(['Index', pd.Grouper(key='Date', freq='M')]).agg({
    'CloseUSD': 'last'
}).reset_index()

# Filter from 2000 onwards
monthly_data = monthly_data[monthly_data['Date'] >= '2000-01-01']

print(f"Monthly data points: {len(monthly_data)}")
print("__RESULT__:")
print(json.dumps({"indices_count": int(monthly_data['Index'].nunique()), 
                  "months_per_index": monthly_data.groupby('Index').size().to_dict()}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
