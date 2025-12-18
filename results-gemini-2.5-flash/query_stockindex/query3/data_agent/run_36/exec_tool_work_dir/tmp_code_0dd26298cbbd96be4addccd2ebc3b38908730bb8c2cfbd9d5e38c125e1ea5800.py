code = """import pandas as pd
import json

df = pd.read_json(locals()['var_function-call-12376398776406068395'])
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Get the first trading day of each month
df['year_month'] = df['Date'].dt.to_period('M')
monthly_first_prices = df.groupby(['Index', 'year_month'])['CloseUSD'].first().reset_index()

# Calculate monthly returns for regular monthly investments.
# Assume an investment of 1 unit at the beginning of each month.
# The total value at the end is the sum of (final_price / price_at_investment_month).

# Get the last closing price for each index
last_prices = df.groupby('Index')['CloseUSD'].last().reset_index()
last_prices.rename(columns={'CloseUSD': 'LastCloseUSD'}, inplace=True)

# Merge to calculate returns
monthly_first_prices = pd.merge(monthly_first_prices, last_prices, on='Index')
monthly_first_prices['MonthlyReturn'] = monthly_first_prices['LastCloseUSD'] / monthly_first_prices['CloseUSD']

# Sum up monthly returns for each index to get overall return
overall_returns = monthly_first_prices.groupby('Index')['MonthlyReturn'].sum().reset_index()
overall_returns.rename(columns={'MonthlyReturn': 'OverallReturn'}, inplace=True)

# Sort and get top 5
top_5_indices = overall_returns.sort_values(by='OverallReturn', ascending=False).head(5)

print('__RESULT__:')
print(top_5_indices.to_json(orient='records'))"""

env_args = {'var_function-call-12376398776406068395': 'file_storage/function-call-12376398776406068395.json'}

exec(code, env_args)
