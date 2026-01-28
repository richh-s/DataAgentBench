code = """import json, pandas as pd

path = var_call_lLHayFpptPvz0PWdY6BQBzUX
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for c in ['Open','Close']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

s = df['Date'].astype(str)
parsed = pd.to_datetime(s, errors='coerce', format='%Y-%m-%d %H:%M:%S')
mask = parsed.isna()
parsed.loc[mask] = pd.to_datetime(s[mask], errors='coerce', format='%d %b %Y, %H:%M')
mask = parsed.isna()
parsed.loc[mask] = pd.to_datetime(s[mask], errors='coerce', format='%B %d, %Y at %I:%M %p')

df['dt'] = parsed

# North America indices in this dataset: IXIC (Nasdaq Composite), NYA (NYSE Composite), GSPTSE (S&P/TSX)
na_map = {'IXIC':'NASDAQ Composite','NYA':'NYSE Composite','GSPTSE':'S&P/TSX Composite'}

df2018 = df[(df['dt']>=pd.Timestamp('2018-01-01')) & (df['dt']<pd.Timestamp('2019-01-01')) & (df['Index'].isin(na_map.keys()))].copy()

df2018['up'] = df2018['Close'] > df2018['Open']
df2018['down'] = df2018['Close'] < df2018['Open']

g = df2018.groupby('Index').agg(up_days=('up','sum'), down_days=('down','sum')).reset_index()

g['name'] = g['Index'].map(na_map)
more = g[g['up_days'] > g['down_days']].sort_values('Index')

out = more[['Index','name','up_days','down_days']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ImZxLoJzkhHadq2CyQ1XeMxM': ['index_info'], 'var_call_ICvN9TcHGfgqkv1rn4ueR8cD': ['index_trade'], 'var_call_Gx1D7le8KOQIhwqYB8K61Avl': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}, {'Date': '02 Feb 1987, 00:00'}, {'Date': '03 Feb 1987, 00:00'}, {'Date': 'February 04, 1987 at 12:00 AM'}, {'Date': 'February 05, 1987 at 12:00 AM'}, {'Date': '06 Feb 1987, 00:00'}, {'Date': '1987-02-09 00:00:00'}, {'Date': '1987-02-10 00:00:00'}, {'Date': '11 Feb 1987, 00:00'}, {'Date': '12 Feb 1987, 00:00'}, {'Date': 'February 13, 1987 at 12:00 AM'}, {'Date': '16 Feb 1987, 00:00'}, {'Date': 'February 17, 1987 at 12:00 AM'}, {'Date': 'February 18, 1987 at 12:00 AM'}, {'Date': '19 Feb 1987, 00:00'}, {'Date': '1987-02-20 00:00:00'}, {'Date': 'February 23, 1987 at 12:00 AM'}, {'Date': '24 Feb 1987, 00:00'}, {'Date': 'February 25, 1987 at 12:00 AM'}, {'Date': '26 Feb 1987, 00:00'}, {'Date': '27 Feb 1987, 00:00'}, {'Date': '1987-03-02 00:00:00'}, {'Date': '1987-03-03 00:00:00'}, {'Date': '1987-03-04 00:00:00'}, {'Date': 'March 05, 1987 at 12:00 AM'}, {'Date': 'March 06, 1987 at 12:00 AM'}, {'Date': '09 Mar 1987, 00:00'}, {'Date': 'March 10, 1987 at 12:00 AM'}, {'Date': '11 Mar 1987, 00:00'}, {'Date': '12 Mar 1987, 00:00'}, {'Date': 'March 13, 1987 at 12:00 AM'}], 'var_call_lLHayFpptPvz0PWdY6BQBzUX': 'file_storage/call_lLHayFpptPvz0PWdY6BQBzUX.json', 'var_call_XZVwt1UPdyzoxaPDoOfE1JIG': [], 'var_call_Or1ee0pPJIyXKzv1qZnebBuP': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}]}

exec(code, env_args)
