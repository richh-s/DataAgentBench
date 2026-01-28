code = """import json
import pandas as pd

# Load the data
with open(var_functions.query_db:12, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Convert string values to float
df['Open'] = pd.to_numeric(df['Open'])
df['High'] = pd.to_numeric(df['High'])
df['Low'] = pd.to_numeric(df['Low'])

# Filter out any rows where Open is 0 to avoid division by zero
df = df[df['Open'] != 0]

# Calculate intraday volatility for each day
df['Intraday_Volatility'] = (df['High'] - df['Low']) / df['Open']

# Calculate average intraday volatility for each index
avg_volatility = df.groupby('Index')['Intraday_Volatility'].agg(['mean', 'count']).reset_index()
avg_volatility = avg_volatility.sort_values('mean', ascending=False)

print("__RESULT__:")
print(avg_volatility.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:9': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.execute_python:10': ['N225', 'HSI', '000001.SS', '399001.SZ', 'NSEI', 'TWII'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
