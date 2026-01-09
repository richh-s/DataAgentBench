code = """import json, pandas as pd

trade_src = var_call_yLEqysLvcLFy5q5ogsDokRKE
if isinstance(trade_src, str):
    with open(trade_src, 'r') as f:
        trade = json.load(f)
else:
    trade = trade_src

df = pd.DataFrame(trade)

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['Date','CloseUSD'])

monthly = (df.sort_values(['Index','Date'])
             .assign(YearMonth=lambda x: x['Date'].dt.to_period('M'))
             .groupby(['Index','YearMonth'], as_index=False)
             .tail(1))

monthly['shares'] = 1.0 / monthly['CloseUSD']

g = monthly.groupby('Index').agg(
    total_contrib=('shares','size'),
    total_shares=('shares','sum'),
    last_price=('CloseUSD','last')
).reset_index()

g['final_value'] = g['total_shares'] * g['last_price']
g['overall_return_multiple'] = g['final_value'] / g['total_contrib']

g = g.sort_values('overall_return_multiple', ascending=False)

index_country = {
    '^GSPC': 'United States',
    '^IXIC': 'United States',
    '^DJI': 'United States',
    'HSI': 'Hong Kong',
    '^HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'N225': 'Japan',
    '^N225': 'Japan',
    '^FCHI': 'France',
    '^GDAXI': 'Germany',
    'DAX': 'Germany',
    '^NSEI': 'India',
    '^GSPTSE': 'Canada',
    '^KS11': 'South Korea',
    '^SSMI': 'Switzerland',
    '^TWII': 'Taiwan',
    '^JN0U.JO': 'South Africa',
}

top5 = g.head(5).copy()
top5['Country'] = top5['Index'].map(index_country).fillna('Unknown')

out = top5[['Index','overall_return_multiple','Country']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_yLEqysLvcLFy5q5ogsDokRKE': 'file_storage/call_yLEqysLvcLFy5q5ogsDokRKE.json', 'var_call_rjr7nTeDTr2TPNINZNtzjKhk': ['index_info'], 'var_call_AYSYWAtWG7s9sDyAbJGpxYwX': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
