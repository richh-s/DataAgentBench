code = """import pandas as pd
import json
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Load the trade data file
trade_data_file = locals()['var_functions.query_db:8']
with open(trade_data_file, 'r') as f:
    trade_data = json.load(f)

# Create DataFrame
df = pd.DataFrame(trade_data)

# Convert string values to float for price columns
numeric_cols = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'CloseUSD']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col])

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter data from 2000 onward
df_filtered = df[df['Date'] >= pd.Timestamp('2000-01-01')].copy()

# Add YearMonth column for monthly grouping
df_filtered['YearMonth'] = df_filtered['Date'].dt.to_period('M')

# For each index, get the last trading day of each month's CloseUSD value
monthly_prices = df_filtered.groupby(['Index', 'YearMonth']).apply(
    lambda x: x.loc[x['Date'].idxmax(), ['Date', 'CloseUSD']]
).reset_index()

# Convert YearMonth to string for easier handling
monthly_prices['YearMonth_str'] = monthly_prices['YearMonth'].astype(str)

print('__RESULT__:')
print(monthly_prices.head(10).to_json(orient='records', date_format='iso'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': [{'Index': '000001.SS', 'First_Date': '2000-01-04T00:00:00.000', 'Last_Date': '2021-05-31T00:00:00.000', 'Trading_Days': 1710}, {'Index': '399001.SZ', 'First_Date': '2000-01-05T00:00:00.000', 'Last_Date': '2021-06-02T00:00:00.000', 'Trading_Days': 1758}, {'Index': 'GDAXI', 'First_Date': '2000-01-05T00:00:00.000', 'Last_Date': '2021-05-31T00:00:00.000', 'Trading_Days': 1833}, {'Index': 'GSPTSE', 'First_Date': '2000-01-05T00:00:00.000', 'Last_Date': '2021-05-13T00:00:00.000', 'Trading_Days': 1802}, {'Index': 'HSI', 'First_Date': '2000-01-14T00:00:00.000', 'Last_Date': '2021-05-24T00:00:00.000', 'Trading_Days': 1706}, {'Index': 'IXIC', 'First_Date': '2000-01-06T00:00:00.000', 'Last_Date': '2021-05-27T00:00:00.000', 'Trading_Days': 1853}, {'Index': 'J203.JO', 'First_Date': '2012-02-08T00:00:00.000', 'Last_Date': '2021-05-28T00:00:00.000', 'Trading_Days': 764}, {'Index': 'N100', 'First_Date': '2000-01-10T00:00:00.000', 'Last_Date': '2021-05-31T00:00:00.000', 'Trading_Days': 1786}, {'Index': 'N225', 'First_Date': '2000-01-04T00:00:00.000', 'Last_Date': '2021-06-01T00:00:00.000', 'Trading_Days': 1730}, {'Index': 'NSEI', 'First_Date': '2007-09-25T00:00:00.000', 'Last_Date': '2021-05-31T00:00:00.000', 'Trading_Days': 1083}, {'Index': 'NYA', 'First_Date': '2000-01-03T00:00:00.000', 'Last_Date': '2021-05-24T00:00:00.000', 'Trading_Days': 1817}, {'Index': 'SSMI', 'First_Date': '2000-01-05T00:00:00.000', 'Last_Date': '2021-05-21T00:00:00.000', 'Trading_Days': 1746}, {'Index': 'TWII', 'First_Date': '2000-01-17T00:00:00.000', 'Last_Date': '2021-05-26T00:00:00.000', 'Trading_Days': 1754}], 'var_functions.execute_python:16': {'000001.SS': 'China', '399001.SZ': 'China', 'GDAXI': 'Germany', 'GSPTSE': 'Canada', 'HSI': 'Hong Kong', 'IXIC': 'United States', 'J203.JO': 'South Africa', 'N100': 'Netherlands', 'N225': 'Japan', 'NSEI': 'India', 'NYA': 'United States', 'SSMI': 'Switzerland', 'TWII': 'Taiwan'}}

exec(code, env_args)
