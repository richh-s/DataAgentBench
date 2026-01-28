code = """import json
import pandas as pd
from datetime import datetime

# Load the data from the file
file_path = locals()['var_functions.query_db:6']
with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Create DataFrame
df = pd.DataFrame(trade_data)

# Define function to parse dates in different formats
def parse_date(date_str):
    if 'at' in date_str:
        # Format: "September 29, 2003 at 12:00 AM"
        date_part = date_str.split(' at ')[0]
        return pd.to_datetime(date_part, format='%B %d, %Y').date()
    else:
        # Format: "2020-01-08 00:00:00"
        return pd.to_datetime(date_str).date()

# Apply date parsing
df['Date'] = df['Date'].apply(parse_date)

# Convert OHLC to numeric
df['Open'] = pd.to_numeric(df['Open'])
df['High'] = pd.to_numeric(df['High'])
df['Low'] = pd.to_numeric(df['Low'])

# Filter for Asian indices (based on Exchange metadata geography)
asian_indices = ['000001.SS', '399001.SZ', 'HSI', 'N225', 'NSEI', 'TWII', 'J203.JO']
df_asia = df[df['Index'].isin(asian_indices)].copy()

# Calculate intraday volatility for each day: (High - Low) / Open
df_asia['intraday_volatility'] = (df_asia['High'] - df_asia['Low']) / df_asia['Open']

# Calculate average intraday volatility per index since 2020
avg_volatility = df_asia.groupby('Index')['intraday_volatility'].mean().reset_index()
avg_volatility = avg_volatility.sort_values('intraday_volatility', ascending=False)

print('__RESULT__:')
print(avg_volatility.to_json(orient='records', indent=2))"""

env_args = {'var_functions.query_db:0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII'], 'var_functions.execute_python:16': [{'Index': '000001.SS', 'Date': '2020-01-08 00:00:00', 'Open': '3094.239014', 'High': '3094.239014', 'Low': '3059.131104', 'Close': '3066.893066'}, {'Index': '000001.SS', 'Date': '2020-01-10 00:00:00', 'Open': '3102.293945', 'High': '3105.225098', 'Low': '3081.395996', 'Close': '3092.291016'}, {'Index': '000001.SS', 'Date': '2020-01-15 00:00:00', 'Open': '3103.169922', 'High': '3107.939941', 'Low': '3082.040039', 'Close': '3090.040039'}, {'Index': '000001.SS', 'Date': '2020-02-03 00:00:00', 'Open': '2716.697998', 'High': '2766.576904', 'Low': '2716.697998', 'Close': '2746.605957'}, {'Index': '000001.SS', 'Date': '2020-02-05 00:00:00', 'Open': '2792.371094', 'High': '2842.74292', 'Low': '2778.864014', 'Close': '2818.087891'}], 'var_functions.execute_python:22': [{'Index': 'TWII', 'Date': 'September 29, 2003 at 12:00 AM', 'Open': '5645.080078', 'High': '5668.919922', 'Low': '5627.430176', 'Close': '5643.5'}, {'Index': 'TWII', 'Date': 'September 29, 2004 at 12:00 AM', 'Open': '5843.700195', 'High': '5877.080078', 'Low': '5809.75', 'Close': '5809.75'}, {'Index': 'TWII', 'Date': 'September 29, 2009 at 12:00 AM', 'Open': '7385.839844', 'High': '7436.290039', 'Low': '7378.970215', 'Close': '7429.97998'}, {'Index': 'TWII', 'Date': 'September 29, 2020 at 12:00 AM', 'Open': '12488.09961', 'High': '12571.33984', 'Low': '12429.71973', 'Close': '12467.73047'}, {'Index': 'TWII', 'Date': 'September 30, 2003 at 12:00 AM', 'Open': '5672.77002', 'High': '5677.120117', 'Low': '5611.410156', 'Close': '5611.410156'}, {'Index': 'TWII', 'Date': 'September 30, 2004 at 12:00 AM', 'Open': '5864.049805', 'High': '5899.540039', 'Low': '5827.379883', 'Close': '5845.689941'}, {'Index': 'TWII', 'Date': 'September 30, 2005 at 12:00 AM', 'Open': '6053.589844', 'High': '6118.609863', 'Low': '6047.200195', 'Close': '6118.609863'}, {'Index': 'TWII', 'Date': 'September 30, 2011 at 12:00 AM', 'Open': '7222.160156', 'High': '7251.870117', 'Low': '7163.75', 'Close': '7225.379883'}, {'Index': 'TWII', 'Date': 'September 30, 2014 at 12:00 AM', 'Open': '8954.580078', 'High': '8998.830078', 'Low': '8860.169922', 'Close': '8966.919922'}, {'Index': 'TWII', 'Date': 'September 30, 2020 at 12:00 AM', 'Open': '12483.65039', 'High': '12568.67969', 'Low': '12466.58008', 'Close': '12515.61035'}]}

exec(code, env_args)
