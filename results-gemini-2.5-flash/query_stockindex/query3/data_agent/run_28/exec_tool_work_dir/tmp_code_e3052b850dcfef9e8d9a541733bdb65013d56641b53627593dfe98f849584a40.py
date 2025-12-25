code = """import pandas as pd
import json

# Load the full result from the file
with open(locals()['var_function-call-7326152765868364010'], 'r') as f:
    trade_data = json.load(f)

df = pd.DataFrame(trade_data)
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Get the last trading day of each month for each index
monthly_data = df.loc[df.groupby([df['Index'], df['Date'].dt.year, df['Date'].dt.month])['Date'].idxmax()]

# Calculate total return for each index
returns = {}
for index_symbol in monthly_data['Index'].unique():
    index_df = monthly_data[monthly_data['Index'] == index_symbol].sort_values(by='Date')
    
    if len(index_df) < 2:
        continue

    total_invested = 0
    total_value = 0
    
    for i in range(len(index_df)):
        # Assume a $1 investment at the end of each month
        investment_amount = 1
        total_invested += investment_amount
        
        # Calculate the value of this $1 investment at the end of the period
        if i < len(index_df) -1:
            final_price = index_df.iloc[-1]['CloseUSD']
            initial_price = index_df.iloc[i]['CloseUSD']
            total_value += (final_price / initial_price) * investment_amount
        else:
            total_value += investment_amount # The last investment is worth its face value

    returns[index_symbol] = (total_value - total_invested) / total_invested * 100

# Sort by return and get the top 5
top_5_indices = sorted(returns.items(), key=lambda item: item[1], reverse=True)[:5]

print("__RESULT__:")
print(json.dumps(top_5_indices))"""

env_args = {'var_function-call-7326152765868364010': 'file_storage/function-call-7326152765868364010.json'}

exec(code, env_args)
