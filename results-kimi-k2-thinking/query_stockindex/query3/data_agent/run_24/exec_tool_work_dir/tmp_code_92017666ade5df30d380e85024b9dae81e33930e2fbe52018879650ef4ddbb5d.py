code = """import json
import pandas as pd
from datetime import datetime

# Get trade data
trade_result = locals()['var_functions.query_db:8']
if isinstance(trade_result, str):
    with open(trade_result, 'r') as f:
        trade_data = json.load(f)
else:
    trade_data = trade_result

df = pd.DataFrame(trade_data)

# Convert Date using string parsing
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])
df['Year'] = df['Date'].str[:4]
df['Month'] = df['Date'].str[5:7]
df['Day'] = df['Date'].str[8:10]

# Convert to actual datetime
df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])

# Map indices to countries
index_country = {
    'N225': 'Japan', 'HSI': 'Hong Kong', '000001.SS': 'China', 
    '399001.SZ': 'China', 'GDAXI': 'Germany', 'IXIC': 'USA', 
    'NYA': 'USA', 'N100': 'Netherlands', 'NSEI': 'India', 
    'TWII': 'Taiwan', 'GSPTSE': 'Canada', 'J203.JO': 'South Africa', 'SSMI': 'Switzerland'
}

df['Country'] = df['Index'].map(index_country)

# Filter for 2000 onwards
df_2000 = df[df['Date'] >= '2000-01-01'].copy()

# Calculate monthly investment returns for each index
results = []
for idx in df_2000['Index'].unique():
    idx_data = df_2000[df_2000['Index'] == idx].sort_values('Date')
    
    # Skip if insufficient data
    if len(idx_data) < 100:
        continue
    
    # Get monthly closing prices (last day of each month)
    idx_data['Period'] = idx_data['Date'].dt.to_period('M')
    monthly = idx_data.groupby('Period').agg({'CloseUSD': 'last', 'Date': 'last'}).reset_index()
    monthly = monthly.sort_values('Period')
    
    # Dollar cost averaging: $100 invested monthly
    total_invested = 0
    total_shares = 0
    monthly_investment = 100
    
    for _, row in monthly.iterrows():
        price = row['CloseUSD']
        if price > 0:
            total_shares += monthly_investment / price
            total_invested += monthly_investment
    
    if total_invested == 0:
        continue
    
    final_price = monthly['CloseUSD'].iloc[-1]
    final_value = total_shares * final_price
    roi = ((final_value - total_invested) / total_invested) * 100
    
    results.append({
        'Index': idx,
        'Country': idx_data['Country'].iloc[0],
        'Months': len(monthly),
        'Total_Invested': total_invested,
        'Final_Value': round(final_value, 2),
        'ROI_Percent': round(roi, 2)
    })

# Sort by ROI and get top 5
top5 = pd.DataFrame(results).sort_values('ROI_Percent', ascending=False).head(5)

print('__RESULT__:')
print(top5.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
