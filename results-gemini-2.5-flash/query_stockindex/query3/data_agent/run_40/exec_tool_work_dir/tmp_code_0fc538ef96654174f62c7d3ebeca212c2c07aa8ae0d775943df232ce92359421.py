code = """import pandas as pd
import json

df = pd.read_json(locals()['var_function-call-8311487335704339999'])
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Get the last closing price for each month for each index
monthly_closes = df.groupby([df['Index'], df['Date'].dt.to_period('M')])['CloseUSD'].last().reset_index()
monthly_closes['Date'] = monthly_closes['Date'].dt.start_time
monthly_closes = monthly_closes.sort_values(by=['Index', 'Date'])


all_returns = []

for index_symbol in monthly_closes['Index'].unique():
    index_data = monthly_closes[monthly_closes['Index'] == index_symbol].copy()
    
    if len(index_data) < 2:
        continue # Skip if less than 2 months of data

    # Calculate monthly growth factor
    index_data['PrevCloseUSD'] = index_data['CloseUSD'].shift(1)
    index_data['GrowthFactor'] = index_data['CloseUSD'] / index_data['PrevCloseUSD']
    
    # Simulate monthly investments
    # Assuming an investment of 1 unit at the beginning of each month (from the second month onwards)
    # The first investment is made at the start of the first month with data
    # And subsequent investments are added to the previous month's value after it has grown
    
    portfolio_value = 0.0
    # We start investing from the first month available for an index
    # The first month's close price is considered as the base for the first investment's return
    # Subsequent investments are added at the start of the next month and grow from there
    
    # Initialize portfolio_value with the first month's closing price (representing the first investment's growth)
    # and also consider the initial investment amount
    
    # Let's refine the simulation: Assume $1 invested *at the end* of each month, buying shares at that month's closing price.
    # Or, assume $1 invested at the *start* of each month, buying at the *previous* month's closing price, and growing over the month.
    # The prompt says "regular monthly investments... since 2000". This usually means a fixed amount invested at a specific point each month.
    # Let's assume we invest $1 at the end of each month, based on the `last()` closing price of that month. 
    # The return is calculated from the accumulation of these investments.

    # For the first month, we invest $1, and its value is 1 * (final_month_close / first_month_close)
    # For the second month, we invest $1, its value is 1 * (final_month_close / second_month_close)
    # And so on. Total return is sum of all these normalized values.

    first_close = index_data['CloseUSD'].iloc[0]
    last_close = index_data['CloseUSD'].iloc[-1]
    
    if first_close == 0: # Avoid division by zero
        overall_return = 0
    else:
        # Total value of all $1 investments made at the start of each month, 
        # growing till the end of the investment period
        # Each dollar invested at time t_i grows by (last_close / close_at_t_i)
        total_value = (index_data['CloseUSD'].iloc[-1] / index_data['CloseUSD']).sum()

        # Number of investments made
        num_investments = len(index_data)
        
        # Overall return percentage: (total_value - num_investments) / num_investments * 100
        # This calculates the profit divided by total capital invested.
        if num_investments > 0:
            overall_return = ((total_value - num_investments) / num_investments) * 100
        else:
            overall_return = 0

    all_returns.append({'Index': index_symbol, 'OverallReturn': overall_return})

returns_df = pd.DataFrame(all_returns)

# Sort by OverallReturn and get the top 5
top_5_indices = returns_df.sort_values(by='OverallReturn', ascending=False).head(5)

print('__RESULT__:')
print(top_5_indices.to_json(orient='records'))"""

env_args = {'var_function-call-8311487335704339999': 'file_storage/function-call-8311487335704339999.json'}

exec(code, env_args)
