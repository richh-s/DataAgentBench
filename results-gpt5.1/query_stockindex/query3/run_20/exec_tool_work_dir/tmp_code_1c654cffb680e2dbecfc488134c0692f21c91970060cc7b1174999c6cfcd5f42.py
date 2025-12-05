code = """import pandas as pd, json, os

# Load full daily prices from file
path = var_call_hD7RktzgrxIZz5NI1ZhOvfBU
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure types
df['Date'] = pd.to_datetime(df['Date'])
df['Adj Close'] = pd.to_numeric(df['Adj Close'])

# Keep data from 2000-01-01 onward
start = pd.Timestamp('2000-01-01')
mask = df['Date'] >= start
df = df[mask]

# Resample to monthly using last available Adj Close in each month
df['YearMonth'] = df['Date'].dt.to_period('M')
monthly = df.sort_values(['Index','Date']).groupby(['Index','YearMonth']).tail(1)

# Assume $1 invested at end of each month from first available month >=2000 for that index
# Number of units bought each month = 1 / price
monthly['units'] = 1.0 / monthly['Adj Close']

# Total units accumulated per index
units_per_index = monthly.groupby('Index')['units'].sum().reset_index()

# Need final price per index (last available date overall)
last_prices = df.sort_values(['Index','Date']).groupby('Index').tail(1)[['Index','Adj Close']].rename(columns={'Adj Close':'final_price'})

summary = units_per_index.merge(last_prices, on='Index')
summary['final_value'] = summary['units'] * summary['final_price']
# Total invested dollars = number of months (since $1 each month)
months_invested = monthly.groupby('Index')['YearMonth'].nunique().reset_index().rename(columns={'YearMonth':'months'})
summary = summary.merge(months_invested, on='Index')
summary['total_invested'] = summary['months'] * 1.0
summary['return_multiple'] = summary['final_value'] / summary['total_invested']

# Filter indices that actually have data starting in or before 2000 per earlier query
first_dates = pd.DataFrame(var_call_kO3vJhEX2gqzdcRhPEt8vWf9)
first_dates['first_date'] = pd.to_datetime(first_dates['first_date'])
eligible = first_dates[first_dates['first_date'] <= pd.Timestamp('2000-01-31')]['Index']
summary = summary[summary['Index'].isin(eligible)]

# Top 5 indices by return_multiple
top5 = summary.sort_values('return_multiple', ascending=False).head(5)[['Index','return_multiple']]

result = top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_kO3vJhEX2gqzdcRhPEt8vWf9': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}], 'var_call_hD7RktzgrxIZz5NI1ZhOvfBU': 'file_storage/call_hD7RktzgrxIZz5NI1ZhOvfBU.json', 'var_call_wItJgQBq7zudaa4P2aR0l0Q0': ['index_info']}

exec(code, env_args)
