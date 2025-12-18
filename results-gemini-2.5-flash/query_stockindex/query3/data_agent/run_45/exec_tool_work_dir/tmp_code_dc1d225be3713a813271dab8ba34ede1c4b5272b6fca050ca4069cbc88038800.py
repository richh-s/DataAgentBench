code = """import pandas as pd
import json

df_path = locals()['var_function-call-5945128186317195746']
with open(df_path, 'r') as f:
    df = pd.DataFrame(json.load(f))

df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Get the last trading day of each month for each index
monthly_close = df.groupby(['Index', pd.Grouper(key='Date', freq='M')])['CloseUSD'].last().reset_index()

returns = {}
for index in monthly_close['Index'].unique():
    index_data = monthly_close[monthly_close['Index'] == index].sort_values(by='Date')
    
    # Ensure there are at least two data points to calculate a return
    if len(index_data) < 2:
        continue

    # Assuming monthly investment of 1 unit
    initial_investment = 1
    total_value = initial_investment

    for i in range(1, len(index_data)):
        current_close = index_data.iloc[i]['CloseUSD']
        previous_close = index_data.iloc[i-1]['CloseUSD']
        
        # Calculate monthly return
        monthly_return = (current_close - previous_close) / previous_close
        
        # Apply the return to the total value, and add another 1 unit for the new monthly investment
        total_value = total_value * (1 + monthly_return) + 1 
    
    returns[index] = total_value - (len(index_data) * initial_investment) # total return considering initial investments

# Sort by returns and get the top 5
top_5_indices = sorted(returns.items(), key=lambda item: item[1], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top_5_indices))"""

env_args = {'var_function-call-5945128186317195746': 'file_storage/function-call-5945128186317195746.json'}

exec(code, env_args)
