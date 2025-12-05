code = """import pandas as pd, json, os
from datetime import datetime

path = var_call_eKhqQ0LsM84AIfRIRFglNxdX
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# coerce errors in dates
df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.to_period('M').dt.to_timestamp()
df = df.dropna(subset=['Date'])

df['Adj Close'] = pd.to_numeric(df['Adj Close'], errors='coerce')
df = df.dropna(subset=['Adj Close'])

monthly = df.sort_values(['Index','Date']).drop_duplicates(['Index','Date'], keep='last')
monthly['units'] = 1.0 / monthly['Adj Close']
monthly['value'] = monthly['units'] * monthly['Adj Close']

final_values = monthly.groupby('Index')['value'].sum().reset_index()

top5 = final_values.sort_values('value', ascending=False).head(5)

mapping = {
    'N225': ('Tokyo Stock Exchange','Japan'),
    'HSI': ('Hong Kong Stock Exchange','Hong Kong'),
    '000001.SS': ('Shanghai Stock Exchange','China'),
    '399001.SZ': ('Shenzhen Stock Exchange','China'),
    '^GSPC': ('New York Stock Exchange','United States'),
    '^IXIC': ('NASDAQ','United States'),
    '^GDAXI': ('Frankfurt Stock Exchange','Germany'),
    '^FCHI': ('Euronext','France'),
    '^FTSE': ('London Stock Exchange','United Kingdom'),
    '^BSESN': ('National Stock Exchange of India','India'),
    '^KS11': ('Korea Exchange','South Korea'),
    '^SSMI': ('SIX Swiss Exchange','Switzerland'),
    '^GSPTSE': ('Toronto Stock Exchange','Canada'),
    '^J203.JO': ('Johannesburg Stock Exchange','South Africa')
}

result = []
for _, row in top5.iterrows():
    idx = row['Index']
    exch, country = mapping.get(idx, ('Unknown','Unknown'))
    result.append({'Index': idx, 'Exchange': exch, 'Country': country})

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_eKhqQ0LsM84AIfRIRFglNxdX': 'file_storage/call_eKhqQ0LsM84AIfRIRFglNxdX.json', 'var_call_kyJ1YNwshERxlTN7bfKV6xXP': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
