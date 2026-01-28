code = """import json
import pandas as pd

# Load trade data
file_info = locals()['var_functions.query_db:8']
if isinstance(file_info, str):
    with open(file_info, 'r') as f:
        trade_data = json.load(f)
else:
    trade_data = file_info

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Clean and convert data
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])
df['Date_str'] = df['Date']

# Extract year-month from date string for monthly grouping
df['YearMonth'] = df['Date_str'].str[:7]

# Map indices to countries
index_country = {
    'N225': 'Japan', 'HSI': 'Hong Kong', '000001.SS': 'China', 
    '399001.SZ': 'China', 'GDAXI': 'Germany', 'IXIC': 'USA', 
    'NYA': 'USA', 'N100': 'Netherlands', 'NSEI': 'India', 
    'TWII': 'Taiwan', 'GSPTSE': 'Canada', 'J203.JO': 'South Africa', 'SSMI': 'Switzerland'
}

df['Country'] = df['Index'].map(index_country)

# Filter for data from 2000 onwards
df_2000 = df[df['Date_str'] >= '2000-01-01'].copy()

# Calculate monthly investment returns
results = []

for idx in df_2000['Index'].unique():
    idx_data = df_2000[df_2000['Index'] == idx].copy()
    
    # Get monthly closing prices (last trading day of each month)
    monthly = idx_data.groupby('YearMonth').agg({
        'CloseUSD': 'last'
    }).reset_index()
    monthly = monthly.sort_values('YearMonth')
    
    # Skip if insufficient data
    if len(monthly) < 24:  # Need at least 2 years
        continue
    
    # Calculate dollar cost averaging returns: $100 monthly investment
    total_invested = 0
    total_shares = 0
    monthly_amount = 100
    
    for _, row in monthly.iterrows():
        price = row['CloseUSD']
        if price > 0:
            total_shares += monthly_amount / price
            total_invested += monthly_amount
    
    if total_invested == 0:
        continue
    
    final_price = monthly['CloseUSD'].iloc[-1]
    final_value = total_shares * final_price
    roi = ((final_value - total_invested) / total_invested) * 100
    
    results.append({
        'Index': idx,
        'Country': index_country.get(idx, 'Unknown'),
        'Months_of_Data': len(monthly),
        'Total_Invested': round(total_invested, 2),
        'Final_Value': round(final_value, 2),
        'ROI_Percent': round(roi, 2)
    })

# Sort by ROI and get top 5
top5 = pd.DataFrame(results).sort_values('ROI_Percent', ascending=False).head(5)

print('__RESULT__:')
print(top5.to_json(orient='records', indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
