code = """import json, pandas as pd

path = var_call_tetSxc6SzLAuLv9kEpzVCL69
with open(path, 'r') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['Date','CloseUSD'])

m = df.copy()
m['Month'] = m['Date'].dt.to_period('M').dt.to_timestamp()
monthly = (m.sort_values(['Index','Date'])
             .groupby(['Index','Month'], as_index=False)
             .tail(1)[['Index','Month','CloseUSD']])

monthly['shares'] = 1.0 / monthly['CloseUSD']
agg = monthly.groupby('Index').agg(
    months=('Month','nunique'),
    total_shares=('shares','sum'),
    last_month=('Month','max'),
    last_price=('CloseUSD','last')
).reset_index()
agg['final_value'] = agg['total_shares'] * agg['last_price']
agg['total_invested'] = agg['months'] * 1.0
agg['multiple'] = agg['final_value'] / agg['total_invested']

agg2 = agg[agg['months']>=12].sort_values('multiple', ascending=False)
top5 = agg2.head(5).copy()

country_map = {
    '^GSPC':'United States','^IXIC':'United States','^DJI':'United States','^RUT':'United States',
    '^FTSE':'United Kingdom','^FCHI':'France','^GDAXI':'Germany','^N225':'Japan','^HSI':'Hong Kong',
    '000001.SS':'China','399001.SZ':'China','^STI':'Singapore','^BSESN':'India','^NSEI':'India',
    '^KS11':'South Korea','^TWII':'Taiwan','^BVSP':'Brazil','^MXX':'Mexico','^GSPTSE':'Canada',
    '^AORD':'Australia','^AXJO':'Australia','^SSMI':'Switzerland','^STOXX50E':'Eurozone',
    '^IBEX':'Spain','^N100':'Netherlands','^OMX':'Sweden','^ISEQ':'Ireland','^TA125.TA':'Israel',
    '^JN0U.JO':'South Africa'
}

top5['country'] = top5['Index'].map(country_map).fillna('Unknown')
out = top5[['Index','multiple','months','last_month','country']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out, default=str))"""

env_args = {'var_call_KLQHika56qcFPW44Mp3qMrFp': ['index_info'], 'var_call_kFUOdi0y8ql8euw7U9rBsd87': ['index_trade'], 'var_call_tetSxc6SzLAuLv9kEpzVCL69': 'file_storage/call_tetSxc6SzLAuLv9kEpzVCL69.json'}

exec(code, env_args)
