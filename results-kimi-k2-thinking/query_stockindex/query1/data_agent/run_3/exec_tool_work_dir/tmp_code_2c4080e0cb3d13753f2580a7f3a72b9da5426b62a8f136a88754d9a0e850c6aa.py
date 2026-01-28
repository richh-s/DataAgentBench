code = """# Load the actual Asia indices data and analyze it
import json
import pandas as pd
import numpy as np

# Load data directly
with open('file_storage/functions.query_db:46.json', 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Convert numeric columns
for col in ['Open', 'High', 'Low', 'Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse dates more carefully
time_strings = df['Date'].astype(str)
dates = []
for date_str in time_strings:
    if ' at ' in date_str:
        date_part = date_str.split(' at ')[0]
    else:
        date_part = date_str.split(',')[0]
    
    try:
        date_obj = pd.to_datetime(date_part, dayfirst=True)
    except:
        date_obj = pd.NaT
    dates.append(date_obj)

df['Date_parsed'] = dates

# Filter for 2020+
mask_2020 = df['Date_parsed'] >= pd.Timestamp('2020-01-01')
df_2020 = df[mask_2020].copy()

# Identify Asia indices and calculate volatility
asia_indices = ['N225', 'HSI', 'NSEI', '000001.SS', 'TWII', '399001.SZ']
df_asia = df_2020[df_2020['Index'].isin(asia_indices)].copy()

# Calculate intraday volatility
df_asia['Intraday_Volatility'] = (df_asia['High'] - df_asia['Low']) / df_asia['Open']

# Clean invalid values
df_asia = df_asia[df_asia['Intraday_Volatility'].notna()]
df_asia = df_asia[np.isfinite(df_asia['Intraday_Volatility'])]

# Calculate average volatility per index
volatility_by_index = df_asia.groupby('Index')['Intraday_Volatility'].mean().sort_values(ascending=False)

print("__RESULT__:")
print(volatility_by_index.to_json())"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': 'Loaded 48151 records', 'var_functions.execute_python:16': {'records': 100, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'indices': ['HSI']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'total_records': 0, 'unique_indices': 0, 'asia_indices_count': 0, 'indices_sample': [], 'asia_indices': []}, 'var_functions.execute_python:26': {'records': 100, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'index_sample': ['HSI'], 'date_sample': ['31 Dec 1986, 00:00', 'January 02, 1987 at 12:00 AM', 'January 15, 1987 at 12:00 AM', 'January 16, 1987 at 12:00 AM', 'January 19, 1987 at 12:00 AM'], 'date_sample_end': ['October 19, 1987 at 12:00 AM', '26 Oct 1987, 00:00', 'October 27, 1987 at 12:00 AM', '28 Oct 1987, 00:00', '29 Oct 1987, 00:00']}, 'var_functions.execute_python:30': {'error': 'Could not load variables'}, 'var_functions.query_db:32': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:38': [{'Index': 'N225', 'count': '13874'}, {'Index': 'GSPTSE', 'count': '10526'}, {'Index': 'NSEI', 'count': '3346'}, {'Index': 'GDAXI', 'count': '8438'}, {'Index': 'J203.JO', 'count': '2346'}, {'Index': 'IXIC', 'count': '12690'}, {'Index': 'HSI', 'count': '8492'}, {'Index': '000001.SS', 'count': '5791'}, {'Index': 'SSMI', 'count': '7671'}, {'Index': 'TWII', 'count': '5869'}, {'Index': 'NYA', 'count': '13947'}, {'Index': 'N100', 'count': '5474'}, {'Index': '399001.SZ', 'count': '5760'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.execute_python:44': {'file_path': 'file_storage/functions.query_db:2.json', 'records': 100}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
