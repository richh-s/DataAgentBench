code = """import json
import pandas as pd
from datetime import datetime

# Read the query result from the file
file_path = locals()['var_functions.query_db:2']
with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Get unique indices
unique_indices = df['Index'].unique().tolist()

# Calculate monthly returns for each index using dollar cost averaging
results = []

for idx in unique_indices:
    idx_data = df[df['Index'] == idx].copy()
    idx_data = idx_data.sort_values('Date')
    
    # Skip if we don't have data from near 2000
    if idx_data['Date'].min().year > 2000:
        continue
    
    # Calculate monthly investment returns (dollar cost averaging)
    # Assume $100 invested at the beginning of each month
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    monthly_prices = idx_data.groupby('YearMonth').first().reset_index()
    
    if len(monthly_prices) < 12:  # Need at least a year of data
        continue
    
    # Calculate returns with dollar cost averaging
    total_invested = 0
    total_shares = 0
    
    for _, row in monthly_prices.iterrows():
        total_invested += 100  # $100 per month
        total_shares += 100 / row['CloseUSD']
    
    # Final value
    final_price = monthly_prices['CloseUSD'].iloc[-1]
    final_value = total_shares * final_price
    total_return = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': idx,
        'TotalReturn': total_return,
        'Years': len(monthly_prices) / 12,
        'FinalValue': final_value,
        'TotalInvested': total_invested
    })

# Sort by total return
results_sorted = sorted(results, key=lambda x: x['TotalReturn'], reverse=True)
top_5 = results_sorted[:5]

print('__RESULT__:')
print(json.dumps({
    'top_5_indices': top_5,
    'total_indices_analyzed': len(results)
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
