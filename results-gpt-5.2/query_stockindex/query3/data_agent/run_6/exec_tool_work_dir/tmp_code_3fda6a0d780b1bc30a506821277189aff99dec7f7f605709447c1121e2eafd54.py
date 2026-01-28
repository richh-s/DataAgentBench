code = """import json, pandas as pd
from datetime import datetime

# load full trade data
path = var_call_vL1QPMftdWbthrrxzfai5eNQ
with open(path, 'r') as f:
    records = json.load(f)

df = pd.DataFrame(records)

# parse dates with multiple formats
s = df['date_raw'].astype(str)
parsed = pd.to_datetime(s, errors='coerce', utc=False)
# second pass for formats like '31 Dec 1986, 00:00'
mask = parsed.isna()
parsed.loc[mask] = pd.to_datetime(s[mask], format='%d %b %Y, %H:%M', errors='coerce')
# third pass for 'September 30, 2015 at 12:00 AM'
mask = parsed.isna()
parsed.loc[mask] = pd.to_datetime(s[mask].str.replace(' at ', ' ', regex=False), format='%B %d, %Y %I:%M %p', errors='coerce')

df['date'] = parsed.dt.tz_localize(None)
df['close_usd'] = pd.to_numeric(df['close_usd'], errors='coerce')

df = df.dropna(subset=['date','close_usd'])

# filter since 2000-01-01
start = pd.Timestamp('2000-01-01')
df = df[df['date'] >= start].copy()

# monthly DCA: invest 1 unit of USD on first trading day of each month
# shares bought = 1/price

df['month'] = df['date'].dt.to_period('M')
first_days = df.sort_values(['idx','date']).groupby(['idx','month'], as_index=False).first()

first_days['shares'] = 1.0 / first_days['close_usd']
shares_sum = first_days.groupby('idx', as_index=False)['shares'].sum().rename(columns={'shares':'total_shares'})
contrib = first_days.groupby('idx', as_index=False).size().rename(columns={'size':'n_months'})

# final value at last available date for each index
last = df.sort_values(['idx','date']).groupby('idx', as_index=False).last()[['idx','date','close_usd']].rename(columns={'close_usd':'final_close_usd','date':'final_date'})

res = shares_sum.merge(contrib, on='idx').merge(last, on='idx')
res['total_contrib_usd'] = res['n_months'].astype(float) * 1.0
res['final_value_usd'] = res['total_shares'] * res['final_close_usd']
res['overall_return_multiple'] = res['final_value_usd'] / res['total_contrib_usd']
res['overall_return_pct'] = (res['overall_return_multiple'] - 1.0) * 100.0

# top 5 indices by return multiple
res_top5 = res.sort_values('overall_return_multiple', ascending=False).head(5).copy()

# map idx to exchange/country (inferred)
idx_to_exchange_country = {
    'NYA': ('New York Stock Exchange', 'United States'),
    'IXIC': ('NASDAQ', 'United States'),
    'HSI': ('Hong Kong Stock Exchange', 'Hong Kong'),
    '000001.SS': ('Shanghai Stock Exchange', 'China'),
    '399001.SZ': ('Shenzhen Stock Exchange', 'China'),
    'N225': ('Tokyo Stock Exchange', 'Japan'),
    'GDAXI': ('Frankfurt Stock Exchange', 'Germany'),
    'GSPTSE': ('Toronto Stock Exchange', 'Canada'),
    'SSMI': ('SIX Swiss Exchange', 'Switzerland'),
    'TWII': ('Taiwan Stock Exchange', 'Taiwan'),
    'N100': ('Euronext', 'Europe'),
    'J203.JO': ('Johannesburg Stock Exchange', 'South Africa'),
    'NSEI': ('National Stock Exchange of India', 'India'),
}

res_top5['exchange'] = res_top5['idx'].map(lambda x: idx_to_exchange_country.get(x, (None,None))[0])
res_top5['country'] = res_top5['idx'].map(lambda x: idx_to_exchange_country.get(x, (None,None))[1])

out = res_top5[['idx','exchange','country','n_months','final_date','overall_return_multiple','overall_return_pct']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out, default=str))"""

env_args = {'var_call_UY5tmn0qZ3I19hkYjSdDWEE7': ['index_info'], 'var_call_SeqENvo5S2LzC7wwbD10zWkq': ['index_trade'], 'var_call_xxu9CreI2TcrryuVONYGdJ5K': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_dgO9yd7mDjFzegb0QlFRmtbj': [{'idx': '000001.SS', 'min_date_raw': '01 Apr 2003, 00:00', 'max_date_raw': 'September 30, 2015 at 12:00 AM', 'n_rows': '5791'}, {'idx': '399001.SZ', 'min_date_raw': '01 Apr 2004, 00:00', 'max_date_raw': 'September 30, 2015 at 12:00 AM', 'n_rows': '5760'}, {'idx': 'GDAXI', 'min_date_raw': '01 Apr 1992, 00:00', 'max_date_raw': 'September 30, 2016 at 12:00 AM', 'n_rows': '8438'}, {'idx': 'GSPTSE', 'min_date_raw': '01 Apr 1981, 00:00', 'max_date_raw': 'September 30, 2016 at 12:00 AM', 'n_rows': '10526'}, {'idx': 'HSI', 'min_date_raw': '01 Apr 1992, 00:00', 'max_date_raw': 'September 30, 2019 at 12:00 AM', 'n_rows': '8492'}, {'idx': 'IXIC', 'min_date_raw': '01 Apr 1974, 00:00', 'max_date_raw': 'September 30, 2015 at 12:00 AM', 'n_rows': '12690'}, {'idx': 'J203.JO', 'min_date_raw': '01 Apr 2016, 00:00', 'max_date_raw': 'September 30, 2019 at 12:00 AM', 'n_rows': '2346'}, {'idx': 'N100', 'min_date_raw': '01 Apr 2003, 00:00', 'max_date_raw': 'September 30, 2019 at 12:00 AM', 'n_rows': '5474'}, {'idx': 'N225', 'min_date_raw': '01 Apr 1971, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n_rows': '13874'}, {'idx': 'NSEI', 'min_date_raw': '01 Apr 2014, 00:00', 'max_date_raw': 'September 30, 2014 at 12:00 AM', 'n_rows': '3346'}, {'idx': 'NYA', 'min_date_raw': '01 Apr 1969, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n_rows': '13947'}, {'idx': 'SSMI', 'min_date_raw': '01 Apr 1996, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n_rows': '7671'}, {'idx': 'TWII', 'min_date_raw': '01 Apr 2004, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n_rows': '5869'}], 'var_call_i2LDdMwKGuVq8c7OFcN6pg2B': [{'idx': 'HSI', 'date_raw': '1999-01-04 00:00:00', 'close_usd': '1275.19208986'}, {'idx': 'HSI', 'date_raw': 'January 05, 1999 at 12:00 AM', 'close_usd': '1285.8377441'}, {'idx': 'HSI', 'date_raw': '1999-01-06 00:00:00', 'close_usd': '1330.3939753000002'}, {'idx': 'HSI', 'date_raw': 'January 07, 1999 at 12:00 AM', 'close_usd': '1390.1641403'}, {'idx': 'HSI', 'date_raw': '1999-01-08 00:00:00', 'close_usd': '1393.951026'}], 'var_call_vL1QPMftdWbthrrxzfai5eNQ': 'file_storage/call_vL1QPMftdWbthrrxzfai5eNQ.json'}

exec(code, env_args)
