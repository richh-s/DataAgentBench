code = """import json, pandas as pd

p = var_call_fZBYlUx6uQezfyNSTEW6jvqQ
with open(p, 'r', encoding='utf-8') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
df['dt'] = pd.to_datetime(df['dt'])
df['close_usd'] = pd.to_numeric(df['close_usd'], errors='coerce')
df = df.dropna(subset=['close_usd'])

df['ym'] = df['dt'].dt.to_period('M').astype(str)
first_month = (df.sort_values(['idx','dt'])
               .groupby(['idx','ym'], as_index=False)
               .first()[['idx','ym','close_usd','dt']])
last_price = (df.sort_values(['idx','dt'])
              .groupby('idx', as_index=False)
              .last()[['idx','close_usd','dt']]
              .rename(columns={'close_usd':'last_close_usd','dt':'last_dt'}))

agg = (first_month.groupby('idx')
       .agg(months=('ym','nunique'),
            shares=('close_usd', lambda s: (1.0/s).sum()),
            start_dt=('dt','min'))
       .reset_index())
agg = agg.merge(last_price, on='idx', how='left')
agg['invested_usd'] = agg['months'] * 1.0
agg['final_value_usd'] = agg['shares'] * agg['last_close_usd']
agg['multiple'] = agg['final_value_usd'] / agg['invested_usd']

# top 5 indices by DCA multiple
top5 = agg.sort_values('multiple', ascending=False).head(5)

country_map = {
    '^GSPC':'United States', '^DJI':'United States', '^IXIC':'United States', '^RUT':'United States', '^NYA':'United States',
    '^FTSE':'United Kingdom', '^FCHI':'France', '^GDAXI':'Germany', '^STOXX50E':'Eurozone',
    '^N225':'Japan', '^HSI':'Hong Kong', '000001.SS':'China', '^KS11':'South Korea', '^TWII':'Taiwan',
    '^AXJO':'Australia', '^BSESN':'India', '^NSEI':'India', '^BVSP':'Brazil', '^MXX':'Mexico',
    '^GSPTSE':'Canada', '^SPTSX':'Canada', '^SSMI':'Switzerland'
}

def map_country(idx):
    if idx in country_map:
        return country_map[idx]
    if isinstance(idx, str) and (idx.endswith('.SS') or idx.endswith('.SZ')):
        return 'China'
    if isinstance(idx, str) and idx.endswith('.SA'):
        return 'Brazil'
    return None

top5 = top5.copy()
top5['country'] = top5['idx'].apply(map_country)

out = top5[['idx','multiple','months','invested_usd','final_value_usd','country','start_dt','last_dt']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out, default=str))"""

env_args = {'var_call_fZBYlUx6uQezfyNSTEW6jvqQ': 'file_storage/call_fZBYlUx6uQezfyNSTEW6jvqQ.json'}

exec(code, env_args)
