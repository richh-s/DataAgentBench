code = """import json
import pandas as pd
import numpy as np

# Load the data
file_path = locals()['var_functions.query_db:34']
df = pd.read_json(file_path)

# Clean and parse dates - multiple formats detected
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter for 2020+ data
start_date = pd.Timestamp('2020-01-01')
df_2020 = df[df['Date'] >= start_date].copy()

# Calculate intraday volatility
# First convert string values to numeric
cols = ['Open', 'High', 'Low']
for col in cols:
    df_2020[col] = pd.to_numeric(df_2020[col], errors='coerce')

# Calculate daily intraday volatility as (High - Low) / Open
df_2020['intraday_volatility'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

# Filter out invalid data (zero or missing open prices)
df_2020 = df_2020[df_2020['Open'] > 0]

# Calculate average volatility for each index
results = {}
for index in df_2020['Index'].unique():
    index_data = df_2020[df_2020['Index'] == index]
    if len(index_data) > 0:
        avg_vol = index_data['intraday_volatility'].mean()
        results[index] = {
            'average_volatility': float(avg_vol),
            'trading_days': int(len(index_data))
        }

# Sort by highest avg volatility
sorted_results = sorted(results.items(), key=lambda x: x[1]['average_volatility'], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'total_records_analyzed': int(len(df)),
    'records_since_2020': int(len(df_2020)),
    'avg_volatilities': dict(sorted_results)
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:9': [{'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}], 'var_functions.query_db:8': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:22': {'total_rows': 20187, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'sample_data': [{'Index': 'HSI', 'Date': '1986-12-31', 'Open': 2568.300049, 'High': 2568.300049, 'Low': 2568.300049, 'Close': 2568.300049}, {'Index': 'HSI', 'Date': '1987-01-02', 'Open': 2540.100098, 'High': 2540.100098, 'Low': 2540.100098, 'Close': 2540.100098}, {'Index': 'HSI', 'Date': '1987-01-15', 'Open': 2559.100098, 'High': 2559.100098, 'Low': 2559.100098, 'Close': 2559.100098}], 'index_counts': {'N225': 6349, 'HSI': 4006, '000001.SS': 2752, 'TWII': 2751, '399001.SZ': 2719, 'NSEI': 1610}}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:32': {'total_rows': 20187, 'date_range': '1965-01-06 00:00:00 to 2021-06-03 00:00:00', 'index_counts': "{'N225': np.int64(6349), 'HSI': np.int64(4006), '000001.SS': np.int64(2752), 'TWII': np.int64(2751), '399001.SZ': np.int64(2719), 'NSEI': np.int64(1610)}", 'missing_dates': 0}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
