code = """import json
import pandas as pd
import numpy as np

# Load data
with open(locals()['var_function-call-8952406571807986639'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert columns to numeric
cols = ['Open', 'High', 'Low']
for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse dates
# Attempt to parse with mixed format
try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')
except ValueError:
    # Fallback if format='mixed' is not supported in installed pandas version
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter for date >= 2020-01-01
df = df[df['Date'] >= '2020-01-01']

# Filter out Open = 0 to avoid division by zero
df = df[df['Open'] > 0]

# Calculate Intraday Volatility
df['Volatility'] = (df['High'] - df['Low']) / df['Open']

# Calculate average volatility per index
result = df.groupby('Index')['Volatility'].mean().sort_values(ascending=False)

print("__RESULT__:")
print(result.to_json())"""

env_args = {'var_function-call-4424860790471531299': ['index_info'], 'var_function-call-4424860790471530630': ['index_trade'], 'var_function-call-4471314797337986561': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-4471314797337985712': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_function-call-15118583615275931984': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}], 'var_function-call-6588912966158541438': [{'count_star()': '43132'}], 'var_function-call-8952406571807986639': 'file_storage/function-call-8952406571807986639.json'}

exec(code, env_args)
