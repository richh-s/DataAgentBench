code = """import json, pandas as pd

trade_src = var_call_QOBVxFcpoxbXBm4Ylg6ascjW
if isinstance(trade_src, str):
    with open(trade_src, 'r') as f:
        trades = json.load(f)
else:
    trades = trade_src

df = pd.DataFrame(trades)
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# Dates appear like '2000-01-04 00:00:00'
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date','CloseUSD'])
df = df.sort_values(['Index','Date'])

df['YearMonth'] = df['Date'].dt.to_period('M')
first_in_month = df.groupby(['Index','YearMonth'], as_index=False).first()[['Index','YearMonth','CloseUSD','Date']]
first_in_month['shares'] = 1.0 / first_in_month['CloseUSD']

shares = first_in_month.groupby('Index', as_index=False)['shares'].sum().rename(columns={'shares':'total_shares'})
months = first_in_month.groupby('Index', as_index=False).size().rename(columns={'size':'months_invested'})
last_price = df.groupby('Index', as_index=False).last()[['Index','CloseUSD','Date']].rename(columns={'CloseUSD':'last_price_usd','Date':'last_date'})

res = shares.merge(months, on='Index').merge(last_price, on='Index')
res['total_invested_usd'] = res['months_invested'].astype(float)
res['final_value_usd'] = res['total_shares'] * res['last_price_usd']
res['total_return_multiple'] = res['final_value_usd'] / res['total_invested_usd']
res = res.sort_values('total_return_multiple', ascending=False)

top5 = res.head(5).copy()

index_to_country = {
    '^GSPC': ('United States','S&P 500 (NYSE/US)'),
    '^IXIC': ('United States','Nasdaq Composite (NASDAQ/US)'),
    '^DJI': ('United States','Dow Jones Industrial Average (US)'),
    'N225': ('Japan','Nikkei 225 (Tokyo)'),
    'HSI': ('Hong Kong','Hang Seng (Hong Kong)'),
    '^HSI': ('Hong Kong','Hang Seng (Hong Kong)'),
    '000001.SS': ('China','SSE Composite (Shanghai)'),
    '399001.SZ': ('China','SZSE Component (Shenzhen)'),
    '^FTSE': ('United Kingdom','FTSE 100 (London)'),
    '^GDAXI': ('Germany','DAX (Frankfurt)'),
    '^FCHI': ('France','CAC 40 (Euronext Paris)'),
    '^STOXX50E': ('Eurozone','EURO STOXX 50 (Euronext)'),
    '^NSEI': ('India','NIFTY 50 (NSE India)'),
    '^BSESN': ('India','SENSEX (BSE India)'),
    '^GSPTSE': ('Canada','S&P/TSX (Toronto)'),
    '^KS11': ('South Korea','KOSPI (Korea Exchange)'),
    '^TWII': ('Taiwan','TAIEX (Taiwan)'),
    '^SSMI': ('Switzerland','SMI (SIX Swiss)'),
}

def country(idx):
    if idx in index_to_country:
        return index_to_country[idx][0]
    if isinstance(idx,str) and idx.endswith('.SS'):
        return 'China'
    if isinstance(idx,str) and idx.endswith('.SZ'):
        return 'China'
    return None

top5['Country'] = top5['Index'].map(country)

out = top5[['Index','Country','total_return_multiple','months_invested','last_date']].copy()
out['total_return_multiple'] = out['total_return_multiple'].round(4)
out['last_date'] = out['last_date'].dt.strftime('%Y-%m-%d')

print('__RESULT__:')
print(json.dumps(out.to_dict(orient='records')))"""

env_args = {'var_call_QOBVxFcpoxbXBm4Ylg6ascjW': 'file_storage/call_QOBVxFcpoxbXBm4Ylg6ascjW.json', 'var_call_hHa6C9Szwj2YXan7RZNOSlz5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
