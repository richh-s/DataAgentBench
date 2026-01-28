code = """import json, pandas as pd

path = var_call_xN7QGS8DGTDZccYycOsH3Mw7
with open(path, 'r') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
# robust datetime parsing
s = df['Date'].astype(str).str.replace(' 00:00:00','', regex=False)
df['Date'] = pd.to_datetime(s, errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['Date','CloseUSD'])
df = df[df['Date'] >= pd.Timestamp('2000-01-01')]

m = df.copy()
m['Month'] = m['Date'].dt.to_period('M')
m = m.sort_values(['Index','Date'])
firsts = m.groupby(['Index','Month'], as_index=False).first()[['Index','Month','CloseUSD']]

firsts['shares_bought'] = 1.0 / firsts['CloseUSD']
agg = firsts.groupby('Index').agg(
    months=('Month','nunique'),
    total_shares=('shares_bought','sum'),
    last_month=('Month','max')
).reset_index()

last_price = df.sort_values(['Index','Date']).groupby('Index', as_index=False).last()[['Index','CloseUSD','Date']]
last_price = last_price.rename(columns={'CloseUSD':'final_price','Date':'final_date'})

res = agg.merge(last_price, on='Index', how='left')
res['total_invested'] = res['months'].astype(float)
res['final_value'] = res['total_shares'] * res['final_price']
res['return_multiple'] = res['final_value'] / res['total_invested']
res['total_return_pct'] = (res['return_multiple'] - 1.0) * 100.0

first_month = firsts.groupby('Index', as_index=False)['Month'].min().rename(columns={'Month':'start_month'})
res = res.merge(first_month, on='Index', how='left')
res_2000 = res[res['start_month'] <= pd.Period('2000-01')].copy()

res_top = res_2000.sort_values('return_multiple', ascending=False).head(5).copy()

index_to_country = {
    '^GSPC': 'United States',
    '^IXIC': 'United States',
    '^DJI': 'United States',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'N225': 'Japan',
    '^N225': 'Japan',
    '^GDAXI': 'Germany',
    '^FCHI': 'France',
    '^NSEI': 'India',
    '^KS11': 'South Korea',
    '^TWII': 'Taiwan',
    '^GSPTSE': 'Canada',
    '^SSMI': 'Switzerland',
    '^JN0U.JO': 'South Africa',
}
res_top['Country'] = res_top['Index'].map(index_to_country)

out = res_top[['Index','Country','return_multiple','total_return_pct']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out, default=str))"""

env_args = {'var_call_xN7QGS8DGTDZccYycOsH3Mw7': 'file_storage/call_xN7QGS8DGTDZccYycOsH3Mw7.json', 'var_call_aMRtFzom1Dse7n6ySG0WwHl3': ['index_info'], 'var_call_O8PCIru3pEzeo822r5WHCMD0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
