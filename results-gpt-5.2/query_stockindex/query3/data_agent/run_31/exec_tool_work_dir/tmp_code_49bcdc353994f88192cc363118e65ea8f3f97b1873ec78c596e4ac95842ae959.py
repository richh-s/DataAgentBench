code = """import json, pandas as pd
from datetime import datetime

# Load trade data (may be a filepath)
trade_src = var_call_QOBVxFcpoxbXBm4Ylg6ascjW
if isinstance(trade_src, str):
    with open(trade_src, 'r') as f:
        trades = json.load(f)
else:
    trades = trade_src

df = pd.DataFrame(trades)
# Clean types
# CloseUSD may be string
if 'CloseUSD' in df.columns:
    df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

df['Date'] = pd.to_datetime(df['Date'])
df = df.dropna(subset=['CloseUSD'])
df = df.sort_values(['Index','Date'])

# Dollar-cost averaging: invest $1 on first available trading day of each month for each index
# Shares bought = 1 / price_on_invest_day
# Final value = total_shares * last_price
# Total invested = number_of_months_with_data * 1

df['YearMonth'] = df['Date'].dt.to_period('M')
first_in_month = df.groupby(['Index','YearMonth'], as_index=False).first()[['Index','YearMonth','CloseUSD','Date']]

# total shares per index
first_in_month['shares'] = 1.0 / first_in_month['CloseUSD']
shares = first_in_month.groupby('Index', as_index=False)['shares'].sum().rename(columns={'shares':'total_shares'})
months = first_in_month.groupby('Index', as_index=False).size().rename(columns={'size':'months_invested'})

last_price = df.groupby('Index', as_index=False).last()[['Index','CloseUSD','Date']].rename(columns={'CloseUSD':'last_price_usd','Date':'last_date'})

res = shares.merge(months, on='Index').merge(last_price, on='Index')
res['total_invested_usd'] = res['months_invested'] * 1.0
res['final_value_usd'] = res['total_shares'] * res['last_price_usd']
res['total_return_multiple'] = res['final_value_usd'] / res['total_invested_usd']
res = res.sort_values('total_return_multiple', ascending=False)

top5 = res.head(5).copy()

# Map index to country (and exchange) using known major index symbols
index_to_country = {
    '^GSPC': ('United States','New York Stock Exchange / S&P 500'),
    '^IXIC': ('United States','NASDAQ / Nasdaq Composite'),
    '^DJI': ('United States','New York Stock Exchange / Dow Jones Industrial Average'),
    'N225': ('Japan','Tokyo Stock Exchange / Nikkei 225'),
    'HSI': ('Hong Kong','Hong Kong Stock Exchange / Hang Seng'),
    '^HSI': ('Hong Kong','Hong Kong Stock Exchange / Hang Seng'),
    '000001.SS': ('China','Shanghai Stock Exchange / SSE Composite'),
    '399001.SZ': ('China','Shenzhen Stock Exchange / SZSE Component'),
    '^FTSE': ('United Kingdom','London Stock Exchange / FTSE 100'),
    '^GDAXI': ('Germany','Frankfurt Stock Exchange / DAX'),
    '^FCHI': ('France','Euronext Paris / CAC 40'),
    '^STOXX50E': ('Eurozone','Euronext / EURO STOXX 50'),
    '^NSEI': ('India','National Stock Exchange of India / NIFTY 50'),
    '^BSESN': ('India','BSE (India) / Sensex'),
    '^GSPTSE': ('Canada','Toronto Stock Exchange / S&P/TSX Composite'),
    '^KS11': ('South Korea','Korea Exchange / KOSPI'),
    '^TWII': ('Taiwan','Taiwan Stock Exchange / TAIEX'),
    '^SSMI': ('Switzerland','SIX Swiss Exchange / SMI'),
    '^JN0U.JO': ('South Africa','Johannesburg Stock Exchange'),
}

def lookup_country(idx):
    if idx in index_to_country:
        return index_to_country[idx][0]
    # heuristics
    if idx.endswith('.SS'):
        return 'China'
    if idx.endswith('.SZ'):
        return 'China'
    return None

def lookup_exchange(idx):
    if idx in index_to_country:
        return index_to_country[idx][1]
    return None

top5['Country'] = top5['Index'].map(lookup_country)
top5['Exchange/Index name'] = top5['Index'].map(lookup_exchange)

out = top5[['Index','Country','total_return_multiple','months_invested','last_date']].copy()
out['total_return_multiple'] = out['total_return_multiple'].round(4)
out['last_date'] = out['last_date'].astype(str)

print('__RESULT__:')
print(json.dumps(out.to_dict(orient='records')))"""

env_args = {'var_call_QOBVxFcpoxbXBm4Ylg6ascjW': 'file_storage/call_QOBVxFcpoxbXBm4Ylg6ascjW.json', 'var_call_hHa6C9Szwj2YXan7RZNOSlz5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
