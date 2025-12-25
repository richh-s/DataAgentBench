code = """import json, pandas as pd
from datetime import datetime

file_path = var_call_oZk204n1OTMSPRiO0E94hMs3
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# ensure proper types
df['Adj Close'] = pd.to_numeric(df['Adj Close'])

# parse dates flexibly
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# filter dates >= 2000-01-01
df = df[df['Date'] >= pd.Timestamp('2000-01-01')]

# monthly regular investment: $1 per month at last available trading day of each month

# sort and get month-end rows per index
df = df.sort_values(['Index', 'Date'])
df['year_month'] = df['Date'].dt.to_period('M')

month_end = df.groupby(['Index','year_month']).tail(1).copy()

# assume investing 1 unit of currency each month: shares bought = 1 / price
month_end['units'] = 1.0 / month_end['Adj Close']

agg = month_end.groupby('Index').agg(
    total_units = ('units','sum'),
    final_price = ('Adj Close', 'last'),
    n_months = ('units','size')
).reset_index()

agg['final_value'] = agg['total_units'] * agg['final_price']
agg['total_invested'] = agg['n_months'] * 1.0
agg['return_multiple'] = agg['final_value'] / agg['total_invested']

# keep indices that have data from 2000-01 month onwards
first_month = month_end.groupby('Index')['year_month'].min().reset_index(name='first_month')
agg = agg.merge(first_month, on='Index')
agg = agg[agg['first_month'] <= pd.Period('2000-01')]

Top5 = agg.sort_values('return_multiple', ascending=False).head(5)

result = Top5.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_cNzUQfttU7i6hoZg7kBhsZLf': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}], 'var_call_WTsldFx1Avw9TCL2I4x8wOxY': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'HSI'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_X0DzSD6LHO0gUEKxmY5m6gOu': ['index_info'], 'var_call_oZk204n1OTMSPRiO0E94hMs3': 'file_storage/call_oZk204n1OTMSPRiO0E94hMs3.json'}

exec(code, env_args)
