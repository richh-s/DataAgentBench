code = """import json
import pandas as pd
from datetime import datetime

# Read the full result from the file
with open(var_functions.query_db_14, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert date strings to datetime objects
def parse_date(date_str):
    try:
        # Try different date formats
        if ',' in date_str:
            return datetime.strptime(date_str, '%d %b %Y, %H:%M')
        elif 'at' in date_str:
            return datetime.strptime(date_str, '%B %d, %Y at %I:%M %p')
        else:
            return pd.to_datetime(date_str, errors='coerce')
    except:
        return pd.to_datetime(date_str, errors='coerce')

df['Date'] = df['Date'].apply(parse_date)

# Filter for dates since 2020
df_2020 = df[df['Date'] >= '2020-01-01'].copy()

# Calculate intraday volatility: (High - Low) / Open
df_2020['Open'] = pd.to_numeric(df_2020['Open'], errors='coerce')
df_2020['High'] = pd.to_numeric(df_2020['High'], errors='coerce')
df_2020['Low'] = pd.to_numeric(df_2020['Low'], errors='coerce')

df_2020['Intraday_Volatility'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

# Group by index and calculate average intraday volatility
avg_volatility = df_2020.groupby('Index')['Intraday_Volatility'].mean().reset_index()

# Sort by average volatility descending
avg_volatility = avg_volatility.sort_values('Intraday_Volatility', ascending=False)

print('__RESULT__:')
print(avg_volatility.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.execute_python:12': {'asia_indices': ['HSI', '000001.SS', 'N225', '399001.SZ', 'NSEI', 'TWII']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
