code = """import json, pandas as pd
from datetime import datetime
import re

path = var_call_5CxUHpSJZkgfdqVRi5Oqov68
with open(path,'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# ensure numeric
for c in ['Open','Close']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

# parse date with pandas
# remove 'at 12:00 AM'
df['Date_clean'] = df['Date'].str.replace(r'\s+at\s+\d{1,2}:\d{2}\s+[AP]M','', regex=True)
# some have comma time ', 00:00'
df['Date_clean'] = df['Date_clean'].str.replace(', 00:00','', regex=False)
# some have ' 00:00:00'
df['Date_clean'] = df['Date_clean'].str.replace(' 00:00:00','', regex=False)

# parse
parsed = pd.to_datetime(df['Date_clean'], errors='coerce', infer_datetime_format=True)
df['Date_parsed'] = parsed

df2018 = df[(df['Date_parsed']>=pd.Timestamp('2018-01-01')) & (df['Date_parsed']<pd.Timestamp('2019-01-01'))].copy()

# classify NA indices: infer from common tickers present
na_set = {'^GSPC','^DJI','^IXIC','^RUT','^GSPTSE','GSPTSE','^FTSE','^NYA','^SPX','SPX','DJI','IXIC','RUT','^MXX','MXX','^BVSP'}
# but database seems to use symbols like GSPC? let's check unique indices
indices = set(df2018['Index'].unique())
# choose likely NA indices by known ones existing in dataset
known_na = [i for i in indices if i in ['^GSPC','^DJI','^IXIC','^RUT','^GSPTSE','GSPTSE','^MXX','MXX']]
# also possible 'GSPC','DJI','IXIC','RUT'
known_na += [i for i in indices if i in ['GSPC','DJI','IXIC','RUT']]
known_na = sorted(set(known_na))

sub = df2018[df2018['Index'].isin(known_na)].copy()
agg = sub.groupby('Index').apply(lambda g: pd.Series({
    'up_days': int((g['Close']>g['Open']).sum()),
    'down_days': int((g['Close']<g['Open']).sum()),
    'total_days': int(g.shape[0])
})).reset_index()
agg['more_up_than_down'] = agg['up_days']>agg['down_days']
res = agg[agg['more_up_than_down']].sort_values('Index')
answer = res[['Index','up_days','down_days']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps({'na_indices_present': known_na, 'indices_more_up_than_down_2018': answer}))"""

env_args = {'var_call_Sb3OdfCwMWjldfnmakCMly9p': ['index_info'], 'var_call_wdvQWiCq1ArP8Wh2f7OnXN2o': ['index_trade'], 'var_call_hRFude3ReKIMb97BLBAkvMyh': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_call_52EKmCOONmhtG92lxBCT9l3v': {'status': 'need_more_query'}, 'var_call_5CxUHpSJZkgfdqVRi5Oqov68': 'file_storage/call_5CxUHpSJZkgfdqVRi5Oqov68.json'}

exec(code, env_args)
