code = """import pandas as pd
import numpy as np
import json
from pathlib import Path

# Read the data file
file_path = '/tmp/tmpu4l8a_7i/index_trade_data.json'
with open(file_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert data types
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])
df['Open'] = pd.to_numeric(df['Open'])

# Filter data from January 2000 onwards
df_filtered = df[df['Date'] >= '2000-01-01'].copy()

# Create country mapping for indices
index_country_map = {
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'HSI': 'Hong Kong',
    'IXIC': 'USA',
    'J203.JO': 'South Africa',
    'N100': 'Netherlands',
    'N225': 'Japan',
    'NSEI': 'India',
    'NYA': 'USA',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan'
}

# Add country column
df_filtered['Country'] = df_filtered['Index'].map(index_country_map)

print('__RESULT__:')
print(json.dumps(f"Loaded {len(df_filtered)} records from {df_filtered['Date'].min()} to {df_filtered['Date'].max()}, indices: {sorted(df_filtered['Index'].unique())}"))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': 'Error: File not found at /tmp/tmpu4l8a_7i/index_trade_data.json', 'var_functions.query_db:12': [{'Index': '000001.SS', 'earliest_date': '2000-01-04 00:00:00', 'latest_date': 'September 30, 2015 at 12:00 AM', 'total_days': '4354'}, {'Index': '399001.SZ', 'earliest_date': '2000-01-05 00:00:00', 'latest_date': 'September 30, 2015 at 12:00 AM', 'total_days': '4355'}, {'Index': 'GDAXI', 'earliest_date': '2000-01-05 00:00:00', 'latest_date': 'September 30, 2016 at 12:00 AM', 'total_days': '5590'}, {'Index': 'GSPTSE', 'earliest_date': '2000-01-05 00:00:00', 'latest_date': 'September 30, 2016 at 12:00 AM', 'total_days': '6506'}, {'Index': 'HSI', 'earliest_date': '2000-01-14 00:00:00', 'latest_date': 'September 30, 2019 at 12:00 AM', 'total_days': '5604'}, {'Index': 'IXIC', 'earliest_date': '2000-01-06 00:00:00', 'latest_date': 'September 30, 2015 at 12:00 AM', 'total_days': '7351'}, {'Index': 'J203.JO', 'earliest_date': '2012-02-08 00:00:00', 'latest_date': 'September 30, 2019 at 12:00 AM', 'total_days': '1854'}, {'Index': 'N100', 'earliest_date': '2000-01-10 00:00:00', 'latest_date': 'September 30, 2019 at 12:00 AM', 'total_days': '4245'}, {'Index': 'N225', 'earliest_date': '2000-01-04 00:00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_days': '7979'}, {'Index': 'NSEI', 'earliest_date': '2007-09-25 00:00:00', 'latest_date': 'September 30, 2014 at 12:00 AM', 'total_days': '2577'}, {'Index': 'NYA', 'earliest_date': '2000-01-03 00:00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_days': '7960'}, {'Index': 'SSMI', 'earliest_date': '2000-01-05 00:00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_days': '5188'}, {'Index': 'TWII', 'earliest_date': '2000-01-17 00:00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_days': '4385'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
