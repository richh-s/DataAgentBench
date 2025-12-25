code = """import pandas as pd
import json
import dateutil.parser

# Load the data
with open(locals()['var_function-call-12945559462189205208'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Function to parse dates
def parse_date(date_str):
    try:
        return pd.to_datetime(date_str)
    except:
        return pd.NaT

# Apply date parsing
# Since formats are mixed, to_datetime might be slow or fail without format='mixed' (if pandas version is old)
# Let's try pd.to_datetime first.
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter for dates >= 2020-01-01
df = df[df['Date'] >= '2020-01-01']

# Calculate Intraday Volatility
# (High - Low) / Open
# Check for Open = 0 to avoid division by zero
df = df[df['Open'] > 0]
df['Volatility'] = (df['High'] - df['Low']) / df['Open']

# Calculate average volatility per index
avg_vol = df.groupby('Index')['Volatility'].mean()

print("__RESULT__:")
print(avg_vol.to_json())"""

env_args = {'var_function-call-18377847100518607785': ['index_info'], 'var_function-call-18377847100518604932': ['index_trade'], 'var_function-call-17249532800429248748': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-17249532800429250121': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}], 'var_function-call-16464408201266803447': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-6482134199211340422': [{'Date': '31 Dec 1986, 00:00'}], 'var_function-call-15208872293743233061': [{'Date': '31 Dec 1986, 00:00', 'parsed_date': '1986-12-31 00:00:00'}], 'var_function-call-12945559462189205208': 'file_storage/function-call-12945559462189205208.json'}

exec(code, env_args)
