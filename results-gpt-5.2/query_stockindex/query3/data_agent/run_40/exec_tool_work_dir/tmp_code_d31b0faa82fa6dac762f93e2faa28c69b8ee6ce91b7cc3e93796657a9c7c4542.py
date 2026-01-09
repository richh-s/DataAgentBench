code = """import json, pandas as pd

# Load large trade data
path = var_call_xN7QGS8DGTDZccYycOsH3Mw7
with open(path, 'r') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
# types
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

# monthly contribution at each index's first available trading day of each month
# create month period
m = df.copy()
m['Month'] = m['Date'].dt.to_period('M')
# first trading day in month per index
m = m.sort_values(['Index','Date'])
firsts = m.groupby(['Index','Month'], as_index=False).first()[['Index','Month','CloseUSD']]

# compute DCA shares with $1 each month
firsts['shares_bought'] = 1.0 / firsts['CloseUSD']
agg = firsts.groupby('Index').agg(
    months=('Month','nunique'),
    total_invested=('shares_bought', lambda s: float(len(s))),
    total_shares=('shares_bought','sum'),
    last_month=('Month','max')
).reset_index()

# get final price as last available CloseUSD per index
last_price = df.sort_values(['Index','Date']).groupby('Index', as_index=False).last()[['Index','CloseUSD','Date']]
last_price = last_price.rename(columns={'CloseUSD':'final_price','Date':'final_date'})

res = agg.merge(last_price, on='Index', how='left')
res['final_value'] = res['total_shares'] * res['final_price']
res['total_invested'] = res['months'].astype(float)  # 1 USD per month
res['return_multiple'] = res['final_value'] / res['total_invested']
res['total_return_pct'] = (res['return_multiple'] - 1.0) * 100.0

# ensure started since 2000: require first month == 2000-01
first_month = firsts.groupby('Index', as_index=False)['Month'].min().rename(columns={'Month':'start_month'})
res = res.merge(first_month, on='Index', how='left')
res_2000 = res[res['start_month'] <= pd.Period('2000-01')].copy()

# pick top 5 by return multiple
res_top = res_2000.sort_values('return_multiple', ascending=False).head(5).copy()

# map indices to exchanges/countries (manual mapping based on common major indices)
index_to_exchange_country = {
    '^GSPC': ('New York Stock Exchange', 'United States'),
    '^IXIC': ('NASDAQ', 'United States'),
    '^DJI': ('New York Stock Exchange', 'United States'),
    'HSI': ('Hong Kong Stock Exchange', 'Hong Kong'),
    '000001.SS': ('Shanghai Stock Exchange', 'China'),
    '399001.SZ': ('Shenzhen Stock Exchange', 'China'),
    'N225': ('Tokyo Stock Exchange', 'Japan'),
    '^N225': ('Tokyo Stock Exchange', 'Japan'),
    '^FTSE': ('London Stock Exchange', 'United Kingdom'),
    '^GDAXI': ('Frankfurt Stock Exchange', 'Germany'),
    '^FCHI': ('Euronext', 'France'),
    '^STI': ('Singapore Exchange', 'Singapore'),
    '^BSESN': ('BSE India', 'India'),
    '^NSEI': ('National Stock Exchange of India', 'India'),
    '^KS11': ('Korea Exchange', 'South Korea'),
    '^TWII': ('Taiwan Stock Exchange', 'Taiwan'),
    '^GSPTSE': ('Toronto Stock Exchange', 'Canada'),
    '^SSMI': ('SIX Swiss Exchange', 'Switzerland'),
    '^JN0U.JO': ('Johannesburg Stock Exchange', 'South Africa'),
}

res_top['Exchange'] = res_top['Index'].map(lambda x: index_to_exchange_country.get(x, (None,None))[0])
res_top['Country'] = res_top['Index'].map(lambda x: index_to_exchange_country.get(x, (None,None))[1])

out = res_top[['Index','Country','return_multiple','total_return_pct','months','final_date']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out, default=str))"""

env_args = {'var_call_xN7QGS8DGTDZccYycOsH3Mw7': 'file_storage/call_xN7QGS8DGTDZccYycOsH3Mw7.json', 'var_call_aMRtFzom1Dse7n6ySG0WwHl3': ['index_info'], 'var_call_O8PCIru3pEzeo822r5WHCMD0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
