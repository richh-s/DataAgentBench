code = """import json, pandas as pd
from datetime import datetime

path = var_call_2dIYsGu3z6gkQun3PKxfVrFN
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# parse date in a forgiving way and filter since 2020-01-01
from dateutil import parser

def parse_date(x):
    try:
        return parser.parse(x)
    except Exception:
        return pd.NaT

# dateutil isn't available; fall back to pandas to_datetime with errors='coerce'
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)
mask = df['Date'] >= pd.Timestamp('2020-01-01')
df = df[mask]

# compute intraday volatility
valid = (df['Open'] > 0) & df['High'].notna() & df['Low'].notna()
df = df[valid].copy()
df['intraday_vol'] = (df['High'] - df['Low']) / df['Open']

# Map indices to regions using knowledge; focus on Asia
asia_indices = {
    'N225','HSI','000001.SS','399001.SZ','399006.SZ','^STI','^KS11','^TWII','^JKSE','^BSESN','^NSEI','^AXJO','^AXAJ','^SET.BK','^KLSE','^PSI','^VNINDEX'
}

avg_vol = df[df['Index'].isin(asia_indices)].groupby('Index')['intraday_vol'].mean().sort_values(ascending=False)

result = {
    'ranking': avg_vol.head(10).to_dict(),
    'top_index': avg_vol.index[0] if len(avg_vol) else None,
}

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_odd7ChwHe3uQJBWg1zaTw4JQ': ['index_info'], 'var_call_6UD0mOqyuGeKJOEnFz9rkDWH': ['index_trade'], 'var_call_2dIYsGu3z6gkQun3PKxfVrFN': 'file_storage/call_2dIYsGu3z6gkQun3PKxfVrFN.json'}

exec(code, env_args)
