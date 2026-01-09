code = """import json, pandas as pd
from datetime import datetime

# load large json list
path = var_call_KwRVe1RvsF0ea8b5VZVKCHUL
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# parse dates with mixed formats
s = df['Date'].astype(str)
# normalize ' at 12:00 AM'
s = s.str.replace(r'\s+at\s+12:00\s+AM\s*$', '', regex=True)

fmts = ["%d %b %Y, %H:%M", "%B %d, %Y", "%d %b %Y", "%b %d %Y, %H:%M", "%Y-%m-%d"]

def try_parse(x):
    for fmt in fmts:
        try:
            return datetime.strptime(x, fmt)
        except Exception:
            pass
    return None

parsed = s.map(try_parse)
df = df.assign(dt=parsed)
df = df[df['dt'].notna()].copy()

df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df[df['CloseUSD'].notna()].copy()

df = df[df['dt'] >= pd.Timestamp('2000-01-01')].copy()

# monthly contributions: invest 1 unit on first trading day of each month
# shares bought = 1 / price
# final value = sum(shares)*last_price; total invested = n_months

df = df.sort_values(['Index','dt'])
df['month'] = df['dt'].dt.to_period('M').astype(str)
first_days = df.groupby(['Index','month'], as_index=False).first()
first_days['shares'] = 1.0 / first_days['CloseUSD']
shares = first_days.groupby('Index', as_index=False)['shares'].sum().rename(columns={'shares':'total_shares'})
last = df.groupby('Index', as_index=False).last()[['Index','CloseUSD','dt']].rename(columns={'CloseUSD':'last_price','dt':'last_date'})
inv = first_days.groupby('Index', as_index=False).size().rename(columns={'size':'months_invested'})
res = shares.merge(inv, on='Index').merge(last, on='Index')
res['total_invested'] = res['months_invested'] * 1.0
res['final_value'] = res['total_shares'] * res['last_price']
res['overall_return_multiple'] = res['final_value'] / res['total_invested']
res = res.sort_values('overall_return_multiple', ascending=False)

# top 5 indices
out = res.head(5)[['Index','overall_return_multiple','months_invested','last_date']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out, default=str))"""

env_args = {'var_call_IQw038LXdeVI95KVq3Mdzg2F': ['index_info'], 'var_call_aYQMZRH4VMisJJFJwPksBzAv': ['index_trade'], 'var_call_zxM3mfHEjBOGwDFynqF5e7Lg': [{'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13947'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13874'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '12690'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '10526'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '8492'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '8438'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '7671'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '5869'}, {'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5791'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5760'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '5474'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'n': '3346'}, {'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '2346'}], 'var_call_KwRVe1RvsF0ea8b5VZVKCHUL': 'file_storage/call_KwRVe1RvsF0ea8b5VZVKCHUL.json'}

exec(code, env_args)
