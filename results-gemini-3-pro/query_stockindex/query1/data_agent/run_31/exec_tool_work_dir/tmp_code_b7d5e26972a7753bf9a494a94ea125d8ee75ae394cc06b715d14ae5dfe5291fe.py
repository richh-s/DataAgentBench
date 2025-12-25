code = """import pandas as pd
import json
import os
from datetime import datetime

# Load data
file_path = locals()['var_function-call-677703264432954975']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert columns to numeric
for col in ['Open', 'High', 'Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with NaN in numeric columns or Open == 0
df = df.dropna(subset=['Open', 'High', 'Low'])
df = df[df['Open'] != 0]

# Parse dates
# We have mixed formats. pd.to_datetime can handle many, but let's try to be robust.
# Formats seen: 
# 1. 31 Dec 1986, 00:00
# 2. January 02, 1987 at 12:00 AM
# 3. 1987-01-05 00:00:00

def parse_date(date_str):
    try:
        return pd.to_datetime(date_str)
    except:
        return pd.NaT

# pd.to_datetime usually handles mixed formats by default quite well if we don't specify format.
# However, "January 02, 1987 at 12:00 AM" might be tricky for the default parser depending on the version.
# Let's clean the " at 12:00 AM" part if present to make it easier, or just let pandas try.
# Actually, the format "January 02, 1987 at 12:00 AM" is reasonably standard for US locale.

df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter for >= 2020-01-01
df = df[df['Date_parsed'] >= '2020-01-01']

# Calculate Volatility
df['Volatility'] = (df['High'] - df['Low']) / df['Open']

# Group by Index and average
result = df.groupby('Index')['Volatility'].mean().sort_values(ascending=False)

print("__RESULT__:")
print(result.to_json())"""

env_args = {'var_function-call-7889717879193856720': ['index_info'], 'var_function-call-7889717879193856883': ['index_trade'], 'var_function-call-12037778265510678070': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_function-call-10885150610954781749': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-2728149395629616103': [{'Date': '31 Dec 1986, 00:00'}], 'var_function-call-4100812765947977826': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00'}, {'Index': 'HSI', 'Date': '1987-01-08 00:00:00'}, {'Index': 'HSI', 'Date': '1987-01-09 00:00:00'}, {'Index': 'HSI', 'Date': '1987-01-12 00:00:00'}, {'Index': 'HSI', 'Date': '1987-01-13 00:00:00'}, {'Index': 'HSI', 'Date': '1987-01-14 00:00:00'}, {'Index': 'HSI', 'Date': 'January 15, 1987 at 12:00 AM'}, {'Index': 'HSI', 'Date': 'January 16, 1987 at 12:00 AM'}, {'Index': 'HSI', 'Date': 'January 19, 1987 at 12:00 AM'}, {'Index': 'HSI', 'Date': '20 Jan 1987, 00:00'}, {'Index': 'HSI', 'Date': 'January 21, 1987 at 12:00 AM'}, {'Index': 'HSI', 'Date': '22 Jan 1987, 00:00'}, {'Index': 'HSI', 'Date': 'January 23, 1987 at 12:00 AM'}, {'Index': 'HSI', 'Date': 'January 26, 1987 at 12:00 AM'}, {'Index': 'HSI', 'Date': '27 Jan 1987, 00:00'}, {'Index': 'HSI', 'Date': 'January 28, 1987 at 12:00 AM'}], 'var_function-call-16002337889460237317': [{'count_star()': '43132'}], 'var_function-call-677703264432954975': 'file_storage/function-call-677703264432954975.json'}

exec(code, env_args)
