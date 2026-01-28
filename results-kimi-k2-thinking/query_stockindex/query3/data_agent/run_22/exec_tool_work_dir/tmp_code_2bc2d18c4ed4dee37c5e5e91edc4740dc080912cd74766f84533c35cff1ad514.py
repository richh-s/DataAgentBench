code = """import json
import pandas as pd
from datetime import datetime
import numpy as np

# Get the data from storage
result_data = var_functions.query_db:8

# Check if it's a file path
file_path = str(result_data)
if file_path.endswith('.json') or ('/' in file_path or '\\' in file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
else:
    data = result_data

# Create DataFrame
df = pd.DataFrame(data)
print("Data loaded successfully")
print("Total records:", len(df))
print("Date range:", df['Date'].min(), "to", df['Date'].max())
print("Indices available:", sorted(df['Index'].unique()))

# Convert data types
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'])
df = df.dropna(subset=['CloseUSD'])

# Create monthly data
monthly_data = df.groupby(['Index', pd.Grouper(key='Date', freq='M')]).agg({
    'CloseUSD': 'last'
}).reset_index()

monthly_data = monthly_data[monthly_data['Date'] >= '2000-01-01']
indices = monthly_data['Index'].unique()
print("\nProcessing indices from 2000 onwards:", len(indices))

# Index to exchange mapping
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
print(json.dumps({"status": "success", "indices": sorted(indices), "total_records": len(monthly_data)}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
