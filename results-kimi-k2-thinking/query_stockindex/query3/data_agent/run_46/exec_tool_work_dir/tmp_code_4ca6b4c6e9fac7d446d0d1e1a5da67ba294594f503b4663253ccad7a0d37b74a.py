code = """import json
import pandas as pd
from datetime import datetime

# Load data
index_info = locals()['var_functions.query_db:13']
price_data_file = locals()['var_functions.query_db:16']

# Load price data from file
if isinstance(price_data_file, str) and price_data_file.endswith('.json'):
    with open(price_data_file, 'r') as f:
        price_data = json.load(f)
else:
    price_data = price_data_file

print(f"Loaded {len(price_data)} price records")
print(f"Loaded {len(index_info)} index info records")

# Create index to exchange/country mapping
index_mapping = {
    '000001.SS': {'exchange': 'Shanghai Stock Exchange', 'country': 'China'},
    '399001.SZ': {'exchange': 'Shenzhen Stock Exchange', 'country': 'China'},
    'GDAXI': {'exchange': 'Frankfurt Stock Exchange', 'country': 'Germany'},
    'GSPTSE': {'exchange': 'Toronto Stock Exchange', 'country': 'Canada'},
    'HSI': {'exchange': 'Hong Kong Stock Exchange', 'country': 'Hong Kong'},
    'IXIC': {'exchange': 'NASDAQ', 'country': 'USA'},
    'J203.JO': {'exchange': 'Johannesburg Stock Exchange', 'country': 'South Africa'},
    'N100': {'exchange': 'Euronext', 'country': 'Netherlands'},
    'N225': {'exchange': 'Tokyo Stock Exchange', 'country': 'Japan'},
    'NSEI': {'exchange': 'National Stock Exchange of India', 'country': 'India'},
    'NYA': {'exchange': 'New York Stock Exchange', 'country': 'USA'},
    'SSMI': {'exchange': 'SIX Swiss Exchange', 'country': 'Switzerland'},
    'TWII': {'exchange': 'Taiwan Stock Exchange', 'country': 'Taiwan'}
}

# Convert to DataFrame
df = pd.DataFrame(price_data)
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

print(f"DataFrame shape: {df.shape}")
print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
print(f"Indices: {df['Index'].unique()}")

# Calculate monthly data for each index
monthly_data = []
for idx in df['Index'].unique():
    idx_data = df[df['Index'] == idx].copy()
    idx_data = idx_data.sort_values('Date')
    
    # Get first trading day of each month
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    monthly_prices = idx_data.groupby('YearMonth').first().reset_index()
    
    if len(monthly_prices) > 0:
        monthly_data.append({
            'Index': idx,
            'Data': monthly_prices
        })

print(f"Processed {len(monthly_data)} indices")
if len(monthly_data) > 0:
    print(f"Sample for {monthly_data[0]['Index']}: {len(monthly_data[0]['Data'])} months")
    print(monthly_data[0]['Data'].head())

print('__RESULT__:')
print(json.dumps({
    'status': 'data_loaded',
    'num_indices': len(monthly_data),
    'indices': [item['Index'] for item in monthly_data]
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:13': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
