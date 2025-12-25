code = """import json, pandas as pd
from datetime import datetime

# Load the large trade file
path = var_call_4PkVc2XLg0Ho455rjf67tdb8
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Keep only rows from 2020-01-01 onward (Date field is messy strings)
# First, normalize dates by trying multiple formats
formats = ['%Y-%m-%d', '%d %b %Y, %H:%M', '%B %d, %Y at %I:%M %p']

def parse_date(s):
    for fmt in formats:
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            continue
    return None

df['parsed_date'] = df['Date'].apply(parse_date)

mask = df['parsed_date'].notna() & (df['parsed_date'] >= datetime(2020,1,1))
df = df[mask]

# Cast numeric columns
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Compute intraday volatility
df['vol'] = (df['High'] - df['Low']) / df['Open']

# Map indices to regions (Asia vs others)
index_to_region = {
    'N225': 'Asia',        # Tokyo Stock Exchange, Japan
    'HSI': 'Asia',         # Hong Kong Stock Exchange, Hong Kong
    '000001.SS': 'Asia',   # Shanghai Stock Exchange, China
    '399001.SZ': 'Asia',   # Shenzhen Stock Exchange, China
    'NSEI': 'Asia',        # National Stock Exchange of India, India
    'KOSPI': 'Asia',       # Korea Exchange (if present)
    'TWII': 'Asia',        # Taiwan Stock Exchange, Taiwan
}

# Filter to Asia indices only
df_asia = df[df['Index'].isin(index_to_region.keys())].copy()

result = {}
if not df_asia.empty:
    grp = df_asia.groupby('Index')['vol'].mean().sort_values(ascending=False)
    result = {"index_with_highest_avg_intraday_vol_since_2020_in_asia": grp.index[0],
              "average_intraday_volatility": float(grp.iloc[0])}
else:
    result = {"error": "No Asia-region index data found since 2020 in the dataset."}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_AGxjG4jgWLCzpmCcxs6pqUGc': ['index_info'], 'var_call_J7qZGMek1JdhnDZBbfqMzfLl': ['index_trade'], 'var_call_AQsp5U0jhFFrU3dZXetEhWZB': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_TAyb4ZKsKXDQrI3o4fOHGGmt': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'J203.JO'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_call_4PkVc2XLg0Ho455rjf67tdb8': 'file_storage/call_4PkVc2XLg0Ho455rjf67tdb8.json'}

exec(code, env_args)
