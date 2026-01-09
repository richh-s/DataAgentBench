code = """import json, pandas as pd
from datetime import datetime

path = var_call_fUlnjxtUPSFiYiSMjqLbTil6
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# parse dates robustly
s = df['Date'].astype(str)
# normalize common 'at 12:00 AM'
s = s.str.replace(' at 12:00 AM','', regex=False)
# some have ', 00:00'
s = s.str.replace(', 00:00','', regex=False)

dt = pd.to_datetime(s, errors='coerce', infer_datetime_format=True)
# fallback: try another parse for remaining
mask = dt.isna()
if mask.any():
    dt2 = pd.to_datetime(s[mask], errors='coerce', format='%Y-%m-%d %H:%M:%S')
    dt.loc[mask] = dt2

df['dt'] = dt
# keep from 2000-01-01
start = pd.Timestamp('2000-01-01')
df = df[df['dt']>=start].copy()
# ensure numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['dt','CloseUSD'])

# monthly contributions at first available trading day each month per index
# compute monthly first price
idx_month = df.assign(month=df['dt'].dt.to_period('M'))
firsts = idx_month.sort_values(['Index','dt']).groupby(['Index','month'], as_index=False).first()[['Index','month','CloseUSD']]

# DCA: invest 1 unit USD each month -> shares = 1/price
firsts['shares'] = 1.0/firsts['CloseUSD']
shares_sum = firsts.groupby('Index', as_index=False)['shares'].sum()
# last available close (latest date) per index
df_last = df.sort_values(['Index','dt']).groupby('Index', as_index=False).last()[['Index','CloseUSD','dt']]

res = shares_sum.merge(df_last, on='Index', how='inner')
res = res.rename(columns={'CloseUSD':'last_close_usd','dt':'last_date'})
# total invested = number of months
months = firsts.groupby('Index', as_index=False).size().rename(columns={'size':'n_months'})
res = res.merge(months, on='Index')
res['invested_usd'] = res['n_months'].astype(float)
res['final_value_usd'] = res['shares']*res['last_close_usd']
res['return_multiple'] = res['final_value_usd']/res['invested_usd']
res = res.sort_values('return_multiple', ascending=False)

# mapping index->country via known symbols
country_map = {
    'IXIC':'United States',
    'NYA':'United States',
    'GSPTSE':'Canada',
    'GDAXI':'Germany',
    'SSMI':'Switzerland',
    'N225':'Japan',
    'HSI':'Hong Kong',
    '000001.SS':'China',
    '399001.SZ':'China',
    'TWII':'Taiwan',
    'N100':'Europe (Euronext)',
    'J203.JO':'South Africa',
    'NSEI':'India'
}
res['country'] = res['Index'].map(country_map)

out = res.head(5)[['Index','country','return_multiple','final_value_usd','invested_usd','n_months','last_date']]
# convert last_date to iso
out['last_date'] = out['last_date'].dt.strftime('%Y-%m-%d')
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_1WYE8vnztUcSDODnpobMq51C': ['index_info'], 'var_call_zNaIozwVAdsCjdG2xkAFh5Ya': ['index_trade'], 'var_call_YLaoQthgB5ifUM0IdSy9C0dZ': [{'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5791'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5760'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '8438'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '10526'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '8492'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '12690'}, {'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '2346'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '5474'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13874'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'n': '3346'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13947'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '7671'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '5869'}], 'var_call_NVgUXkJJ3f9k1UngMbFbETBt': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_fUlnjxtUPSFiYiSMjqLbTil6': 'file_storage/call_fUlnjxtUPSFiYiSMjqLbTil6.json'}

exec(code, env_args)
