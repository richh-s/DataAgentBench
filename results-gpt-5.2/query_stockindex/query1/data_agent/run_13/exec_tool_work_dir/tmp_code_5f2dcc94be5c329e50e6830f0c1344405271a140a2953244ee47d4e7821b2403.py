code = """import json, pandas as pd
from datetime import datetime

# load full dataset
path = var_call_F1hUCkumXxxCikpw9uDjD7Js
with open(path, 'r') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
# coerce numeric
for c in ['Open','High','Low']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

# parse dates with multiple formats
s = df['Date'].astype(str)
# try a broad parse; pandas handles many formats
parsed = pd.to_datetime(s, errors='coerce', infer_datetime_format=True)

df['parsed_date'] = parsed

df = df.dropna(subset=['parsed_date','Open','High','Low'])
df = df[df['parsed_date'] >= pd.Timestamp('2020-01-01')]

# intraday volatility
vol = (df['High'] - df['Low']) / df['Open'].replace(0, pd.NA)
df['intraday_vol'] = vol

df = df.dropna(subset=['intraday_vol'])

avg = df.groupby('Index', as_index=False)['intraday_vol'].mean().sort_values('intraday_vol', ascending=False)

# Asia indices list (inferred major Asian markets)
asia_indices = [
    'N225','HSI','000001.SS','399001.SZ','KS11','TWII','STI','SENSEX','NIFTY 50','JKSE','KLCI','PSEI','SET.BK','VNINDEX','NZ50'
]
# keep those present
avg_asia = avg[avg['Index'].isin(asia_indices)].copy()

# If some common tickers differ, include ones we can infer by suffix
# add any .SS/.SZ/.HK/.KS/.TW that are present
extra = avg[avg['Index'].str.contains(r'\.(SS|SZ|HK|KS|TW)$', na=False)]
avg_asia = pd.concat([avg_asia, extra], ignore_index=True).drop_duplicates(subset=['Index'])

avg_asia = avg_asia.sort_values('intraday_vol', ascending=False)

winner = avg_asia.head(1)
result = {
    'index': None if winner.empty else winner.iloc[0]['Index'],
    'avg_intraday_volatility': None if winner.empty else float(winner.iloc[0]['intraday_vol']),
    'period_start': '2020-01-01'
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_3getYX8YLBRSfQ9Guec1JEXg': ['index_info'], 'var_call_f9IGKpwzmePT0fcfi6uKiuzL': ['index_trade'], 'var_call_F3ThOp7zrL2le4xRtQougNd5': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_call_F1hUCkumXxxCikpw9uDjD7Js': 'file_storage/call_F1hUCkumXxxCikpw9uDjD7Js.json'}

exec(code, env_args)
