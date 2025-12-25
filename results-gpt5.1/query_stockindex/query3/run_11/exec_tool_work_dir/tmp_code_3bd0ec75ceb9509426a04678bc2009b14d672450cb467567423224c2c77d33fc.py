code = """import pandas as pd, json
import os

path = var_call_KmUB4PMVss1gFLBDfJGMxp75
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# convert Date and Adj Close
df['Date'] = pd.to_datetime(df['Date'])
df['Adj Close'] = pd.to_numeric(df['Adj Close'])

# monthly regular investment on first trading day of each month
df['YearMonth'] = df['Date'].dt.to_period('M')
first_days = df.sort_values('Date').groupby(['Index','YearMonth']).first().reset_index()

# assume invest 1 unit of currency each month, buy units = 1 / price
first_days['units'] = 1.0 / first_days['Adj Close']

agg = first_days.groupby('Index').agg(
    total_units=('units','sum'),
    total_invested=('units', 'size')  # since 1 per month
).reset_index()

# need final price per index (last available Adj Close)
last_prices = df.sort_values('Date').groupby('Index').tail(1)[['Index','Adj Close']].rename(columns={'Adj Close':'final_price'})

agg = agg.merge(last_prices, on='Index', how='left')
agg['final_value'] = agg['total_units'] * agg['final_price']
agg['return_multiple'] = agg['final_value'] / agg['total_invested']

agg_sorted = agg.sort_values('return_multiple', ascending=False).head(5)

result = agg_sorted[['Index','return_multiple']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_KmUB4PMVss1gFLBDfJGMxp75': 'file_storage/call_KmUB4PMVss1gFLBDfJGMxp75.json', 'var_call_DuiGncb2ss0g8YQgE9IqFwFL': ['index_info']}

exec(code, env_args)
