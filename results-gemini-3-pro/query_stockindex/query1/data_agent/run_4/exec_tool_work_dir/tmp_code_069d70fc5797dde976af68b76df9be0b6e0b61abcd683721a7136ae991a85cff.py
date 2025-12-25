code = """import json
import pandas as pd
from dateutil import parser
import datetime

# Load the file path from the variable
file_path = locals()['var_function-call-7317204134736203706']

# Read the JSON file
with open(file_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert columns to numeric, coercing errors
cols = ['Open', 'High', 'Low']
for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with NaN in price columns
df = df.dropna(subset=cols)

# Parse dates
# Since formats are mixed, we can try using dateutil parser or pandas mixed format
# pd.to_datetime with format='mixed' is available in newer pandas, 
# but let's try a safer apply with parser.parse if to_datetime fails or just apply parser.parse
# Given the size (10k+ rows preview, probably 40-50k total), apply might be slow but acceptable.
# Let's try pd.to_datetime first without format, it's usually smart.
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce')

# If many NaT, we might need a custom parser. Let's check.
# Actually, the preview showed "January 02, 1987 at 12:00 AM". pd.to_datetime handles this.
# "31 Dec 1986, 00:00". pd.to_datetime handles this.
# So standard pd.to_datetime should work.

# Filter for >= 2020-01-01
df = df[df['Date_parsed'] >= pd.Timestamp('2020-01-01')]

# Calculate intraday volatility
# (High - Low) / Open
# Filter out Open == 0
df = df[df['Open'] != 0]
df['volatility'] = (df['High'] - df['Low']) / df['Open']

# Group by Index and calculate mean
result = df.groupby('Index')['volatility'].mean().reset_index()
result = result.sort_values(by='volatility', ascending=False)

# Output
print("__RESULT__:")
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-7121374812617314841': ['index_info'], 'var_function-call-7121374812617315646': ['index_trade'], 'var_function-call-5415332971970561668': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}], 'var_function-call-5415332971970560037': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}], 'var_function-call-14120316340986073691': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-14120316340986076838': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-7317204134736203706': 'file_storage/function-call-7317204134736203706.json'}

exec(code, env_args)
