code = """import pandas as pd

# Read the full result from the JSON file
df = pd.read_json(locals()['var_function-call-5404062162637134718'])

# Convert 'Date' to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# Sort by Index and Date to ensure correct processing
df = df.sort_values(by=['Index', 'Date'])

# Get the first trading day of each month for each index
df['YearMonth'] = df['Date'].dt.to_period('M')
monthly_prices = df.groupby(['Index', 'YearMonth']).first().reset_index()

# Calculate returns for each index assuming monthly investments
# For each index, we assume an investment of 1 unit at the start of each month.
# The return is the sum of the value of each monthly investment at the end of the period.

returns = {}
for index_symbol in monthly_prices['Index'].unique():
    index_data = monthly_prices[monthly_prices['Index'] == index_symbol].copy()
    
    # Convert 'Adj Close' to numeric, coercing errors to NaN
    index_data.loc[:, 'Adj Close'] = pd.to_numeric(index_data['Adj Close'], errors='coerce')
    
    # Drop rows where 'Adj Close' is NaN after conversion
    index_data.dropna(subset=['Adj Close'], inplace=True)
    
    if len(index_data) < 2:  # Need at least two data points to calculate a return
        returns[index_symbol] = 0.0
        continue

    # The last available 'Adj Close' is the final price for calculating return
    final_price = index_data['Adj Close'].iloc[-1]
    
    total_invested_value = 0.0
    # Sum of (final_price / price_at_investment) for each monthly investment
    for _, row in index_data.iterrows():
        price_at_investment = row['Adj Close']
        if price_at_investment > 0:
            total_invested_value += (final_price / price_at_investment) -1 # Calculate the return for each monthly investment
    
    returns[index_symbol] = total_invested_value

# Sort by return in descending order and get the top 5
sorted_returns = sorted(returns.items(), key=lambda item: item[1], reverse=True)
top_5_indices = sorted_returns[:5]

# Extract just the index symbols
top_5_index_symbols = [item[0] for item in top_5_indices]

print('__RESULT__:')
print(pd.DataFrame(top_5_indices, columns=['Index', 'Return']).to_json(orient='records'))"""

env_args = {'var_function-call-5404062162637134718': 'file_storage/function-call-5404062162637134718.json'}

exec(code, env_args)
