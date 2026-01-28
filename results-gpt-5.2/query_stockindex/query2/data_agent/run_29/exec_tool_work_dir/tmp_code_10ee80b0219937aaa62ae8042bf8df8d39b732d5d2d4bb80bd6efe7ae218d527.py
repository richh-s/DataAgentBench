code = """import json, pandas as pd
from datetime import datetime

path = var_call_lLHayFpptPvz0PWdY6BQBzUX
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# coerce numeric
for c in ['Open','Close']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

# parse dates with multiple formats
s = df['Date'].astype(str)
parsed = pd.to_datetime(s, errors='coerce', format='%Y-%m-%d %H:%M:%S')
mask = parsed.isna()
parsed2 = pd.to_datetime(s[mask], errors='coerce', format='%d %b %Y, %H:%M')
parsed.loc[mask] = parsed2
mask = parsed.isna()
parsed3 = pd.to_datetime(s[mask], errors='coerce', format='%B %d, %Y at %I:%M %p')
parsed.loc[mask] = parsed3

df['dt'] = parsed

df2018 = df[(df['dt']>=pd.Timestamp('2018-01-01')) & (df['dt']<pd.Timestamp('2019-01-01'))].copy()

g = df2018.groupby('Index').agg(
    up_days=('Close', lambda x: int(((df2018.loc[x.index,'Close'] > df2018.loc[x.index,'Open']).sum()))),
    down_days=('Close', lambda x: int(((df2018.loc[x.index,'Close'] < df2018.loc[x.index,'Open']).sum())))
).reset_index()

g['more_up_than_down'] = g['up_days'] > g['down_days']

# North American indices list (common in dataset): US and Canada
north_american = {'^GSPC':'S&P 500','^DJI':'Dow Jones Industrial Average','^IXIC':'NASDAQ Composite','^RUT':'Russell 2000','^GSPTSE':'S&P/TSX Composite','^MXX':'S&P/BMV IPC (Mexico)'}
# Filter to those present
present = g[g['Index'].isin(north_american.keys())].copy()
more = present[present['more_up_than_down']].copy()
more['name'] = more['Index'].map(north_american)
more = more.sort_values('Index')

out = more[['Index','name','up_days','down_days']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ImZxLoJzkhHadq2CyQ1XeMxM': ['index_info'], 'var_call_ICvN9TcHGfgqkv1rn4ueR8cD': ['index_trade'], 'var_call_Gx1D7le8KOQIhwqYB8K61Avl': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}, {'Date': '02 Feb 1987, 00:00'}, {'Date': '03 Feb 1987, 00:00'}, {'Date': 'February 04, 1987 at 12:00 AM'}, {'Date': 'February 05, 1987 at 12:00 AM'}, {'Date': '06 Feb 1987, 00:00'}, {'Date': '1987-02-09 00:00:00'}, {'Date': '1987-02-10 00:00:00'}, {'Date': '11 Feb 1987, 00:00'}, {'Date': '12 Feb 1987, 00:00'}, {'Date': 'February 13, 1987 at 12:00 AM'}, {'Date': '16 Feb 1987, 00:00'}, {'Date': 'February 17, 1987 at 12:00 AM'}, {'Date': 'February 18, 1987 at 12:00 AM'}, {'Date': '19 Feb 1987, 00:00'}, {'Date': '1987-02-20 00:00:00'}, {'Date': 'February 23, 1987 at 12:00 AM'}, {'Date': '24 Feb 1987, 00:00'}, {'Date': 'February 25, 1987 at 12:00 AM'}, {'Date': '26 Feb 1987, 00:00'}, {'Date': '27 Feb 1987, 00:00'}, {'Date': '1987-03-02 00:00:00'}, {'Date': '1987-03-03 00:00:00'}, {'Date': '1987-03-04 00:00:00'}, {'Date': 'March 05, 1987 at 12:00 AM'}, {'Date': 'March 06, 1987 at 12:00 AM'}, {'Date': '09 Mar 1987, 00:00'}, {'Date': 'March 10, 1987 at 12:00 AM'}, {'Date': '11 Mar 1987, 00:00'}, {'Date': '12 Mar 1987, 00:00'}, {'Date': 'March 13, 1987 at 12:00 AM'}], 'var_call_lLHayFpptPvz0PWdY6BQBzUX': 'file_storage/call_lLHayFpptPvz0PWdY6BQBzUX.json'}

exec(code, env_args)
