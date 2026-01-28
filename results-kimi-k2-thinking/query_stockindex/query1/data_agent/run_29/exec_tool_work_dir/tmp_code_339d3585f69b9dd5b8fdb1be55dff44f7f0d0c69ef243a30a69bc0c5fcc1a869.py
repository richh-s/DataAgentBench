code = """import json
import pandas as pd
from datetime import datetime

# Load the data from the file
file_path = locals()['var_functions.query_db:6']
with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Create DataFrame and convert data types
df = pd.DataFrame(trade_data)
df['Date'] = pd.to_datetime(df['Date']).dt.date
df['Open'] = pd.to_numeric(df['Open'])
df['High'] = pd.to_numeric(df['High'])
df['Low'] = pd.to_numeric(df['Low'])

# Filter for Asian indices
asian_indices = ['000001.SS', '399001.SZ', 'HSI', 'N225', 'NSEI', 'TWII']
df_asia = df[df['Index'].isin(asian_indices)].copy()

# Calculate intraday volatility for each day: (High - Low) / Open
df_asia['intraday_volatility'] = (df_asia['High'] - df_asia['Low']) / df_asia['Open']

# Calculate average intraday volatility per index since 2020
avg_volatility = df_asia.groupby('Index')['intraday_volatility'].mean().reset_index()
avg_volatility = avg_volatility.sort_values('intraday_volatility', ascending=False)

print('__RESULT__:')
print(avg_volatility.to_json(orient='records'))"""

env_args = {'var_functions.query_db:0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII'], 'var_functions.execute_python:16': [{'Index': '000001.SS', 'Date': '2020-01-08 00:00:00', 'Open': '3094.239014', 'High': '3094.239014', 'Low': '3059.131104', 'Close': '3066.893066'}, {'Index': '000001.SS', 'Date': '2020-01-10 00:00:00', 'Open': '3102.293945', 'High': '3105.225098', 'Low': '3081.395996', 'Close': '3092.291016'}, {'Index': '000001.SS', 'Date': '2020-01-15 00:00:00', 'Open': '3103.169922', 'High': '3107.939941', 'Low': '3082.040039', 'Close': '3090.040039'}, {'Index': '000001.SS', 'Date': '2020-02-03 00:00:00', 'Open': '2716.697998', 'High': '2766.576904', 'Low': '2716.697998', 'Close': '2746.605957'}, {'Index': '000001.SS', 'Date': '2020-02-05 00:00:00', 'Open': '2792.371094', 'High': '2842.74292', 'Low': '2778.864014', 'Close': '2818.087891'}]}

exec(code, env_args)
