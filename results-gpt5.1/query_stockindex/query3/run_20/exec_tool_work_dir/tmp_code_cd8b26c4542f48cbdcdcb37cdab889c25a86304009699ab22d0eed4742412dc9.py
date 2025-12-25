code = """import pandas as pd, json

# Reload simpler
path = var_call_hD7RktzgrxIZz5NI1ZhOvfBU
import os
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates with dayfirst to handle '01 Apr 2016, 00:00' style if present, but here they look ISO
try:
    df['Date'] = pd.to_datetime(df['Date'])
except Exception:
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

df['Adj Close'] = pd.to_numeric(df['Adj Close'], errors='coerce')

start = pd.Timestamp('2000-01-01')
df = df[df['Date'] >= start]

# Drop rows with missing prices
df = df.dropna(subset=['Adj Close'])

df['YearMonth'] = df['Date'].dt.to_period('M')
monthly = df.sort_values(['Index','Date']).groupby(['Index','YearMonth']).tail(1)

monthly['units'] = 1.0 / monthly['Adj Close']
units_per_index = monthly.groupby('Index')['units'].sum().reset_index()

last_prices = df.sort_values(['Index','Date']).groupby('Index').tail(1)[['Index','Adj Close']].rename(columns={'Adj Close':'final_price'})

summary = units_per_index.merge(last_prices, on='Index')
months_invested = monthly.groupby('Index')['YearMonth'].nunique().reset_index().rename(columns={'YearMonth':'months'})
summary = summary.merge(months_invested, on='Index')
summary['final_value'] = summary['units'] * summary['final_price']
summary['total_invested'] = summary['months'] * 1.0
summary['return_multiple'] = summary['final_value'] / summary['total_invested']

first_dates = pd.DataFrame(var_call_kO3vJhEX2gqzdcRhPEt8vWf9)
first_dates['first_date'] = pd.to_datetime(first_dates['first_date'], dayfirst=True, errors='coerce')
eligible = first_dates[first_dates['first_date'] <= pd.Timestamp('2000-01-31')]['Index']
summary = summary[summary['Index'].isin(eligible)]

top5 = summary.sort_values('return_multiple', ascending=False).head(5)[['Index','return_multiple']]

print("__RESULT__:")
print(json.dumps(top5.to_dict(orient='records')))"""

env_args = {'var_call_kO3vJhEX2gqzdcRhPEt8vWf9': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}], 'var_call_hD7RktzgrxIZz5NI1ZhOvfBU': 'file_storage/call_hD7RktzgrxIZz5NI1ZhOvfBU.json', 'var_call_wItJgQBq7zudaa4P2aR0l0Q0': ['index_info']}

exec(code, env_args)
