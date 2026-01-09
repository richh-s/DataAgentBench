code = """import json, pandas as pd
from datetime import datetime

path = var_call_1sqjtRTYXfUiaRn778mUhzxx
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# coerce numeric
for c in ['Open','High','Low']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

# parse dates with mixed formats
s = df['Date'].astype(str)
# try pandas parsing
dt = pd.to_datetime(s, errors='coerce', infer_datetime_format=True, utc=False)
# second pass for remaining using dateutil via pandas (still)
mask = dt.isna()
if mask.any():
    dt2 = pd.to_datetime(s[mask], errors='coerce', utc=False)
    dt.loc[mask] = dt2

df['dt'] = dt

# filter since 2020-01-01
start = pd.Timestamp('2020-01-01')
df = df[df['dt'] >= start]

# compute intraday volatility
vol = (df['High'] - df['Low']) / df['Open']
df['vol'] = vol.replace([pd.NA, float('inf'), -float('inf')], pd.NA)
df = df.dropna(subset=['vol'])

agg = df.groupby('Index').agg(avg_intraday_vol=('vol','mean'), n_days=('vol','size')).reset_index()
agg = agg.sort_values('avg_intraday_vol', ascending=False)

# Asia indices list (major): HSI (Hong Kong), N225 (Japan), 000001.SS (China Shanghai), 399001.SZ (China Shenzhen), KS11 (Korea), TWII (Taiwan), STI (Singapore), SENSEX/BSESN? (India), NIFTY? etc.
asia_set = {'HSI','N225','000001.SS','399001.SZ','KS11','TWII','STI','BSESN','SENSEX','NSEI','NIFTY 50','JKSE','KLCI','SET.BK','VNINDEX','PSEI'}
asia = agg[agg['Index'].isin(asia_set)].copy()

# if empty, fall back by taking top among indices that are known Asia in dataset by checking presence
if asia.empty:
    # infer by choosing indices that contain '.SS' or '.SZ' or are in common tickers
    asia = agg[agg['Index'].str.contains(r'\\.SS|\\.SZ', na=False) | agg['Index'].isin({'HSI','N225','KS11','TWII','STI'})].copy()

winner = asia.iloc[0].to_dict() if not asia.empty else None

out = {
    'winner_index': None if winner is None else winner['Index'],
    'avg_intraday_volatility': None if winner is None else float(winner['avg_intraday_vol']),
    'n_days_since_2020': None if winner is None else int(winner['n_days']),
    'top_asia': asia.head(10).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_u76uTqHCjSvKeIahYMqS5YhF': ['index_info'], 'var_call_usoFzwcYys8hHiui1BeCpFQG': ['index_trade'], 'var_call_4RtYxDqILTrpUBomRzmrKXY3': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_1sqjtRTYXfUiaRn778mUhzxx': 'file_storage/call_1sqjtRTYXfUiaRn778mUhzxx.json'}

exec(code, env_args)
