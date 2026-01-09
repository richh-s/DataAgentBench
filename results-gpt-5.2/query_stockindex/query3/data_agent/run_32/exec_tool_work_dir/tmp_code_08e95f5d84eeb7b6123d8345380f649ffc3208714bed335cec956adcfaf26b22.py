code = """import json, pandas as pd
from datetime import datetime

# load trade data
path = var_call_gpP6pfNH9lmgSRTKpwFKM4Dd
with open(path, 'r') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# parse dates with mixed formats
s = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)
# second pass with dateutil-like flexibility already in pandas; still some may be NaT; try manual common formats
mask = s.isna()
if mask.any():
    fmts = ["%d %b %Y, %H:%M", "%B %d, %Y at %I:%M %p", "%Y-%m-%d %H:%M:%S", "%b %d, %Y at %I:%M %p", "%d %B %Y, %H:%M"]
    s2 = pd.Series([pd.NaT]*len(df))
    for fmt in fmts:
        m = mask & s2.isna()
        if not m.any():
            continue
        s2.loc[m] = pd.to_datetime(df.loc[m,'Date'], format=fmt, errors='coerce')
    s.loc[mask] = s2.loc[mask]

df['date'] = s
# keep from 2000-01-01
start = pd.Timestamp('2000-01-01')
df = df[df['date']>=start].copy()
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['date','CloseUSD'])
# monthly contribution at first available trading day each month
# compute shares purchased = 1/price, cumulative shares, value = shares*last_price

df['month'] = df['date'].dt.to_period('M')
# first trading day per month per index
first = df.sort_values('date').groupby(['Index','month'], as_index=False).first()
# last available date per index for valuation
last_price = df.sort_values('date').groupby('Index', as_index=False).last()[['Index','CloseUSD','date']].rename(columns={'CloseUSD':'last_CloseUSD','date':'last_date'})

first['shares'] = 1.0/first['CloseUSD']
agg = first.groupby('Index').agg(total_shares=('shares','sum'), n_months=('shares','size'), total_invested=('shares','size')).reset_index()
# total_invested is number of months since we invest $1 per month
agg = agg.merge(last_price, on='Index', how='left')
agg['final_value'] = agg['total_shares'] * agg['last_CloseUSD']
agg['return_multiple'] = agg['final_value'] / agg['total_invested']
agg = agg.sort_values('return_multiple', ascending=False)

top5 = agg.head(5)

# map index symbol to country (inferred)
country_map = {
    'IXIC':'United States',
    'NYA':'United States',
    'GSPTSE':'Canada',
    'GDAXI':'Germany',
    'SSMI':'Switzerland',
    'N225':'Japan',
    'HSI':'Hong Kong',
    'TWII':'Taiwan',
    '000001.SS':'China',
    '399001.SZ':'China',
    'N100':'Eurozone',
    'J203.JO':'South Africa',
    'NSEI':'India'
}

top5['Country'] = top5['Index'].map(country_map)
res = top5[['Index','Country','return_multiple','n_months','last_date']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(res, default=str))"""

env_args = {'var_call_Opw0wzUt5btQ6MiXxOvUbvSG': ['index_info'], 'var_call_cBrJEGDcdswyeecnADAd5vGr': ['index_trade'], 'var_call_kM7nx1WP9qNqv8bImYfjof3X': [{'Index': '000001.SS', 'min_date_raw': '01 Apr 2003, 00:00', 'max_date_raw': 'September 30, 2015 at 12:00 AM', 'n': '5791'}, {'Index': '399001.SZ', 'min_date_raw': '01 Apr 2004, 00:00', 'max_date_raw': 'September 30, 2015 at 12:00 AM', 'n': '5760'}, {'Index': 'GDAXI', 'min_date_raw': '01 Apr 1992, 00:00', 'max_date_raw': 'September 30, 2016 at 12:00 AM', 'n': '8438'}, {'Index': 'GSPTSE', 'min_date_raw': '01 Apr 1981, 00:00', 'max_date_raw': 'September 30, 2016 at 12:00 AM', 'n': '10526'}, {'Index': 'HSI', 'min_date_raw': '01 Apr 1992, 00:00', 'max_date_raw': 'September 30, 2019 at 12:00 AM', 'n': '8492'}, {'Index': 'IXIC', 'min_date_raw': '01 Apr 1974, 00:00', 'max_date_raw': 'September 30, 2015 at 12:00 AM', 'n': '12690'}, {'Index': 'J203.JO', 'min_date_raw': '01 Apr 2016, 00:00', 'max_date_raw': 'September 30, 2019 at 12:00 AM', 'n': '2346'}, {'Index': 'N100', 'min_date_raw': '01 Apr 2003, 00:00', 'max_date_raw': 'September 30, 2019 at 12:00 AM', 'n': '5474'}, {'Index': 'N225', 'min_date_raw': '01 Apr 1971, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n': '13874'}, {'Index': 'NSEI', 'min_date_raw': '01 Apr 2014, 00:00', 'max_date_raw': 'September 30, 2014 at 12:00 AM', 'n': '3346'}, {'Index': 'NYA', 'min_date_raw': '01 Apr 1969, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n': '13947'}, {'Index': 'SSMI', 'min_date_raw': '01 Apr 1996, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n': '7671'}, {'Index': 'TWII', 'min_date_raw': '01 Apr 2004, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n': '5869'}], 'var_call_gpP6pfNH9lmgSRTKpwFKM4Dd': 'file_storage/call_gpP6pfNH9lmgSRTKpwFKM4Dd.json'}

exec(code, env_args)
