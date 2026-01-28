code = """import json, pandas as pd
from datetime import datetime

# Load large trades result
path = var_call_SOCR7KF6SHlRigK0hICWNxCP
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)

# Parse dates with mixed formats
s = df['Date'].astype(str)
# Try multiple formats
fmts = [
    '%d %b %Y, %H:%M',
    '%B %d, %Y at %I:%M %p',
]
parsed = pd.to_datetime(pd.NaT)
# iterative parse
out = pd.to_datetime(pd.Series([pd.NaT]*len(s)))
for fmt in fmts:
    mask = out.isna()
    out.loc[mask] = pd.to_datetime(s[mask], format=fmt, errors='coerce')
# fallback
mask = out.isna()
out.loc[mask] = pd.to_datetime(s[mask], errors='coerce')

df['date'] = out

df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['date','CloseUSD'])

# Filter since 2000-01-01
start = pd.Timestamp('2000-01-01')
df = df[df['date'] >= start]

# Monthly DCA: invest 1 unit each month at first available trading day close
# For each index/month, pick earliest date

df['month'] = df['date'].dt.to_period('M')
firsts = df.sort_values(['Index','date']).groupby(['Index','month'], as_index=False).first()

# For each index, compute shares bought per month with $1 contribution
firsts['shares'] = 1.0 / firsts['CloseUSD']
agg = firsts.groupby('Index').agg(months=('shares','size'), total_shares=('shares','sum')).reset_index()

# Get last available CloseUSD per index
lasts = df.sort_values(['Index','date']).groupby('Index', as_index=False).last()[['Index','CloseUSD','date']]
lasts = lasts.rename(columns={'CloseUSD':'last_close_usd','date':'last_date'})

res = agg.merge(lasts, on='Index', how='inner')
res['final_value'] = res['total_shares'] * res['last_close_usd']
res['total_contrib'] = res['months'] * 1.0
res['total_return_mult'] = res['final_value'] / res['total_contrib']
res['total_return_pct'] = (res['total_return_mult'] - 1.0) * 100.0

# Map index to country via known mapping from hint/exchanges
index_country = {
    'NYA': 'United States',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'N225': 'Japan',
    'N100': 'Europe (Euronext)',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'NSEI': 'India',
    'J203.JO': 'South Africa',
}
res['country'] = res['Index'].map(index_country)

# Top 5 by total_return_mult
res_top5 = res.sort_values('total_return_mult', ascending=False).head(5)

out = res_top5[['Index','country','months','last_date','total_return_mult','total_return_pct']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out, default=str))"""

env_args = {'var_call_X7U4PaHYoNz0cxBLZOjfkfw3': ['index_info'], 'var_call_RmGz0DEtqY53VNrpYG4tUIz0': ['index_trade'], 'var_call_dOuhG1kPaGpv0MHydvmaUKYD': [{'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '2346'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '12690'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '8492'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13947'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '5474'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5760'}, {'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5791'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '7671'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '5869'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13874'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '10526'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'n': '3346'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '8438'}], 'var_call_SOCR7KF6SHlRigK0hICWNxCP': 'file_storage/call_SOCR7KF6SHlRigK0hICWNxCP.json', 'var_call_LjTrjfbPFsm8YZdV0LuJltPi': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
