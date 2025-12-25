code = """import pandas as pd, json

first_dates = pd.DataFrame(var_call_3Y35E48JpUeGsxVC8WeNKuU6)
valid_indices = first_dates[first_dates['first_date'] <= '01 Feb 2000, 00:00']['Index'].tolist()

import os, json as js
path = var_call_wZ39U6U92veAyvRXOlPdID4G
with open(path, 'r') as f:
    data = js.load(f)

df = pd.DataFrame(data)
df = df[df['Index'].isin(valid_indices)].copy()

# normalize date
from dateutil import parser

# dateutil may not be available; instead, leave as string and group by year-month using tail 4 digits for year etc.

# We'll assume formats always include year as last 4 chars before optional time

def to_ym(s):
    s = str(s)
    # find 4-digit year
    import re
    m = re.search(r'(19|20)\d{2}', s)
    if not m:
        return None
    year = int(m.group(0))
    # find month by name or number
    months = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12,
              'Jan':1,'Feb':2,'Mar':3,'Apr':4,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    for name, num in months.items():
        if name in s:
            month = num
            break
    else:
        # try numeric at start
        import re
        m2 = re.match(r'\d{2}', s)
        month = int(m2.group(0)) if m2 else 1
    return f"{year:04d}-{month:02d}"


df['ym'] = df['Date'].apply(to_ym)
df = df[df['ym'] >= '2000-01']

# sort and take last date per index-month as investment day (end of month)
df_sorted = df.sort_values(['Index','ym','Date'])
last_per_month = df_sorted.groupby(['Index','ym']).tail(1)

# assume invest 1 unit of currency per month; units bought = 1 / Adj Close
last_per_month['Adj Close'] = last_per_month['Adj Close'].astype(float)
last_per_month['units'] = 1.0 / last_per_month['Adj Close']

# total units per index
units = last_per_month.groupby('Index')['units'].sum().reset_index(name='total_units')

# get final price per index (latest date overall)
latest = df.sort_values(['Index','Date']).groupby('Index').tail(1)[['Index','Adj Close']].rename(columns={'Adj Close':'final_price'})
latest['final_price'] = latest['final_price'].astype(float)

res = units.merge(latest, on='Index')
res['final_value'] = res['total_units'] * res['final_price']
res['months'] = last_per_month.groupby('Index')['ym'].nunique().values
res['total_invested'] = res['months'] * 1.0
res['return_multiple'] = res['final_value'] / res['total_invested']

res_top5 = res.sort_values('return_multiple', ascending=False).head(5)

result = res_top5[['Index','return_multiple']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_call_3Y35E48JpUeGsxVC8WeNKuU6': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}], 'var_call_wZ39U6U92veAyvRXOlPdID4G': 'file_storage/call_wZ39U6U92veAyvRXOlPdID4G.json'}

exec(code, env_args)
