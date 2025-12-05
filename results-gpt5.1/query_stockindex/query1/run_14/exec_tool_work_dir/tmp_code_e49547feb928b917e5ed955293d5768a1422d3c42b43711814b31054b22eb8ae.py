code = """import json, pandas as pd
from datetime import datetime

file_path = var_call_GvSOd6LrwWmaoWd5zXyaSohu
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# parse dates robustly, keeping those >= 2020-01-01
parsed_dates = pd.to_datetime(df['Date'], errors='coerce')
mask = parsed_dates >= pd.Timestamp('2020-01-01')
df = df[mask].copy()

# convert price columns to float
for col in ['Open', 'High', 'Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# drop rows with missing needed values or non-positive open
df = df.dropna(subset=['Open','High','Low'])
df = df[df['Open'] > 0]

# intraday volatility
df['intraday_vol'] = (df['High'] - df['Low']) / df['Open']

# aggregate by index
result = df.groupby('Index')['intraday_vol'].mean().sort_values(ascending=False)

# we now must pick Asia-region indices. We'll infer by typical Asian index tickers present.
# Get top 50 by volatility and list them so we can reason outside.
summary = result.head(50).reset_index().to_dict(orient='records')

out = json.dumps(summary)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_WDbaH0IzRX9s2A72JBVlgkLK': ['index_info'], 'var_call_lOYCSESpdcYA59bOxhvM9XFG': ['index_trade'], 'var_call_GvSOd6LrwWmaoWd5zXyaSohu': 'file_storage/call_GvSOd6LrwWmaoWd5zXyaSohu.json'}

exec(code, env_args)
