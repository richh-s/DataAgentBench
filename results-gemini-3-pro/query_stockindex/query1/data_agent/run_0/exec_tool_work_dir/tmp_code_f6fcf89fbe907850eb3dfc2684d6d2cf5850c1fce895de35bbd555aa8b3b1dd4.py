code = """import pandas as pd
import json

# Load data
file_path = locals()['var_function-call-4501430723657214772']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates
# Using pd.to_datetime which is robust
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter for dates >= 2020-01-01
df_filtered = df[df['Date'] >= '2020-01-01'].copy()

# Ensure numeric columns
cols = ['Open', 'High', 'Low']
for col in cols:
    df_filtered[col] = pd.to_numeric(df_filtered[col], errors='coerce')

# Drop invalid rows
df_filtered = df_filtered.dropna(subset=cols)
df_filtered = df_filtered[df_filtered['Open'] > 0]

# Calculate Intraday Volatility
df_filtered['Volatility'] = (df_filtered['High'] - df_filtered['Low']) / df_filtered['Open']

# Calculate Average Volatility by Index
avg_vol = df_filtered.groupby('Index')['Volatility'].mean()

# Find the highest
max_vol_index = avg_vol.idxmax()
max_vol_value = avg_vol.max()

result = {
    'average_volatility_by_index': avg_vol.to_dict(),
    'highest_volatility_index': max_vol_index,
    'highest_volatility_value': max_vol_value
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3882960767731712469': ['index_info'], 'var_function-call-3882960767731713472': ['index_trade'], 'var_function-call-1937197001609186129': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-1937197001609183336': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-6484972356659648397': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}], 'var_function-call-4501430723657214772': 'file_storage/function-call-4501430723657214772.json'}

exec(code, env_args)
