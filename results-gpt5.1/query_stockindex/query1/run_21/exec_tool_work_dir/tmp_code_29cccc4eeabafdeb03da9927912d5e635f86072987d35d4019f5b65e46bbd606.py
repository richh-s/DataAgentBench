code = """import json, pandas as pd
from datetime import datetime

# load full index_trade data from file
path = var_call_tOrNIGcQXGzIvhsIsrRHM4gG
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# normalize dtypes
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# filter since 2020-01-01 using robust date parsing
def parse_date(x):
    try:
        return pd.to_datetime(x, errors='coerce')
    except Exception:
        return pd.NaT

df['Date_parsed'] = df['Date'].apply(parse_date)
mask = df['Date_parsed'] >= pd.Timestamp('2020-01-01')
df = df[mask].copy()

# compute intraday volatility
df['vol'] = (df['High'] - df['Low']) / df['Open']

# map indices to regions manually for known exchanges
asia_indices = {
    'HSI',          # Hong Kong Stock Exchange
    '000001.SS',    # Shanghai Stock Exchange Composite
    '399001.SZ',    # Shenzhen Component
    'N225',         # Nikkei 225 - Tokyo
    'KS11',         # KOSPI - Korea Exchange
    'TWII',         # TAIEX - Taiwan
    '^BSESN',       # BSE Sensex or could be other; here treat as India
    '^NSEI',        # Nifty 50 India
}

# keep only Asia indices
asia_df = df[df['Index'].isin(asia_indices)].copy()

result = asia_df.groupby('Index')['vol'].mean().sort_values(ascending=False)

best_index = None
best_vol = None
if not result.empty:
    best_index = result.index[0]
    best_vol = float(result.iloc[0])

out = {
    'average_intraday_vol_by_index_asia': {idx: float(v) for idx, v in result.items()},
    'highest_avg_vol_index_asia': best_index,
    'highest_avg_vol_value': best_vol
}

res_str = json.dumps(out)
print("__RESULT__:")
print(res_str)"""

env_args = {'var_call_vC3MP4FR78zvtOy9NyXxTcCn': ['index_info'], 'var_call_zI28XAlmOLYPuAle590zSi36': ['index_trade'], 'var_call_OJ3oLTA9rty3DgFnpMoOj7mj': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_tOrNIGcQXGzIvhsIsrRHM4gG': 'file_storage/call_tOrNIGcQXGzIvhsIsrRHM4gG.json'}

exec(code, env_args)
