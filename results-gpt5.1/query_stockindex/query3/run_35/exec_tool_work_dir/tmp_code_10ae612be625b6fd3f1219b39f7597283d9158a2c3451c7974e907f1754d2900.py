code = """import json, pandas as pd

file_path = var_call_oZk204n1OTMSPRiO0E94hMs3
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# keep only rows from 2000 onwards using string year prefix
mask_2000 = df['Date'].str[-14:].str[-4:]  # attempt but unreliable

# Instead, parse year safely: last 14 chars are 'YYYY, 00:00'
# Example: '01 Jan 2000, 00:00' -> year is at position -10:-6
years = df['Date'].str[-12:-8]
years = pd.to_numeric(years, errors='coerce')

df = df[years >= 2000].copy()

# convert Adj Close
df['Adj Close'] = pd.to_numeric(df['Adj Close'])

# extract year-month as string: first 6 chars 'DD Mon ' plus year, we take 'Mon YYYY'
months = df['Date'].str[3:6]
years = df['Date'].str[-12:-8]
df['year_month'] = years + '-' + months

# To sort by calendar order, map months
month_map = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
df['ym_sort'] = years + '-' + months.map(month_map)

# sort
df = df.sort_values(['Index','ym_sort','Date'])

# get last row per Index-year_month combination
month_end = df.groupby(['Index','year_month']).tail(1).copy()

month_end['units'] = 1.0 / month_end['Adj Close']

agg = month_end.groupby('Index').agg(
    total_units=('units','sum'),
    final_price=('Adj Close','last'),
    n_months=('units','size')
).reset_index()

agg['final_value'] = agg['total_units'] * agg['final_price']
agg['total_invested'] = agg['n_months'] * 1.0
agg['return_multiple'] = agg['final_value'] / agg['total_invested']

# determine first month per index
first_month = month_end.groupby('Index')['ym_sort'].min().reset_index(name='first_ym')
agg = agg.merge(first_month, on='Index')

# keep those with data from at most 2000-01
agg = agg[agg['first_ym'] <= '2000-01']

Top5 = agg.sort_values('return_multiple', ascending=False).head(5)

result = Top5.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_cNzUQfttU7i6hoZg7kBhsZLf': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}], 'var_call_WTsldFx1Avw9TCL2I4x8wOxY': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'HSI'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_X0DzSD6LHO0gUEKxmY5m6gOu': ['index_info'], 'var_call_oZk204n1OTMSPRiO0E94hMs3': 'file_storage/call_oZk204n1OTMSPRiO0E94hMs3.json'}

exec(code, env_args)
