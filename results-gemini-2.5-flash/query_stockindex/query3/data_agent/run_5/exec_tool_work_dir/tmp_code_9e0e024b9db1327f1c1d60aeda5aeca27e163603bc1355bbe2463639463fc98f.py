code = """import pandas as pd
import json

# Load the data from the file
with open(locals()['var_function-call-1712380820668893185'], 'r') as f:
    df = pd.DataFrame(json.load(f))

# Convert 'Date' to datetime objects
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter out invalid dates
df = df.dropna(subset=['Date'])

# Convert 'CloseUSD' to numeric, coercing errors will turn non-numeric into NaN
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter out rows with NaN 'CloseUSD' values
df = df.dropna(subset=['CloseUSD'])

# Get the last closing price of each month for each index
monthly_close = df.groupby(['Index', df['Date'].dt.to_period('M')])['CloseUSD'].last().reset_index()
monthly_close['Date'] = monthly_close['Date'].dt.start_time

# Sort by Index and Date
monthly_close = monthly_close.sort_values(by=['Index', 'Date'])

# Calculate monthly returns for regular monthly investments
# For regular monthly investments, we can simulate by taking the cumulative product of monthly price ratios

# Calculate the monthly returns (price ratio for investments)
monthly_close['Monthly_Return'] = monthly_close.groupby('Index')['CloseUSD'].pct_change() + 1

# Replace NaN in Monthly_Return with 1 for the first month of each index (no return yet)
monthly_close['Monthly_Return'] = monthly_close['Monthly_Return'].fillna(1)

# Calculate cumulative return for each index assuming monthly investment strategy:
# If an investor invests a fixed amount monthly, the total return would be the sum of returns of each monthly investment.
# A simpler approach to overall return for a "regular monthly investment" could be to consider the cumulative return
# of an initial investment plus subsequent investments compounding. However, the phrasing "highest overall returns"
# with "regular monthly investments" often implies comparing the total value accumulated. Let's simplify to the total
# gain based on the average monthly price. Or perhaps the total increase if we invested at the beginning of each month.

# Let's calculate total growth if 1 unit was invested each month.
# The final value would be the sum of (final_price / investment_month_price) for each monthly investment.

# Get the first closing price for each index in 2000 to use as a baseline for the first investment
first_prices = monthly_close.groupby('Index').head(1).rename(columns={'CloseUSD': 'FirstCloseUSD'})
monthly_close = pd.merge(monthly_close, first_prices[['Index', 'FirstCloseUSD']], on='Index', how='left')

# Calculate the total return for each index
# Assuming an investor invests 1 unit of money at the beginning of each month (represented by the first available close price for that month)
# And the value of that investment at the end of the period is the last available close price.

# To calculate the overall return from regular monthly investments, we sum the ratios of the latest price to each monthly investment price.
# This means for each month, we calculate (last_recorded_price / price_at_that_month_of_investment).
# Then sum these up and divide by the number of investments to get an average gain per unit invested.
# Or, even simpler, if we assume an equal investment each month, the total return is proportional to the sum of the last available price divided by the price at each investment point.

# Let's assume the simplest interpretation: if 1 unit of money was invested each month, what is the total gain? 
# This means we take the final price of the index and divide by the price at each investment point, then sum these up.

# Find the latest date for each index
latest_date_per_index = monthly_close.groupby('Index')['Date'].max().reset_index()
latest_date_per_index.columns = ['Index', 'LatestDate']

# Get the final closing price for each index on its latest date
final_prices_df = pd.merge(latest_date_per_index, monthly_close, left_on=['Index', 'LatestDate'], right_on=['Index', 'Date'], how='left')
final_prices_df = final_prices_df[['Index', 'CloseUSD']].rename(columns={'CloseUSD': 'FinalCloseUSD'})

# Merge final prices back to monthly_close to calculate individual investment returns
monthly_close_with_final = pd.merge(monthly_close, final_prices_df, on='Index', how='left')

# Calculate the return for each monthly investment (FinalCloseUSD / CloseUSD_at_investment_month)
monthly_close_with_final['Individual_Investment_Return'] = monthly_close_with_final['FinalCloseUSD'] / monthly_close_with_final['CloseUSD']

# Sum up the individual investment returns for each index to get total overall return (if investing 1 unit each month)
overall_returns = monthly_close_with_final.groupby('Index')['Individual_Investment_Return'].sum().reset_index()
overall_returns = overall_returns.sort_values(by='Individual_Investment_Return', ascending=False)

# Top 5 indices
top_5_indices = overall_returns.head(5)

print("__RESULT__:")
print(top_5_indices.to_json(orient='records'))"""

env_args = {'var_function-call-1712380820668893185': 'file_storage/function-call-1712380820668893185.json'}

exec(code, env_args)
