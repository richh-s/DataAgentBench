code = """import pandas as pd
import json

# Load the trade data
with open(locals()['var_function-call-12624981542445449335'], 'r') as f:
    trade_data = json.load(f)

df = pd.DataFrame(trade_data)

# Convert 'Date' to datetime and 'CloseUSD' to numeric
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Get the last CloseUSD for each index (this represents the end of the investment period for each index)
last_close_prices = df.groupby('Index').apply(lambda x: x.sort_values(by='Date').iloc[-1]['CloseUSD']).rename('LastCloseUSD')

# Get the first CloseUSD for each month for each index
df['YearMonth'] = df['Date'].dt.to_period('M')
monthly_first_close = df.groupby(['Index', 'YearMonth'])['CloseUSD'].first().rename('FirstMonthlyCloseUSD').reset_index()

# Calculate the return for each monthly investment
# Join with last_close_prices to get the final value for each index
monthly_returns_calc = pd.merge(monthly_first_close, last_close_prices, on='Index')
monthly_returns_calc['InvestmentValueAtEnd'] = (monthly_returns_calc['LastCloseUSD'] / monthly_returns_calc['FirstMonthlyCloseUSD'])

# Calculate overall return for each index
# Sum up InvestmentValueAtEnd for each index and divide by the number of months (total investments)
overall_returns = monthly_returns_calc.groupby('Index').apply(lambda x: (x['InvestmentValueAtEnd'].sum() / len(x)) - 1).rename('OverallReturn')

# Sort and get the top 5 indices
top_5_indices = overall_returns.nlargest(5).reset_index()

print("__RESULT__:")
print(top_5_indices.to_json(orient='records'))"""

env_args = {'var_function-call-12624981542445449335': 'file_storage/function-call-12624981542445449335.json'}

exec(code, env_args)
