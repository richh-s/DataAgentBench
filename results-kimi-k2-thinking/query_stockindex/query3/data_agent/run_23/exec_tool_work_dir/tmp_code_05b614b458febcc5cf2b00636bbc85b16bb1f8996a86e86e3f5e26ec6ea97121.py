code = """import json
import pandas as pd
from datetime import datetime
import os

# Get the file path from storage
storage_key = 'var_functions.query_db:36'
result_data = locals()[storage_key]

# Load the data
if isinstance(result_data, str):
    file_path = result_data
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
    else:
        print(f"File not found: {file_path}")
        data = []
else:
    data = result_data

print('Loaded records:', len(data))

# Convert to DataFrame
df = pd.DataFrame(data)

# Process date column - handle different formats
def parse_date(date_str):
    try:
        if 'September' in date_str:
            return pd.to_datetime(date_str)
        else:
            return pd.to_datetime(date_str)
    except:
        return pd.NaT

df['Date'] = df['Date'].apply(parse_date)
df = df.dropna(subset=['Date'])

# Convert CloseUSD to numeric
pd.to_numeric(df['CloseUSD'])

# Filter for data from 2000 onwards
df = df[df['Date'] >= '2000-01-01'].copy()

print('Filtered records:', len(df))
print('Date range:', df['Date'].min(), 'to', df['Date'].max())
print('Unique indices:', sorted(df['Index'].unique()))
print('First few rows:')
print(df.head())

# Save processed data for next steps
__RESULT__ = json.dumps({'status': 'success', 'records': len(df), 'indices': sorted(df['Index'].unique())})"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:6': ['index_trade'], 'var_functions.query_db:8': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:10': [{'Index': '000001.SS', 'min(Date)': '2000-01-04 00:00:00', 'max(Date)': 'September 30, 2015 at 12:00 AM', 'day_count': '4354'}, {'Index': '399001.SZ', 'min(Date)': '2000-01-05 00:00:00', 'max(Date)': 'September 30, 2015 at 12:00 AM', 'day_count': '4355'}, {'Index': 'GDAXI', 'min(Date)': '2000-01-05 00:00:00', 'max(Date)': 'September 30, 2016 at 12:00 AM', 'day_count': '5590'}, {'Index': 'GSPTSE', 'min(Date)': '2000-01-05 00:00:00', 'max(Date)': 'September 30, 2016 at 12:00 AM', 'day_count': '6506'}, {'Index': 'HSI', 'min(Date)': '2000-01-14 00:00:00', 'max(Date)': 'September 30, 2019 at 12:00 AM', 'day_count': '5604'}, {'Index': 'IXIC', 'min(Date)': '2000-01-06 00:00:00', 'max(Date)': 'September 30, 2015 at 12:00 AM', 'day_count': '7351'}, {'Index': 'J203.JO', 'min(Date)': '2012-02-08 00:00:00', 'max(Date)': 'September 30, 2019 at 12:00 AM', 'day_count': '1854'}, {'Index': 'N100', 'min(Date)': '2000-01-10 00:00:00', 'max(Date)': 'September 30, 2019 at 12:00 AM', 'day_count': '4245'}, {'Index': 'N225', 'min(Date)': '2000-01-04 00:00:00', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'day_count': '7979'}, {'Index': 'NSEI', 'min(Date)': '2007-09-25 00:00:00', 'max(Date)': 'September 30, 2014 at 12:00 AM', 'day_count': '2577'}, {'Index': 'NYA', 'min(Date)': '2000-01-03 00:00:00', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'day_count': '7960'}, {'Index': 'SSMI', 'min(Date)': '2000-01-05 00:00:00', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'day_count': '5188'}, {'Index': 'TWII', 'min(Date)': '2000-01-17 00:00:00', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'day_count': '4385'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:34': [{'Index': '000001.SS', 'record_count': '4354'}, {'Index': '399001.SZ', 'record_count': '4355'}, {'Index': 'GDAXI', 'record_count': '5590'}, {'Index': 'GSPTSE', 'record_count': '6506'}, {'Index': 'HSI', 'record_count': '5604'}, {'Index': 'IXIC', 'record_count': '7351'}, {'Index': 'J203.JO', 'record_count': '1854'}, {'Index': 'N100', 'record_count': '4245'}, {'Index': 'N225', 'record_count': '7979'}, {'Index': 'NSEI', 'record_count': '2577'}, {'Index': 'NYA', 'record_count': '7960'}, {'Index': 'SSMI', 'record_count': '5188'}, {'Index': 'TWII', 'record_count': '4385'}], 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
