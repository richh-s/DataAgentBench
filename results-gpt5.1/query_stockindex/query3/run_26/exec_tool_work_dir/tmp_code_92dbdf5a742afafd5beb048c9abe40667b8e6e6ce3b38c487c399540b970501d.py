code = """import pandas as pd, json, os

path = var_call_qovv62omWj6Nw35unWwo4kzD
if isinstance(path, str) and os.path.isfile(path):
    data = json.load(open(path))
else:
    data = var_call_qovv62omWj6Nw35unWwo4kzD

df = pd.DataFrame(data)

# handle date parsing robustly
df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.to_period('M')

df['Adj Close'] = pd.to_numeric(df['Adj Close'], errors='coerce')

df = df.dropna(subset=['Date','Adj Close'])

monthly = df.sort_values(['Index','Date']).groupby(['Index','Date']).tail(1)

monthly['units'] = 1.0 / monthly['Adj Close']

agg = monthly.groupby('Index').agg(total_units=('units','sum'), last_price=('Adj Close','last'))
agg['final_value'] = agg['total_units'] * agg['last_price']

result = agg['final_value'].sort_values(ascending=False).head(5).reset_index()

index_to_country = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    '^GSPC': 'United States',
    '^DJI': 'United States',
    '^IXIC': 'United States',
    '^GDAXI': 'Germany',
    '^FCHI': 'France',
    '^FTSE': 'United Kingdom',
    '^BSESN': 'India',
    '^NSEI': 'India',
    '^KS11': 'South Korea',
    '^SSMI': 'Switzerland',
    '^TWII': 'Taiwan',
    '^J203.JO': 'South Africa',
    '^GSPTSE': 'Canada'
}

result['Country'] = result['Index'].map(index_to_country).fillna('Unknown')

out = result.to_dict(orient='records')
js = json.dumps(out)
print('__RESULT__:')
print(js)"""

env_args = {'var_call_qovv62omWj6Nw35unWwo4kzD': 'file_storage/call_qovv62omWj6Nw35unWwo4kzD.json', 'var_call_HYMxOQmqTXzL8ROxc5iF751j': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
