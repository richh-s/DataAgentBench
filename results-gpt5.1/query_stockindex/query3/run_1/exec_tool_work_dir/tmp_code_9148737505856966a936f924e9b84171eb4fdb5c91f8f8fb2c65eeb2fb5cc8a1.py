code = """import json, pandas as pd
from datetime import datetime

# Load full price data
file_path = var_call_Cn08Wm4XExxUGOWwF0Qb54ni
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Normalize Date to actual datetime and filter from 2000-01-01
def parse_date(x):
    for fmt in ['%Y-%m-%d', '%d %b %Y, %H:%M', '%B %d, %Y at %I:%M %p']:
        try:
            return datetime.strptime(x, fmt)
        except Exception:
            continue
    # Try more flexible parsing
    try:
        return pd.to_datetime(x)
    except Exception:
        return pd.NaT

df['Date'] = df['Date'].apply(parse_date)
df = df[df['Date'] >= pd.Timestamp('2000-01-01')].copy()

# Ensure CloseUSD is float
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

# We assume monthly regular investments: invest same amount at first trading day of each month for each index.
# So for each index and each month, use the first available CloseUSD as the "price".

df['year_month'] = df['Date'].dt.to_period('M')

first_prices = df.sort_values('Date').groupby(['Index','year_month']).first().reset_index()

# Assume invest $1 each month per index; number of units bought that month = 1 / price.
first_prices['units'] = 1.0 / first_prices['CloseUSD']

# Total units accumulated per index
units_by_index = first_prices.groupby('Index')['units'].sum().reset_index()

# Get last available price per index
last_prices = df.sort_values('Date').groupby('Index').tail(1)[['Index','CloseUSD']].rename(columns={'CloseUSD':'last_price'})

result = units_by_index.merge(last_prices, on='Index', how='inner')

# Final value = total units * last_price; total invested = number of months (i.e., rows in first_prices) per index.
months_per_index = first_prices.groupby('Index').size().reset_index(name='months')
result = result.merge(months_per_index, on='Index', how='inner')
result['final_value'] = result['units'] * result['last_price']
result['total_invested'] = result['months'] * 1.0
result['return_multiple'] = result['final_value'] / result['total_invested']

# Top 5 indices by return_multiple
top5 = result.sort_values('return_multiple', ascending=False).head(5)

# Map indices to countries manually
index_to_country = {
    'NYA': 'United States',
    'IXIC': 'United States',
    'GSPTSE': 'Canada',
    'GDAXI': 'Germany',
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Eurozone',
    'NSEI': 'India',
    'J203.JO': 'South Africa'
}

top5['Country'] = top5['Index'].map(index_to_country)

output = top5[['Index','Country','return_multiple']].to_dict(orient='records')

res_str = json.dumps(output)
print("__RESULT__:")
print(res_str)"""

env_args = {'var_call_MSOfsMK4HFOt6Zxxbc78eCup': [{'Index': 'J203.JO', 'first_date': '2012-02-08 00:00:00'}, {'Index': 'N225', 'first_date': '2000-01-04 00:00:00'}, {'Index': 'GSPTSE', 'first_date': '2000-01-05 00:00:00'}, {'Index': 'NSEI', 'first_date': '2007-09-25 00:00:00'}, {'Index': 'GDAXI', 'first_date': '2000-01-05 00:00:00'}, {'Index': 'HSI', 'first_date': '2000-01-14 00:00:00'}, {'Index': 'NYA', 'first_date': '2000-01-03 00:00:00'}, {'Index': '000001.SS', 'first_date': '2000-01-04 00:00:00'}, {'Index': 'SSMI', 'first_date': '2000-01-05 00:00:00'}, {'Index': 'TWII', 'first_date': '2000-01-17 00:00:00'}, {'Index': 'N100', 'first_date': '2000-01-10 00:00:00'}, {'Index': '399001.SZ', 'first_date': '2000-01-05 00:00:00'}, {'Index': 'IXIC', 'first_date': '2000-01-06 00:00:00'}], 'var_call_Cn08Wm4XExxUGOWwF0Qb54ni': 'file_storage/call_Cn08Wm4XExxUGOWwF0Qb54ni.json', 'var_call_MEkoX6aYzEcGFB46EEs4OKNw': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
