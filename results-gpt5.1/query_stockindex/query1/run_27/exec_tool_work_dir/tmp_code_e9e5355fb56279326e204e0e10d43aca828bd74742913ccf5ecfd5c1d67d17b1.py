code = """import json, pandas as pd
from datetime import datetime

# load full trade data
path = var_call_o5edDyDiYCT4ZqdgavzgX9iP
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# coerce numeric
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# parse dates with mixed formats
def parse_date(s):
    for fmt in ['%Y-%m-%d','%d %b %Y, %H:%M','%B %d, %Y at %I:%M %p']:
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            continue
    return pd.NaT

df['Date_parsed'] = df['Date'].apply(parse_date)

# filter since 2020-01-01
cut = pd.Timestamp('2020-01-01')
df = df[df['Date_parsed'] >= cut]

# compute intraday volatility
df['vol'] = (df['High'] - df['Low']) / df['Open']
df = df.dropna(subset=['vol'])

# map Asian indices based on knowledge
asia_indices = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'SSEC': 'China',
    'SZI': 'China',
    'KS11': 'South Korea',
    'TWII': 'Taiwan',
    '^BSESN': 'India',
    'NSEI': 'India'
}

asia_df = df[df['Index'].isin(asia_indices.keys())].copy()

res = asia_df.groupby('Index')['vol'].mean().sort_values(ascending=False)

result = {"ordered_indices": res.index.tolist(), "avg_vol": res.values.tolist()}

import json as _j
out = _j.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_5viG8INyxGsd1O10FKwNkLOW': ['index_info'], 'var_call_jriIZqtAUDtIbLOlUXS2dVlK': ['index_trade'], 'var_call_PvILLB2W40kiwW4zr9Qq5jUV': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_o5edDyDiYCT4ZqdgavzgX9iP': 'file_storage/call_o5edDyDiYCT4ZqdgavzgX9iP.json'}

exec(code, env_args)
