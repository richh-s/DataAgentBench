code = """import json, pandas as pd
from datetime import datetime

# Load full large result from file
path = var_call_op4OjPUZic8HfIYq85yMsGnx
with open(path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Keep only records from 2020 onwards; Date formats are mixed strings, so parse flexibly
# We'll try multiple date formats; invalid parses become NaT
for fmt in ["%Y-%m-%d", "%d %b %Y, %H:%M", "%B %d, %Y at %I:%M %p"]:
    mask = pd.to_datetime(df['Date'], format=fmt, errors='coerce')
    if 'parsed' not in df:
        df['parsed'] = mask
    else:
        df['parsed'] = df['parsed'].fillna(mask)

df = df[~df['parsed'].isna()]

# Filter to 2020-01-01 and later
df = df[df['parsed'] >= pd.Timestamp('2020-01-01')]

# Convert numeric columns
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna(subset=['Open','High','Low'])

# Compute intraday volatility
df['intraday_vol'] = (df['High'] - df['Low']) / df['Open']

# Map indices to regions via manual knowledge
asia_indices = {
    'HSI': 'Hong Kong Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange',
    'N225': 'Tokyo Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    'TWII': 'Taiwan Stock Exchange',
    'NSEI': 'National Stock Exchange of India',
    'KS11': 'Korea Exchange'
}

# Keep only Asia indices present in data
df_asia = df[df['Index'].isin(asia_indices.keys())].copy()

# Compute average intraday volatility per index since 2020
avg_vol = df_asia.groupby('Index')['intraday_vol'].mean().reset_index()

# Find index with highest average intraday volatility
if not avg_vol.empty:
    top = avg_vol.sort_values('intraday_vol', ascending=False).iloc[0]
    result = {
        'Index': top['Index'],
        'AverageIntradayVolatility': float(top['intraday_vol'])
    }
else:
    result = {
        'Index': None,
        'AverageIntradayVolatility': None
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_VdcrKMJPVQh4GlmlxguTaXgE': ['index_info'], 'var_call_AiDOXXdOxrYIBWEBTJk8Fo3e': ['index_trade'], 'var_call_r9P9T6bSgmwOlFiTZgncCIuX': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_xOldFhTcdnV5w2KiTJcpQF6P': [{'Index': 'J203.JO'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'IXIC'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}], 'var_call_op4OjPUZic8HfIYq85yMsGnx': 'file_storage/call_op4OjPUZic8HfIYq85yMsGnx.json'}

exec(code, env_args)
