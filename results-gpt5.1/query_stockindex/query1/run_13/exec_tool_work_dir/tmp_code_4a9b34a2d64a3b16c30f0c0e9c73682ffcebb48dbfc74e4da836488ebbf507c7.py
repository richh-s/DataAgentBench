code = """import json, pandas as pd
from datetime import datetime

# load full index_trade data from file
path = var_call_mRIU3VHE8C5Jp8DAGTeBm7K7
with open(path, 'r') as f:
    trade = json.load(f)

df = pd.DataFrame(trade)

# ensure numeric
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# parse date and filter since 2020-01-01
# Date formats are messy; let pandas infer
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

cutoff = pd.Timestamp('2020-01-01')
df = df[df['Date'] >= cutoff].copy()

# compute intraday volatility
df['vol'] = (df['High'] - df['Low']) / df['Open']

# drop rows with missing values
df = df.dropna(subset=['vol'])

# map Asian indices based on symbols
asia_indices = {
    'N225': 'Tokyo Stock Exchange',
    'HSI': 'Hong Kong Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    '^NSEI': 'National Stock Exchange of India',
    'KS11': 'Korea Exchange',
    '^TWII': 'Taiwan Stock Exchange'
}

asia_df = df[df['Index'].isin(asia_indices.keys())].copy()

# average intraday volatility per index
result = asia_df.groupby('Index')['vol'].mean().sort_values(ascending=False)

best_index = result.index[0]
best_vol = float(result.iloc[0])

answer = {
    'best_index': best_index,
    'average_intraday_volatility': best_vol,
    'region': 'Asia'
}

out = json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_UkOuK1TuxyXGisJfCF0AXAyy': ['index_info'], 'var_call_Kwgfo3zhzQ6QDNsipmCYT0oz': ['index_trade'], 'var_call_vTaBCs07u1LquwvISWeCVMUw': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_mRIU3VHE8C5Jp8DAGTeBm7K7': 'file_storage/call_mRIU3VHE8C5Jp8DAGTeBm7K7.json'}

exec(code, env_args)
