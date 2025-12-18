code = """import pandas as pd
import json

df = pd.read_json(locals()['var_function-call-16206780393545946943'])
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Filter data from 2000 onwards
df = df[df['Date'].dt.year >= 2000]

# Get the last day of each month for each index
monthly_last_day = df.groupby(['Index', df['Date'].dt.to_period('M')])['Date'].transform('max')
monthly_data = df[df['Date'] == monthly_last_day]

# Sort by Index and Date to ensure correct order for calculations
monthly_data = monthly_data.sort_values(by=['Index', 'Date'])

# Calculate the return for each index
# Assuming regular monthly investments mean that at the end of each month, we check the value.
# The overall return will be the ratio of the final value to the initial investment (sum of monthly closing prices).
# Since it's 'regular monthly investments', we can assume an equal amount invested each month.
# To simplify, we can assume investing $1 at the end of each month.
# So, for each month, the return on that $1 investment would be (current_close_price / close_price_at_investment_month).
# A more straightforward approach for "overall returns" from "regular monthly investments"
# is to calculate the total value if $1 was invested each month.
# For each index, we will sum up the (final_close_price / monthly_close_price) for each month.
# This represents the total value of all monthly $1 investments if held until the end.

returns = {}
for index_name in monthly_data['Index'].unique():
    index_df = monthly_data[monthly_data['Index'] == index_name]
    
    if len(index_df) > 1:
        # Get the closing price of the last month in the series
        final_close = index_df.iloc[-1]['CloseUSD']
        
        # Calculate the sum of (final_close / monthly_close) for all months
        # This simulates investing $1 each month and seeing its growth relative to the final price.
        # This is a common way to measure overall return from regular investments.
        total_return_multiplier = (final_close / index_df['CloseUSD']).sum()
        returns[index_name] = total_return_multiplier

# Sort indices by their calculated overall returns
sorted_returns = sorted(returns.items(), key=lambda item: item[1], reverse=True)

# Get the top 5 indices
top_5_indices = [item[0] for item in sorted_returns[:5]]

print('__RESULT__:')
print(json.dumps(top_5_indices))"""

env_args = {'var_function-call-16206780393545946943': 'file_storage/function-call-16206780393545946943.json'}

exec(code, env_args)
