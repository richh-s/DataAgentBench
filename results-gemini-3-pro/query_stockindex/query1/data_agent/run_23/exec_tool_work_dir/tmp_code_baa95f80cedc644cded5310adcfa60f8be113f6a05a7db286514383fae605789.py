code = """import json
import pandas as pd
from dateutil import parser

# Load data
with open(locals()['var_function-call-3472490481901833526'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert numeric columns
cols = ['Open', 'High', 'Low']
for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse dates
# Given the inconsistent format, dateutil.parser.parse is best, but might be slow for many rows.
# However, pandas to_datetime with errors='coerce' and infer_datetime_format might work or apply parser.
# Let's try pandas to_datetime first, it handles many formats. 
# If it fails, I'll use dateutil.
# Actually, the mixed format is tricky. Let's use a custom apply with dateutil if the dataset isn't huge.
# The dataset has ~45k rows? It might be slow but acceptable.
# Let's check size first.
print(f"Data size: {len(df)}")

def parse_date(date_str):
    try:
        return parser.parse(date_str)
    except:
        return pd.NaT

# Only parse if not already datetime (it's string from JSON)
df['Date_dt'] = df['Date'].apply(parse_date)

# Filter since 2020
df_since_2020 = df[df['Date_dt'] >= pd.Timestamp('2020-01-01')]

# Calculate Volatility
# (High - Low) / Open
df_since_2020['Volatility'] = (df_since_2020['High'] - df_since_2020['Low']) / df_since_2020['Open']

# Group by Index and average
result = df_since_2020.groupby('Index')['Volatility'].mean().sort_values(ascending=False)

print("__RESULT__:")
print(result.to_json())"""

env_args = {'var_function-call-5450972752404765470': ['index_info'], 'var_function-call-5450972752404765995': ['index_trade'], 'var_function-call-6627325827496991276': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-6627325827496991081': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-4940300357266615165': [{'Date': '31 Dec 1986, 00:00'}], 'var_function-call-3472490481901833526': 'file_storage/function-call-3472490481901833526.json'}

exec(code, env_args)
