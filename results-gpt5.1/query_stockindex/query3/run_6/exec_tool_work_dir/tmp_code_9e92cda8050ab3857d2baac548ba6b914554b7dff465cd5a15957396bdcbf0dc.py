code = """import json, pandas as pd

path = var_call_NrE17zvlczzburZ6OeqKqH3S
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Adj Close'] = df['Adj Close'].astype(float)

# coerce dates robustly
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

first_per_month = df.sort_values(['Index','Date']).groupby(['Index', df['Date'].dt.to_period('M')]).first().reset_index()
first_per_month['units_bought'] = 1.0 / first_per_month['Adj Close']

units_per_index = first_per_month.groupby('Index')['units_bought'].sum().reset_index(name='total_units')

last_price = df.sort_values(['Index','Date']).groupby('Index').tail(1)[['Index','Adj Close']].rename(columns={'Adj Close':'last_price'})

res = pd.merge(units_per_index, last_price, on='Index')
res['final_value'] = res['total_units'] * res['last_price']
months = first_per_month.groupby('Index')['Date'].size().rename('months')
res = res.merge(months, on='Index')
res['total_invested'] = res['months'] * 1.0
res['return_multiple'] = res['final_value'] / res['total_invested']

TopN = res.sort_values('return_multiple', ascending=False).head(5).copy()

country_map = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    '^GSPC': 'United States',
    '^DJI': 'United States',
    '^IXIC': 'United States',
    '^GDAXI': 'Germany',
    '^FCHI': 'France',
    '^STOXX50E': 'Eurozone',
    '^FTSE': 'United Kingdom',
    '^BSESN': 'India',
    '^TWII': 'Taiwan',
    '^KS11': 'South Korea',
    '^SSMI': 'Switzerland',
    'GSPTSE': 'Canada',
}

TopN['Country'] = TopN['Index'].map(country_map).fillna('Unknown')

result = TopN[['Index','Country','return_multiple']].to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_NrE17zvlczzburZ6OeqKqH3S': 'file_storage/call_NrE17zvlczzburZ6OeqKqH3S.json', 'var_call_SICaeCttm2fLewnw0ns7MnOQ': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
