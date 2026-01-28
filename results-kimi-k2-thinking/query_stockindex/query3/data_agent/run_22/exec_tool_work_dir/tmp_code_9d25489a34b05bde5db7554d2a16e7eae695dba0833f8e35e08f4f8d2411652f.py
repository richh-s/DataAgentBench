code = """import json
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import os

# Load the data from storage
storage_key = 'var_functions.query_db:8'
result_data = locals()[storage_key]

# Check if it's a file path or direct data
if isinstance(result_data, str) and (result_data.endswith('.json') or '/' in result_data or os.sep in result_data):
    # It's a file path
    with open(result_data, 'r') as f:
        data = json.load(f)
else:
    # It's already a Python object
    data = result_data

# Create DataFrame
df = pd.DataFrame(data)
print("Data loaded successfully")
print(f"Total records: {len(df)}")
print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
print(f"Indices available: {sorted(df['Index'].unique())}")

# Convert data types
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'])

# Remove any rows with null CloseUSD
df = df.dropna(subset=['CloseUSD'])

# Group by month and get monthly closing prices
monthly_data = df.groupby(['Index', pd.Grouper(key='Date', freq='M')]).agg({
    'CloseUSD': 'last'
}).reset_index()

# Filter from 2000 onwards
monthly_data = monthly_data[monthly_data['Date'] >= '2000-01-01']

indices = monthly_data['Index'].unique()
print(f"\nProcessing {len(indices)} indices from 2000 onwards")

# Dictionary to map index symbols to exchange names
index_to_exchange = {
    'N225': 'Tokyo Stock Exchange',
    'HSI': 'Hong Kong Stock Exchange', 
    '000001.SS': 'Shanghai Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    'IXIC': 'NASDAQ',
    'NYA': 'New York Stock Exchange',
    'GDAXI': 'Frankfurt Stock Exchange',
    'GSPTSE': 'Toronto Stock Exchange',
    'NSEI': 'National Stock Exchange of India',
    'N100': 'Euronext',
    'SSMI': 'SIX Swiss Exchange',
    'TWII': 'Taiwan Stock Exchange',
    'J203.JO': 'Johannesburg Stock Exchange'
}

print("\n__RESULT__:")
result = {
    "indices_count": int(monthly_data['Index'].nunique()),
    "total_months": int(len(monthly_data)),
    "indices": sorted(indices),
    "index_mapping": index_to_exchange
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
