code = """import pandas as pd

df = pd.read_json(locals()['var_function-call-1641922140904638122'])

df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])
df = df[df['Date'] >= '2000-01-01']

# Get the last trading day of each month for each index
monthly_prices = df.loc[df.groupby([df['Index'], df['Date'].dt.to_period('M')])['Date'].idxmax()]

# Sort by Index and Date
monthly_prices = monthly_prices.sort_values(by=['Index', 'Date'])

# Calculate monthly returns for regular monthly investments
# For simplicity, assuming investment happens on the first available date of each month
# and calculating the return based on the last available date of that month.

# Calculate the value of a single unit invested monthly
# The return will be the sum of (current_price / first_investment_price_in_month)

# Get the first closing price for each index to serve as the initial investment price if it's the first investment in the series.
first_prices = monthly_prices.groupby('Index').first().reset_index()
first_prices = first_prices[['Index', 'CloseUSD']].rename(columns={'CloseUSD': 'InitialInvestmentPrice'})

monthly_prices = monthly_prices.merge(first_prices, on='Index', how='left')

# Calculate the value of a 1 USD monthly investment
monthly_prices['InvestmentValue'] = monthly_prices['CloseUSD'] / monthly_prices.groupby('Index')['CloseUSD'].transform('first')

# Calculate cumulative return for each index
# This assumes a monthly investment of 1 unit of "value" (CloseUSD at the first month)
# and tracks the total value if these monthly investments were made.

# To correctly calculate overall returns for regular monthly investments,
# we need to track the cumulative value of these investments.
# For each index, for each month, we "invest" in that month's closing price.
# The total return is the sum of all monthly investments divided by the total invested capital.

# Let's re-think the calculation for "regular monthly investments".
# If an investor makes a fixed monetary investment (e.g., $1) each month, then the number of units bought each month is 1 / CloseUSD.
# The total number of units held would be the sum of (1 / CloseUSD) for all months.
# The final value would be (total units held) * (last CloseUSD).
# The return would be (final value - total invested capital) / total invested capital.

# For each index, get the monthly close prices starting from 2000-01-01
# We have monthly_prices dataframe already with the last day of each month's CloseUSD.

monthly_investments = monthly_prices.copy()

# Calculate number of units purchased with a hypothetical $1 investment each month
monthly_investments['UnitsBought'] = 1 / monthly_investments['CloseUSD']

# Group by index to calculate total units bought and the last closing price
overall_returns = monthly_investments.groupby('Index').agg(
    TotalUnitsBought=('UnitsBought', 'sum'),
    LastCloseUSD=('CloseUSD', 'last'),
    NumberOfMonths=('Date', 'count')
).reset_index()

# Calculate total invested capital (Number of months * $1)
overall_returns['TotalInvestedCapital'] = overall_returns['NumberOfMonths'] * 1

# Calculate final portfolio value
overall_returns['FinalPortfolioValue'] = overall_returns['TotalUnitsBought'] * overall_returns['LastCloseUSD']

# Calculate overall return
overall_returns['OverallReturn'] = (overall_returns['FinalPortfolioValue'] - overall_returns['TotalInvestedCapital']) / overall_returns['TotalInvestedCapital']

# Get top 5 indices
top_5_indices = overall_returns.sort_values(by='OverallReturn', ascending=False).head(5)

print('__RESULT__:')
print(top_5_indices[['Index', 'OverallReturn']].to_json(orient='records'))"""

env_args = {'var_function-call-1641922140904638122': 'file_storage/function-call-1641922140904638122.json'}

exec(code, env_args)
