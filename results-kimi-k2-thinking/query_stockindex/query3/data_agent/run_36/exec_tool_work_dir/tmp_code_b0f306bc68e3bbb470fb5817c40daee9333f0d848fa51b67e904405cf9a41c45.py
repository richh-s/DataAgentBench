code = """import pandas as pd
import json
from datetime import datetime

# Load the trade data file
trade_data_file = locals()['var_functions.query_db:8']
with open(trade_data_file, 'r') as f:
    trade_data = json.load(f)

# Create DataFrame
df = pd.DataFrame(trade_data)

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Convert string values to float for price columns
numeric_cols = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'CloseUSD']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col])

# Filter data from 2000 onward
df_filtered = df[df['Date'] >= '2000-01-01'].copy()

# Get unique indices and their date ranges
indices_info = df_filtered.groupby('Index').agg({
    'Date': ['min', 'max', 'count']
}).round(2)

indices_info.columns = ['First_Date', 'Last_Date', 'Trading_Days']
indices_info = indices_info.reset_index()

print('__RESULT__:')
print(indices_info.to_json(orient='records', date_format='iso'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
