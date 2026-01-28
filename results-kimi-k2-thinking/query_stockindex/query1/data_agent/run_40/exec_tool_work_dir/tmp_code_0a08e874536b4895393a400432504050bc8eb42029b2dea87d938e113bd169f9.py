code = """import json
import pandas as pd

# Get the data from storage
key = var_functions.query_db:8

# Handle both file path and direct data cases
if isinstance(key, str) and '.json' in key:
    with open(key, 'r') as f:
        data = json.load(f)
else:
    data = key

# Create DataFrame
df = pd.DataFrame(data)

# Convert to numeric
numeric_cols = ['Open', 'High', 'Low', 'Close']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Calculate intraday volatility
df['Intraday_Volatility'] = (df['High'] - df['Low']) / df['Open']

# Clean data - remove NaN and infinite values
df = df.dropna(subset=['Intraday_Volatility'])
df = df[df['Intraday_Volatility'].notna() & (df['Intraday_Volatility'] != float('inf')) & (df['Intraday_Volatility'] != float('-inf'))]

# Group by Index and calculate average volatility
avg_volatility = df.groupby('Index')['Intraday_Volatility'].mean().reset_index()

# Sort by volatility descending
avg_volatility = avg_volatility.sort_values('Intraday_Volatility', ascending=False)

# Create result
result = avg_volatility.to_dict('records')

# Print in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
