code = """import json, pandas as pd
from datetime import datetime

# load full trade data from file
file_path = var_call_3rNMO0Tou1xiw6XrDMKHWbcD
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# keep only rows from 2020-01-01 onwards; parse dates robustly
# some dates have different string formats, so use errors='coerce'
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce')
cutoff = pd.Timestamp('2020-01-01')
df = df[df['Date_parsed'] >= cutoff].copy()

# convert price columns to float
for col in ['Open', 'High', 'Low', 'Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# compute intraday volatility (High-Low)/Open, avoid divide by zero
df['intraday_vol'] = (df['High'] - df['Low']) / df['Open']

# map indices to regions using knowledge
region_map = {
    'N225': 'Asia',          # Nikkei 225 - Tokyo
    'HSI': 'Asia',           # Hang Seng - Hong Kong
    '000001.SS': 'Asia',     # SSE Composite - Shanghai
    '399001.SZ': 'Asia',     # SZSE Component - Shenzhen
    'NSEI': 'Asia',          # Nifty 50 - India
    'TWII': 'Asia',          # TAIEX - Taiwan
    'GDAXI': 'Europe',
    'N100': 'Europe',
    'SSMI': 'Europe',
    'GSPTSE': 'North America',
    'IXIC': 'North America',
    'NYA': 'North America',
    'J203.JO': 'Africa'
}

df['Region'] = df['Index'].map(region_map)

# filter to Asia region only
asia_df = df[df['Region'] == 'Asia'].copy()

# drop rows with missing intraday_vol
asia_df = asia_df.dropna(subset=['intraday_vol'])

# compute average intraday volatility per index
result = asia_df.groupby('Index')['intraday_vol'].mean().sort_values(ascending=False)

# prepare a concise answer: highest avg volatility index and its value
if not result.empty:
    top_index = result.index[0]
    top_vol = float(result.iloc[0])
    output = {
        'highest_vol_index_asia_since_2020': top_index,
        'average_intraday_volatility': top_vol,
        'unit': 'dimensionless (average of (High-Low)/Open per day)'
    }
else:
    output = {'error': 'No data for Asia region since 2020'}

out_str = json.dumps(output)
print('__RESULT__:')
print(out_str)"""

env_args = {'var_call_g55VLarFzo60jPNVLYkT2fHd': ['index_info'], 'var_call_UziIylZHMWBvvGxwZzI1fQh6': ['index_trade'], 'var_call_edOQam7MePrylzpETJYfcval': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_5LFAd7wTzXFUhqkPINYEmvGR': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}, {'Index': 'NYA'}], 'var_call_3rNMO0Tou1xiw6XrDMKHWbcD': 'file_storage/call_3rNMO0Tou1xiw6XrDMKHWbcD.json'}

exec(code, env_args)
