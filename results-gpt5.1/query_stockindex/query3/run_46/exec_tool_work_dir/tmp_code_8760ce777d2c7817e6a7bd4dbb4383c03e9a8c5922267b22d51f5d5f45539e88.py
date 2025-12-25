code = """import pandas as pd, json, os

path = var_call_kPM8xWZRBlknO5G3x9PzeZs9
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# parse date more robustly
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

# ensure Adj Close is float
df['Adj Close'] = df['Adj Close'].astype(float)

# assume monthly investment on first trading day each month per index
df = df.sort_values(['Index','Date'])
first_monthly = df.groupby(['Index', df['Date'].dt.to_period('M')]).head(1).copy()

first_monthly['units'] = 1.0 / first_monthly['Adj Close']

cum_units = first_monthly.groupby('Index').agg(
    total_units=('units','sum'),
    start_date=('Date','min'),
    end_date=('Date','max')
).reset_index()

last_price = df.sort_values(['Index','Date']).groupby('Index').tail(1)[['Index','Adj Close']].copy()

res = cum_units.merge(last_price, on='Index')

months = first_monthly.groupby('Index').size().reset_index(name='n_months')
res = res.merge(months, on='Index')
res['contribution'] = res['n_months'] * 1.0
res['final_value'] = res['total_units'] * res['Adj Close']
res['return_multiple'] = res['final_value'] / res['contribution']

top5 = res.sort_values('return_multiple', ascending=False).head(5)[['Index','return_multiple']]

print('__RESULT__:')
print(json.dumps(top5.to_dict(orient='records')))"""

env_args = {'var_call_kPM8xWZRBlknO5G3x9PzeZs9': 'file_storage/call_kPM8xWZRBlknO5G3x9PzeZs9.json', 'var_call_GgXUvBZrMoBR1VMpYx451GC0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
