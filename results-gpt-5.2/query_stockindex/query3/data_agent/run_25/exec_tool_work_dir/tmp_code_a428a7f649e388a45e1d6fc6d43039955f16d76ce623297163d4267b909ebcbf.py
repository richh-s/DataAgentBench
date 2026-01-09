code = """import json, pandas as pd
from datetime import datetime

# load trade data
path = var_call_3mpIPZn3tDW7P4ParJwHNDUR
with open(path,'r') as f:
    recs = json.load(f)
df = pd.DataFrame(recs)

df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

def parse_date(x):
    if x is None:
        return pd.NaT
    for fmt in ['%d %b %Y, %H:%M','%B %d, %Y at %I:%M %p','%b %d %Y, %H:%M','%d %B %Y, %H:%M','%Y-%m-%d']:
        try:
            return pd.Timestamp(datetime.strptime(x, fmt))
        except Exception:
            pass
    return pd.to_datetime(x, errors='coerce')

df['Date'] = df['Date'].apply(parse_date)

df = df.dropna(subset=['Date','CloseUSD'])
df = df[df['Date'] >= pd.Timestamp('2000-01-01')]

# monthly DCA: invest 1 unit at first trading day each month
idx_month = df.sort_values('Date').groupby(['Index', df['Date'].dt.to_period('M')]).first().reset_index(level=1, drop=True)
# idx_month has Date and CloseUSD columns with first day per month

# compute shares and final value
last = df.sort_values('Date').groupby('Index').last()[['CloseUSD']].rename(columns={'CloseUSD':'last_close'})
first_monthly = idx_month.groupby('Index')['CloseUSD'].apply(list)

results = []
for idx, prices in first_monthly.items():
    prices = [p for p in prices if pd.notna(p) and p>0]
    if len(prices)==0 or idx not in last.index:
        continue
    shares = sum(1.0/p for p in prices)  # invest $1 each month
    total_invested = len(prices)*1.0
    final_value = shares * float(last.loc[idx,'last_close'])
    multiple = final_value/total_invested if total_invested else None
    results.append({'Index': idx, 'months': len(prices), 'invested': total_invested, 'final_value': final_value, 'multiple': multiple})

resdf = pd.DataFrame(results)
resdf = resdf.sort_values(['multiple','final_value'], ascending=False)

top5 = resdf.head(5)

# map index to country using known major indices
country_map = {
    'NYA':'United States',
    'IXIC':'United States',
    'N225':'Japan',
    'HSI':'Hong Kong',
    '000001.SS':'China',
    '399001.SZ':'China',
    'GDAXI':'Germany',
    'GSPTSE':'Canada',
    'SSMI':'Switzerland',
    'TWII':'Taiwan',
    'N100':'Europe (Euronext)',
    'J203.JO':'South Africa',
    'NSEI':'India'
}

top5['Country'] = top5['Index'].map(country_map)

out = top5[['Index','Country','multiple','months']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_iWMPpGD0lvENZAOkcMLrrEPh': ['index_trade'], 'var_call_wf7hC1gBbiKdwi3oFjEx6CNF': ['index_info'], 'var_call_9qIzXlOkyV8kolAb2ksyYIHD': [{'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '2346'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '12690'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '8492'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13947'}, {'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5791'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '7671'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '5869'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '5474'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5760'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13874'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '10526'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'n': '3346'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '8438'}], 'var_call_FUahmlibxYISEACKFY6s0Aqt': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_3mpIPZn3tDW7P4ParJwHNDUR': 'file_storage/call_3mpIPZn3tDW7P4ParJwHNDUR.json'}

exec(code, env_args)
