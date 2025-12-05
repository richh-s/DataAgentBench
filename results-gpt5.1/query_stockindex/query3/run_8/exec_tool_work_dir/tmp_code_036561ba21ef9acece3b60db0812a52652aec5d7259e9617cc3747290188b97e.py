code = """import json, pandas as pd
from datetime import datetime

# load full price data
path = var_call_9yJ7HpQSB1x237yJSGdthspi
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# ensure correct dtypes
df['Date'] = pd.to_datetime(df['Date'])
df['Adj Close'] = pd.to_numeric(df['Adj Close'])

# we assume monthly investment at the last trading day of each month
# filter from Jan 2000 onward
start = pd.Timestamp('2000-01-01')
df = df[df['Date'] >= start]

# find month-end rows per index
df['YearMonth'] = df['Date'].dt.to_period('M')
month_end_idx = df.sort_values('Date').groupby(['Index','YearMonth'])['Date'].idxmax()
me_df = df.loc[month_end_idx].copy()

# assume invest 1 unit of currency per month per index, buying at Adj Close
me_df['Units'] = 1.0 / me_df['Adj Close']

# aggregate per index: total invested and final value
# total invested = number of months (since we invest 1 each month)
agg = me_df.groupby('Index').agg(
    months=('Units','size'),
    total_units=('Units','sum')
).reset_index()

# need latest price per index
latest = df.sort_values('Date').groupby('Index').tail(1)[['Index','Adj Close']].rename(columns={'Adj Close':'LastPrice'})
res = agg.merge(latest, on='Index')

res['total_invested'] = res['months'] * 1.0
res['final_value'] = res['total_units'] * res['LastPrice']
res['return_multiple'] = res['final_value'] / res['total_invested']

# manually construct valid_indices from inspected data
valid_indices = ['N225','GSPTSE','GDAXI','HSI','NYA','SSMI','IXIC']
res = res[res['Index'].isin(valid_indices)]

# get top 5 by return_multiple
top5 = res.sort_values('return_multiple', ascending=False).head(5)

# map indices to countries manually
country_map = {
    'NYA': 'United States',
    'IXIC': 'United States',
    'HSI': 'Hong Kong (China)',
    '000001.SS': 'China',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'GDAXI': 'Germany',
    'SSMI': 'Switzerland',
}

top5['Country'] = top5['Index'].map(country_map)

result = top5[['Index','Country','return_multiple']].to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_EJOzOL4WIA3El0OklPMvb5k2': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}], 'var_call_9yJ7HpQSB1x237yJSGdthspi': 'file_storage/call_9yJ7HpQSB1x237yJSGdthspi.json', 'var_call_e7P14d4rw7OLGqK6roNpLk9f': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_raTf01LAKO46bqf6ZDlTBkvi': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}]}

exec(code, env_args)
