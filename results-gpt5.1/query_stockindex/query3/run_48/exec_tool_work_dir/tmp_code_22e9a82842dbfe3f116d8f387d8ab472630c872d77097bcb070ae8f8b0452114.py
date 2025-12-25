code = """import json, pandas as pd
from datetime import datetime

path = var_call_EqEOCpZ72kUvZw3RgZNY2IhN
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse Date more robustly
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', utc=False, infer_datetime_format=True)
# Drop rows with invalid dates
df = df.dropna(subset=['Date'])

df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

start = pd.Timestamp('2000-01-01')
df = df[df['Date'] >= start]

df['year_month'] = df['Date'].dt.to_period('M')

last_days = df.sort_values('Date').groupby(['Index','year_month']).tail(1)

last_days['shares'] = 1.0 / last_days['CloseUSD']

final_price = df.sort_values('Date').groupby('Index').tail(1)[['Index','CloseUSD']].set_index('Index')['CloseUSD']

agg = last_days.groupby('Index')['shares'].sum().to_frame('total_shares')
agg['months'] = last_days.groupby('Index').size()
agg['final_price'] = final_price
agg = agg.dropna()

agg['total_invested'] = agg['months'] * 1.0
agg['final_value'] = agg['total_shares'] * agg['final_price']
agg['return_multiple'] = agg['final_value'] / agg['total_invested']

top5 = agg.sort_values('return_multiple', ascending=False).head(5).reset_index()

country_map = {
    'IXIC': 'United States',
    'NYA': 'United States',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'N100': 'Eurozone',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'J203.JO': 'South Africa',
}

top5['Country'] = top5['Index'].map(country_map)

result = top5[['Index','Country','return_multiple']].to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_sCstXjUWzB0740rTzc4sv3Nw': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_Ivca6rx8BwEo9aAaDcTpoVoM': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}], 'var_call_EqEOCpZ72kUvZw3RgZNY2IhN': 'file_storage/call_EqEOCpZ72kUvZw3RgZNY2IhN.json', 'var_call_WzXorspHQPtiTVBP2gmy96hZ': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
