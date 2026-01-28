code = """import json, pandas as pd
from datetime import datetime

# load full dataset
path = var_call_usFMWtYGNfthNa5kmTDcObLx
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# parse dates robustly
s = df['Date'].astype(str)
dt = pd.to_datetime(s, errors='coerce', infer_datetime_format=True)
# try additional formats for remaining
mask = dt.isna()
if mask.any():
    dt2 = pd.to_datetime(s[mask], errors='coerce', format='%d %b %Y, %H:%M')
    dt.loc[mask] = dt2
mask = dt.isna()
if mask.any():
    dt3 = pd.to_datetime(s[mask], errors='coerce', format='%B %d, %Y at %I:%M %p')
    dt.loc[mask] = dt3

df['dt'] = dt

df = df[df['dt'].dt.year == 2018].copy()

# ensure numeric
for c in ['Open','Close']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

df = df.dropna(subset=['Open','Close','dt','Index'])

g = df.groupby('Index').agg(
    n_days=('dt','size'),
    up_days=('Close', lambda x: int((x.values > df.loc[x.index,'Open'].values).sum())),
    down_days=('Close', lambda x: int((x.values < df.loc[x.index,'Open'].values).sum()))
).reset_index()

g['more_up_than_down'] = g['up_days'] > g['down_days']

# North America indices to consider: common major NA index symbols present in dataset
north_america = {'^GSPC','^DJI','^IXIC','^RUT','^GSPTSE','GSPTSE','^MXX','MXX','^BVSP'}
# ^BVSP is Brazil (South America) - exclude; keep US/Canada/Mexico
north_america = {'^GSPC','^DJI','^IXIC','^RUT','^GSPTSE','GSPTSE','^MXX','MXX'}

na = g[g['Index'].isin(north_america)].copy()
na_more = na[na['more_up_than_down']].sort_values('Index')

result = na_more[['Index','up_days','down_days','n_days']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_7WBEV3uUZmGPjj9UIMaDSreY': ['index_info'], 'var_call_gC33o0nZJdLAtvPBPiZMZj6R': ['index_trade'], 'var_call_El3XbJPgD69wisVsVtoWznRs': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_usFMWtYGNfthNa5kmTDcObLx': 'file_storage/call_usFMWtYGNfthNa5kmTDcObLx.json'}

exec(code, env_args)
