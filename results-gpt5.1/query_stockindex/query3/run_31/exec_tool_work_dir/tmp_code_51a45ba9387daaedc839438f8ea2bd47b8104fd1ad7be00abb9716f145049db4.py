code = """import pandas as pd, json, os

# Load the large index trade result from file
path = var_call_4cZg7WX9YqVoOW1PprPNHOJf
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure proper dtypes
df['Date'] = pd.to_datetime(df['Date'])
df['Adj Close'] = df['Adj Close'].astype(float)

# We simulate regular monthly investments: invest 1 unit of cash on the first trading day of each month per index.
# For each index & month, compute units bought = 1 / adj_close_on_first_trading_day.

df['YearMonth'] = df['Date'].dt.to_period('M')

# First trading day per index per month
first_days = df.sort_values('Date').groupby(['Index','YearMonth']).first().reset_index()
first_days['units'] = 1.0 / first_days['Adj Close']

# Total units accumulated per index since 2000
units_per_index = first_days.groupby('Index')['units'].sum().reset_index()

# Get last available Adj Close per index to value the portfolio
last_prices = df.sort_values('Date').groupby('Index').tail(1)[['Index','Adj Close']].rename(columns={'Adj Close':'last_price'})

summary = units_per_index.merge(last_prices, on='Index')

# Total invested per index = number of months with an investment (i.e., rows in first_days per index)
months_invested = first_days.groupby('Index').size().reset_index(name='months')
summary = summary.merge(months_invested, on='Index')
summary['total_invested'] = summary['months'] * 1.0
summary['final_value'] = summary['units'] * summary['last_price']
summary['return_multiple'] = summary['final_value'] / summary['total_invested']

# Top 5 indices by return_multiple
top5 = summary.sort_values('return_multiple', ascending=False).head(5)

result = top5[['Index','return_multiple']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_4cZg7WX9YqVoOW1PprPNHOJf': 'file_storage/call_4cZg7WX9YqVoOW1PprPNHOJf.json'}

exec(code, env_args)
