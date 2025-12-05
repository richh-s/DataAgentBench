code = """import json, pandas as pd
from datetime import datetime

# Load full trade data from file
file_path = var_call_YaWWfoW6nMaw3bTBpiOEHc30
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse date column robustly and filter from 2020-01-01
def parse_date(x):
    for fmt in ['%Y-%m-%d', '%d %b %Y, %H:%M', '%B %d, %Y at %I:%M %p']:
        try:
            return datetime.strptime(x, fmt)
        except Exception:
            continue
    return pd.NaT

df['Date_parsed'] = df['Date'].apply(parse_date)
df = df.dropna(subset=['Date_parsed'])
cutoff = datetime(2020,1,1)
df = df[df['Date_parsed'] >= cutoff]

# Convert price columns to float
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Compute intraday volatility (High-Low)/Open
df['vol'] = (df['High'] - df['Low']) / df['Open']

# Map indices to exchanges and regions (hard-coded from hints and general knowledge)
index_to_exchange = {
    'NYA': 'New York Stock Exchange',
    'IXIC': 'NASDAQ',
    'HSI': 'Hong Kong Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    'N225': 'Tokyo Stock Exchange',
    'NSEI': 'National Stock Exchange of India',
    'GSPTSE': 'Toronto Stock Exchange',
    'GDAXI': 'Frankfurt Stock Exchange',
    'N100': 'Euronext',
    'SSMI': 'SIX Swiss Exchange',
    'TWII': 'Taiwan Stock Exchange',
    'J203.JO': 'Johannesburg Stock Exchange'
}

exchange_to_region = {
    'New York Stock Exchange': 'North America',
    'NASDAQ': 'North America',
    'Hong Kong Stock Exchange': 'Asia',
    'Shanghai Stock Exchange': 'Asia',
    'Tokyo Stock Exchange': 'Asia',
    'Euronext': 'Europe',
    'Shenzhen Stock Exchange': 'Asia',
    'Toronto Stock Exchange': 'North America',
    'National Stock Exchange of India': 'Asia',
    'Frankfurt Stock Exchange': 'Europe',
    'Korea Exchange': 'Asia',
    'SIX Swiss Exchange': 'Europe',
    'Taiwan Stock Exchange': 'Asia',
    'Johannesburg Stock Exchange': 'Africa'
}

# Keep only indices we have in mapping
df = df[df['Index'].isin(index_to_exchange.keys())]

df['Exchange'] = df['Index'].map(index_to_exchange)
df['Region'] = df['Exchange'].map(exchange_to_region)

# Filter to Asia region
asia_df = df[df['Region'] == 'Asia']

# Compute average intraday volatility per index since 2020
result = asia_df.groupby('Index')['vol'].mean().sort_values(ascending=False)

top_index = None
top_vol = None
if not result.empty:
    top_index = result.index[0]
    top_vol = float(result.iloc[0])

output = {
    'asia_index_avg_vol': {idx: float(v) for idx, v in result.items()},
    'top_index': top_index,
    'top_avg_vol': top_vol
}

out_str = json.dumps(output)
print("__RESULT__:")
print(out_str)"""

env_args = {'var_call_30G9SeiUDvYpjOHr11orV1LB': ['index_info'], 'var_call_zaUcAtmBZ59v2BHziTZ4iv2O': ['index_trade'], 'var_call_a6nGeOLYAXJD17WvwE1aNibw': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_HlsGqclpMNPhAstzZugr0l33': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'IXIC'}], 'var_call_YaWWfoW6nMaw3bTBpiOEHc30': 'file_storage/call_YaWWfoW6nMaw3bTBpiOEHc30.json'}

exec(code, env_args)
