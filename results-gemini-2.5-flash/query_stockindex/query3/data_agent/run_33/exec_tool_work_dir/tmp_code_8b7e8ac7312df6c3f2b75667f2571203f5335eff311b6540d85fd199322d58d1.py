code = """import pandas as pd
import json

with open(locals()['var_function-call-14422826081707029859'], 'r') as f:
    trade_data = json.load(f)

df = pd.DataFrame(trade_data)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)
df = df.dropna(subset=['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Sort by Index and Date to ensure correct order for monthly selections
df = df.sort_values(by=['Index', 'Date'])

# Get the first available price for each month for each index
df['YearMonth'] = df['Date'].dt.to_period('M')
monthly_prices = df.groupby(['Index', 'YearMonth']).first().reset_index()

# Calculate overall returns for regular monthly investments
returns = {}
for index_name in monthly_prices['Index'].unique():
    index_df = monthly_prices[monthly_prices['Index'] == index_name].copy()
    
    if not index_df.empty:
        final_price = index_df['CloseUSD'].iloc[-1]
        
        total_value = (1 / index_df['CloseUSD']).sum() * final_price
        
        total_investment_months = len(index_df)
        
        overall_return = (total_value - total_investment_months) / total_investment_months * 100
        returns[index_name] = overall_return

# Sort returns in descending order and get the top 5
sorted_returns = sorted(returns.items(), key=lambda item: item[1], reverse=True)
top_5_indices = sorted_returns[:5]

# Convert to a list of dictionaries for JSON output
result = [{'Index': item[0], 'OverallReturn': item[1]} for item in top_5_indices]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14422826081707029859': 'file_storage/function-call-14422826081707029859.json'}

exec(code, env_args)
