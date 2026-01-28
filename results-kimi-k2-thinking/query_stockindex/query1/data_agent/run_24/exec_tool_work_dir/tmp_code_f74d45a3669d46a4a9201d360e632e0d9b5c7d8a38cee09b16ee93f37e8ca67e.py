code = """import json
import pandas as pd
import numpy as np
from datetime import datetime

# Load trade data from file
trade_data_file = 'file_storage/functions.query_db:6.json'
with open(trade_data_file, 'r') as f:
    trade_data = json.load(f)

# Create DataFrame
df_trade = pd.DataFrame(trade_data)

# Parse dates
def parse_date(date_str):
    if pd.isna(date_str):
        return pd.NaT
    try:
        return pd.to_datetime(date_str, format='%d %b %Y, %H:%M')
    except:
        try:
            return pd.to_datetime(date_str, format='%B %d, %Y at %I:%M %p')
        except:
            return pd.to_datetime(date_str, errors='coerce')

df_trade['Date_parsed'] = df_trade['Date'].apply(parse_date)

# Convert price columns to numeric
df_trade['Open'] = pd.to_numeric(df_trade['Open'], errors='coerce')
df_trade['High'] = pd.to_numeric(df_trade['High'], errors='coerce')
df_trade['Low'] = pd.to_numeric(df_trade['Low'], errors='coerce')

# Filter for 2020 onwards
df_2020 = df_trade[df_trade['Date_parsed'] >= '2020-01-01'].copy()

# Define Asia indices based on geographic knowledge
asia_indices = ['N225', 'HSI', '000001.SS', '399001.SZ', 'NSEI', 'TWII']

# Filter for Asia indices
df_asia = df_2020[df_2020['Index'].isin(asia_indices)].copy()

# Calculate intraday volatility: (High - Low) / Open
df_asia['Intraday_Volatility'] = (df_asia['High'] - df_asia['Low']) / df_asia['Open']

# Group by index and calculate mean volatility
volatility_by_index = df_asia.groupby('Index')['Intraday_Volatility'].mean().reset_index()
volatility_by_index = volatility_by_index.sort_values('Intraday_Volatility', ascending=False)

# For debugging, also get count of days for each index
count_by_index = df_asia.groupby('Index').size().reset_index(name='Day_Count')
volatility_with_count = pd.merge(volatility_by_index, count_by_index, on='Index')

print('__RESULT__:')
print(volatility_with_count.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'info_var': "<class 'list'>", 'trade_indices_var': "<class 'list'>", 'result': "<class 'str'>"}, 'var_functions.execute_python:12': {'file_path_type': "<class 'str'>", 'file_path_value': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:14': {'trade_rows': 48151, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'CloseUSD'], 'sample_dates': ['31 Dec 1986, 00:00', 'January 02, 1987 at 12:00 AM', 'January 15, 1987 at 12:00 AM', 'January 16, 1987 at 12:00 AM', 'January 19, 1987 at 12:00 AM']}, 'var_functions.execute_python:16': {'rows_2020': 3638, 'indices_in_2020': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII'], 'date_range': {'min': '2020-01-02 00:00:00', 'max': '2021-06-03 00:00:00'}}}

exec(code, env_args)
