code = """import json
import pandas as pd
import os

# Load the trade data file
file_path = var_functions.query_db:8

df = pd.read_json(file_path)

# Convert data types
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Define index to country mapping
index_mapping = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    'GDAXI': 'Germany',
    'IXIC': 'USA',
    'NYA': 'USA',
    'N100': 'Netherlands',
    'NSEI': 'India',
    'TWII': 'Taiwan',
    '399001.SZ': 'China',
    'GSPTSE': 'Canada',
    'J203.JO': 'South Africa',
    'SSMI': 'Switzerland'
}

# Add country info and filter for 2000 onwards
df['Country'] = df['Index'].map(index_mapping)
df_2000 = df[df['Date'] >= '2000-01-01'].copy()

# Calculate regular monthly investment returns for each index
results = []

for index in df_2000['Index'].unique():
    index_data = df_2000[df_2000['Index'] == index].copy()
    index_data = index_data.sort_values('Date')
    
    if len(index_data) < 12:  # Need at least a year of data
        continue
    
    # Group by month and take the last trading day of each month
    index_data['YearMonth'] = index_data['Date'].dt.to_period('M')
    monthly_data = index_data.groupby('YearMonth').agg({
        'CloseUSD': 'last',
        'Date': 'last'
    }).reset_index()
    
    # Calculate returns assuming $100 invested at the end of each month
    total_invested = 0
    total_shares = 0
    monthly_investment = 100
    
    for i, row in monthly_data.iterrows():
        if i == 0:
            # First month - buy at the first available price
            price = row['CloseUSD']
        else:
            # Subsequent months - buy at this month's price
            price = row['CloseUSD']
        
        if price > 0:
            shares = monthly_investment / price
            total_shares += shares
            total_invested += monthly_investment
    
    # Get final value
    final_price = monthly_data['CloseUSD'].iloc[-1]
    final_value = total_shares * final_price
    total_return = ((final_value - total_invested) / total_invested) * 100 if total_invested > 0 else 0
    
    country = index_mapping.get(index, 'Unknown')
    
    results.append({
        'Index': index,
        'Country': country,
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Total_Return_Percent': round(total_return, 2),
        'Data_Points': len(monthly_data)
    })

# Sort by total return and get top 5
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Total_Return_Percent', ascending=False)
top_5 = results_df.head(5)

print('__RESULT__:')
print(top_5.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
