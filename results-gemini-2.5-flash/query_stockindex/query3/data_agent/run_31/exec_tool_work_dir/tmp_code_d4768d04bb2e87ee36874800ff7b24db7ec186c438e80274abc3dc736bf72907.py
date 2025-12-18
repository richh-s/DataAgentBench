code = """import pandas as pd
import json

# Load the full data from the file
with open(locals()['var_function-call-7051207664903736255'], 'r') as f:
    df_trade = pd.DataFrame(json.load(f))

# Convert 'Date' to datetime and 'CloseUSD' to numeric
df_trade['Date'] = pd.to_datetime(df_trade['Date'])
df_trade['CloseUSD'] = pd.to_numeric(df_trade['CloseUSD'])

# Filter data from 2000-01-01 onwards
df_trade = df_trade[df_trade['Date'] >= '2000-01-01']

# Get the last trading day of each month for each index
monthly_closes = df_trade.loc[df_trade.groupby([df_trade['Index'], df_trade['Date'].dt.to_period('M')])['Date'].idxmax()]

# Calculate overall returns for regular monthly investments
# Assume an investment of $100 each month
monthly_investment_amount = 100

returns = {}
for index_symbol in monthly_closes['Index'].unique():
    index_data = monthly_closes[monthly_closes['Index'] == index_symbol].sort_values('Date')

    if len(index_data) < 2:  # Need at least two months to calculate return
        continue

    total_shares = 0
    total_invested_capital = 0
    
    # Calculate shares bought each month
    for _, row in index_data.iterrows():
        shares_bought = monthly_investment_amount / row['CloseUSD']
        total_shares += shares_bought
        total_invested_capital += monthly_investment_amount

    # Final portfolio value (using the last available closing price)
    final_close_price = index_data['CloseUSD'].iloc[-1]
    final_portfolio_value = total_shares * final_close_price
    
    # Overall return calculation
    if total_invested_capital > 0:
        overall_return = (final_portfolio_value - total_invested_capital) / total_invested_capital
        returns[index_symbol] = overall_return

# Sort by returns in descending order and get the top 5
sorted_returns = sorted(returns.items(), key=lambda item: item[1], reverse=True)
top_5_indices = sorted_returns[:5]

print("__RESULT__:")
print(json.dumps(top_5_indices))"""

env_args = {'var_function-call-7051207664903736255': 'file_storage/function-call-7051207664903736255.json'}

exec(code, env_args)
