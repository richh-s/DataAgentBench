code = """import json
import pandas as pd

# Read the data from the file
with open('/home/user/tmp_data_var_functions.query_db:13.json', 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Convert string values to float
df['Open'] = df['Open'].astype(float)
df['High'] = df['High'].astype(float)
df['Low'] = df['Low'].astype(float)

# Calculate intraday volatility for each day
df['intraday_volatility'] = (df['High'] - df['Low']) / df['Open']

# Group by index and calculate average intraday volatility
avg_volatility = df.groupby('Index')['intraday_volatility'].mean().reset_index()

# Sort by average volatility in descending order
avg_volatility = avg_volatility.sort_values('intraday_volatility', ascending=False)

print('__RESULT__:')
print(avg_volatility.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:1': ['index_trade'], 'var_functions.query_db:4': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:8': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json'}

exec(code, env_args)
