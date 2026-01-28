code = """import json, pandas as pd
path = var_call_usFMWtYGNfthNa5kmTDcObLx
with open(path,'r') as f:
    data=json.load(f)
df=pd.DataFrame(data)
df['dt']=pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)
mask=df['dt'].isna()
if mask.any():
    df.loc[mask,'dt']=pd.to_datetime(df.loc[mask,'Date'].astype(str), errors='coerce', format='%d %b %Y, %H:%M')
mask=df['dt'].isna()
if mask.any():
    df.loc[mask,'dt']=pd.to_datetime(df.loc[mask,'Date'].astype(str), errors='coerce', format='%B %d, %Y at %I:%M %p')

for c in ['Open','Close']:
    df[c]=pd.to_numeric(df[c], errors='coerce')

df=df.dropna(subset=['dt','Index','Open','Close'])
df=df[df['dt'].dt.year==2018].copy()

# compute up/down counts
df['up'] = (df['Close']>df['Open']).astype(int)
df['down'] = (df['Close']<df['Open']).astype(int)
agg=df.groupby('Index').agg(n_days=('dt','size'), up_days=('up','sum'), down_days=('down','sum')).reset_index()

na = agg[agg['Index'].isin(['IXIC','NYA','GSPTSE'])].copy()
more = na[na['up_days']>na['down_days']].sort_values('Index')
print('__RESULT__:')
print(json.dumps({'na_all': na.to_dict(orient='records'), 'na_more_up': more.to_dict(orient='records')}))"""

env_args = {'var_call_7WBEV3uUZmGPjj9UIMaDSreY': ['index_info'], 'var_call_gC33o0nZJdLAtvPBPiZMZj6R': ['index_trade'], 'var_call_El3XbJPgD69wisVsVtoWznRs': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_usFMWtYGNfthNa5kmTDcObLx': 'file_storage/call_usFMWtYGNfthNa5kmTDcObLx.json', 'var_call_HQmzWK0JujYBbmFz1K7KaNOj': [], 'var_call_FSw23KDTFmFks1B58ShCQZBM': {'n_indices_2018': 13, 'indices_2018_sample': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII'], 'contains_GSPC': False, 'contains_DJI': False, 'contains_IXIC': False, 'contains_GSPTSE': False, 'contains_MXX': False}}

exec(code, env_args)
