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

# show indices available in 2018
sub=df[df['dt'].dt.year==2018]
inds=sorted(sub['Index'].dropna().unique().tolist())
print('__RESULT__:')
print(json.dumps({'n_indices_2018': len(inds), 'indices_2018_sample': inds[:100], 'contains_GSPC': '^GSPC' in inds, 'contains_DJI': '^DJI' in inds, 'contains_IXIC': '^IXIC' in inds, 'contains_GSPTSE': '^GSPTSE' in inds, 'contains_MXX': '^MXX' in inds}))"""

env_args = {'var_call_7WBEV3uUZmGPjj9UIMaDSreY': ['index_info'], 'var_call_gC33o0nZJdLAtvPBPiZMZj6R': ['index_trade'], 'var_call_El3XbJPgD69wisVsVtoWznRs': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_usFMWtYGNfthNa5kmTDcObLx': 'file_storage/call_usFMWtYGNfthNa5kmTDcObLx.json', 'var_call_HQmzWK0JujYBbmFz1K7KaNOj': []}

exec(code, env_args)
