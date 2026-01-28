code = """import json, pandas as pd
from datetime import datetime

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path

recs = load_records(var_call_v2wpHVmgP5dYQ1U3PFyxGDYq)
df = pd.DataFrame(recs)
# coerce numeric
for c in ['Open','Close']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

# parse dates with mixed formats
s = df['Date'].astype(str)
dt1 = pd.to_datetime(s, errors='coerce', infer_datetime_format=True)
# fallback for 'DD Mon YYYY, HH:MM'
mask = dt1.isna()
if mask.any():
    dt1.loc[mask] = pd.to_datetime(s[mask], errors='coerce', format='%d %b %Y, %H:%M')
mask = dt1.isna()
if mask.any():
    dt1.loc[mask] = pd.to_datetime(s[mask], errors='coerce', format='%B %d, %Y at %I:%M %p')
mask = dt1.isna()
if mask.any():
    dt1.loc[mask] = pd.to_datetime(s[mask], errors='coerce', format='%Y-%m-%d %H:%M:%S')

df['dt'] = dt1

df2018 = df[(df['dt']>=pd.Timestamp('2018-01-01')) & (df['dt']<pd.Timestamp('2019-01-01'))].copy()

summary = (df2018.assign(
    up = (df2018['Close']>df2018['Open']).astype(int),
    down = (df2018['Close']<df2018['Open']).astype(int)
).groupby('Index')[['up','down']].sum().reset_index())
summary['more_up_than_down'] = summary['up']>summary['down']
res = summary[summary['more_up_than_down']].sort_values('Index')[['Index','up','down']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_aRdqmsXiMaoxxSyoua3YCSzS': ['index_info'], 'var_call_PXRgAraG2sbzukr4Gn1TkBvX': ['index_trade'], 'var_call_FifB7Eicgmi4hQh1gfqRTO0K': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_MOmm8MZZ8YGVXPyiCU0oXtsx': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}], 'var_call_2W0xmcDC3rSrdRrW7O1qP0P6': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_call_CCv7Ud5ajr5uuBfGJ7DLPAUj': 'file_storage/call_CCv7Ud5ajr5uuBfGJ7DLPAUj.json', 'var_call_v2wpHVmgP5dYQ1U3PFyxGDYq': 'file_storage/call_v2wpHVmgP5dYQ1U3PFyxGDYq.json'}

exec(code, env_args)
