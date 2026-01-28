code = """import json, pandas as pd
from datetime import datetime

# load trade data
path = var_call_GxylZO4RB6rFzZPmkIFSP9V9
with open(path, 'r') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
# parse date robustly
s = df['Date'].astype(str)
dt = pd.to_datetime(s, errors='coerce', infer_datetime_format=True, utc=False)
# second pass for odd formats
mask = dt.isna()
if mask.any():
    dt2 = pd.to_datetime(s[mask].str.replace(' at 12:00 AM','', regex=False), errors='coerce', infer_datetime_format=True)
    dt.loc[mask] = dt2

df['dt'] = dt
# keep from 2000-01-01 onwards
start = pd.Timestamp('2000-01-01')
df = df[df['dt'].notna() & (df['dt']>=start)].copy()

df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df[df['CloseUSD'].notna()].copy()

# monthly DCA: invest $1 at first available trading day of each month, hold to last date.
end_dt = df.groupby('Index')['dt'].max()
end_price = df.sort_values('dt').groupby('Index').tail(1).set_index('Index')['CloseUSD']

# identify first trading day each month per index
# month period
df['month'] = df['dt'].dt.to_period('M')
first_each_month = df.sort_values('dt').groupby(['Index','month']).first().reset_index()

# for each index, compute shares bought each month: 1/price
first_each_month['inv'] = 1.0
first_each_month['shares'] = first_each_month['inv'] / first_each_month['CloseUSD']

agg = first_each_month.groupby('Index').agg(total_invested=('inv','sum'), total_shares=('shares','sum'), start_month=('month','min'), end_month=('month','max'), n_months=('inv','size'))
agg = agg.join(end_price.rename('end_price'))
agg['final_value'] = agg['total_shares'] * agg['end_price']
agg['multiple'] = agg['final_value'] / agg['total_invested']
agg = agg.sort_values('multiple', ascending=False)

top5 = agg.head(5).reset_index()

# map Index to country via known mapping from hint/exchanges list
index_to_country = {
    'NYA':'United States',
    'IXIC':'United States',
    'HSI':'Hong Kong',
    '000001.SS':'China',
    '399001.SZ':'China',
    'N225':'Japan',
    'GDAXI':'Germany',
    'GSPTSE':'Canada',
    'SSMI':'Switzerland',
    'N100':'Europe (Euronext)',
    'TWII':'Taiwan',
    'NSEI':'India',
    'J203.JO':'South Africa'
}

out = []
for _, r in top5.iterrows():
    out.append({
        'Index': r['Index'],
        'Country': index_to_country.get(r['Index']),
        'DCA_multiple': float(r['multiple']),
        'Months_invested': int(r['n_months']),
        'Final_date': str(end_dt[r['Index']].date())
    })

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_xveqCgWTM8HKeEGW1npxYnup': ['index_trade'], 'var_call_PNcXojW9JH0Kdwjwve4nDEXA': ['index_info'], 'var_call_fOQKtcZwSqNcuEiSDYSiFFC0': [{'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '2346'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13874'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '10526'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'n': '3346'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '8438'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '12690'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '8492'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13947'}, {'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5791'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '7671'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '5869'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '5474'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5760'}], 'var_call_wT22OL8rU5Wv2vPpgeP6Vrx7': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_GxylZO4RB6rFzZPmkIFSP9V9': 'file_storage/call_GxylZO4RB6rFzZPmkIFSP9V9.json'}

exec(code, env_args)
