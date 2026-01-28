code = """import json, pandas as pd

# Load large trade data
path = var_call_JVhJ92G9JGSCLoatiN2vgOI7
with open(path, 'r', encoding='utf-8') as f:
    trade = json.load(f)

df = pd.DataFrame(trade)
# parse
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

# Monthly DCA: invest 1 unit each month at month-end CloseUSD (last available trading day of month)
# Shares bought = 1 / price
# Final value = total_shares * last_price; total_invested = number_of_months

df['Month'] = df['Date'].dt.to_period('M')
# get month-end close (last trading day in month)
month_end = (df.sort_values(['Index','Date'])
              .groupby(['Index','Month'], as_index=False)
              .tail(1))

# For each index: use months starting from 2000-01 to last available month, continuous only where data exists
# Compute shares and final value based on last available price
month_end = month_end.sort_values(['Index','Month'])
month_end['inv'] = 1.0
month_end['shares_bought'] = month_end['inv'] / month_end['CloseUSD']

agg = month_end.groupby('Index').agg(
    months=('Month','nunique'),
    total_shares=('shares_bought','sum'),
    last_price=('CloseUSD','last')
).reset_index()
agg['total_invested'] = agg['months'] * 1.0
agg['final_value'] = agg['total_shares'] * agg['last_price']
agg['multiple'] = agg['final_value'] / agg['total_invested']
agg = agg.sort_values('multiple', ascending=False)

# Map index symbols to countries/exchanges via known major index mapping
index_to_country = {
    'N225': {'country':'Japan','exchange':'Tokyo Stock Exchange'},
    '^GSPC': {'country':'United States','exchange':'New York Stock Exchange'},
    '^IXIC': {'country':'United States','exchange':'NASDAQ'},
    'HSI': {'country':'Hong Kong','exchange':'Hong Kong Stock Exchange'},
    '000001.SS': {'country':'China','exchange':'Shanghai Stock Exchange'},
    '399001.SZ': {'country':'China','exchange':'Shenzhen Stock Exchange'},
    '^FCHI': {'country':'France','exchange':'Euronext'},
    '^GDAXI': {'country':'Germany','exchange':'Frankfurt Stock Exchange'},
    '^GSPTSE': {'country':'Canada','exchange':'Toronto Stock Exchange'},
    '^NSEI': {'country':'India','exchange':'National Stock Exchange of India'},
    '^KS11': {'country':'South Korea','exchange':'Korea Exchange'},
    '^SSMI': {'country':'Switzerland','exchange':'SIX Swiss Exchange'},
    '^TWII': {'country':'Taiwan','exchange':'Taiwan Stock Exchange'},
    '^JN0U.JO': {'country':'South Africa','exchange':'Johannesburg Stock Exchange'},
}

top5 = agg.head(5).copy()
top5['country'] = top5['Index'].map(lambda x: index_to_country.get(x, {}).get('country'))

# format output records
out = top5[['Index','multiple','months','country']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_JVhJ92G9JGSCLoatiN2vgOI7': 'file_storage/call_JVhJ92G9JGSCLoatiN2vgOI7.json', 'var_call_04afrWAiSFqiaaZnCOubWdpU': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
