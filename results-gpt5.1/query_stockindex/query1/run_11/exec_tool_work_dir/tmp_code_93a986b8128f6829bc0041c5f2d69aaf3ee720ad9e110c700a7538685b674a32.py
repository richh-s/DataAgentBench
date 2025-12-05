code = """import json, pandas as pd
from datetime import datetime

# Load full large result from file
file_path = var_call_tT3hXZeqHdLoLIYX2Ebpdqq9
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure numeric
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse dates heuristically then filter since 2020-01-01
# First normalize "Date" using pandas to_datetime with dayfirst and infer
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce', dayfirst=True, infer_datetime_format=True)

cutoff = pd.Timestamp('2020-01-01')
mask = df['Date_parsed'] >= cutoff

# Compute intraday volatility
df_filt = df[mask].copy()

df_filt['vol'] = (df_filt['High'] - df_filt['Low']) / df_filt['Open']

res = df_filt.groupby('Index')['vol'].mean().sort_values(ascending=False)

result = res.to_dict()

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_tfS730ddLFQtLSTTxY3LLOKd': ['index_info'], 'var_call_SLcBV24HGoKKLeQ08IsbDxPg': ['index_trade'], 'var_call_gm1JIHvNSemAHzH7wR7LbmQ3': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_XtJdNM96jpRQUuNbrO3DayWP': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'HSI'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_tT3hXZeqHdLoLIYX2Ebpdqq9': 'file_storage/call_tT3hXZeqHdLoLIYX2Ebpdqq9.json'}

exec(code, env_args)
