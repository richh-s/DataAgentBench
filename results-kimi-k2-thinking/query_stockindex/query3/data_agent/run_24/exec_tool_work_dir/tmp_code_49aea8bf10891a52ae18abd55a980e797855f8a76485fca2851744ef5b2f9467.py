code = """import json
import pandas as pd

# Load the trade data from the storage result
trade_result = locals()['var_functions.query_db:8']

# If it's a file path, read it; otherwise it's the data directly
if isinstance(trade_result, str) and '.json' in trade_result:
    with open(trade_result, 'r') as f:
        trade_data = json.load(f)
else:
    trade_data = trade_result

# Create DataFrame
df = pd.DataFrame(trade_data)

# Convert data types
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Define index to country mapping
index_mapping = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'GDAXI': 'Germany',
    'IXIC': 'USA',
    'NYA': 'USA',
    'N100': 'Netherlands',
    'NSEI': 'India',
    'TWII': 'Taiwan',
    'GSPTSE': 'Canada',
    'J203.JO': 'South Africa',
    'SSMI': 'Switzerland'
}

# Add country info and filter for data from 2000 onwards
df['Country'] = df['Index'].map(index_mapping)
df_2000 = df[df['Date'] >= '2000-01-01'].copy()

# For each index, calculate returns from regular monthly investments
results = []

for index in df_2000['Index'].unique():
    index_data = df_2000[df_2000['Index'] == index].copy()
    index_data = index_data.sort_values('Date')
    
    if len(index_data) < 100:  # Need sufficient data
        continue
    
    # Get monthly closing prices (last trading day of each month)
    index_data['YearMonth'] = index_data['Date'].dt.to_period('M')
    monthly_data = index_data.groupby('YearMonth').agg({
        'CloseUSD': 'last'
    }).reset_index()
    
    monthly_data = monthly_data.sort_values('YearMonth')
    
    # Calculate dollar cost averaging returns assuming $100 invested monthly
    total_invested = 0
    total_shares = 0
    monthly_investment = 100
    
    for i, row in monthly_data.iterrows():
        price = row['CloseUSD']
        if price > 0:
            shares = monthly_investment / price
            total_shares += shares
            total_invested += monthly_investment
    
    # Final value calculation
    final_price = monthly_data['CloseUSD'].iloc[-1]
    final_value = total_shares * final_price
    
    # Calculate ROI
    roi_percent = ((final_value - total_invested) / total_invested * 100) if total_invested > 0 else 0
    
    results.append({
        'Index': index,
        'Country': index_mapping.get(index, 'Unknown'),
        'Months': len(monthly_data),
        'Total_Invested': total_invested,
        'Final_Value': round(final_value, 2),
        'ROI_Percent': round(roi_percent, 2)
    })

# Sort by ROI and get top 5
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('ROI_Percent', ascending=False)
top_5_indices = results_df.head(5)

print('__RESULT__:')
print(top_5_indices.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
