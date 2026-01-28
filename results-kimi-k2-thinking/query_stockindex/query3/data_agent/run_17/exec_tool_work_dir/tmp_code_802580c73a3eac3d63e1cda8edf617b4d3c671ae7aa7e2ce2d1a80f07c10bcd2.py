code = """import json
import pandas as pd
import numpy as np

# Load the data from the JSON file
file_path = locals()['var_functions.query_db:8']

with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Map index symbols to countries
index_to_country = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'IXIC': 'United States',
    'J203.JO': 'South Africa',
    'N100': 'Netherlands/Europe',
    'NSEI': 'India',
    'NYA': 'United States',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan'
}

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert Date to datetime and Adj Close to float
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Adj Close'] = pd.to_numeric(df['Adj Close'], errors='coerce')
df['Country'] = df['Index'].map(index_to_country)

# Filter data from 2000 onwards
df_filtered = df[df['Date'] >= '2000-01-01'].copy()

# Remove any rows with missing data
df_clean = df_filtered.dropna(subset=['Date', 'Adj Close', 'Index'])

# Group by index and calculate monthly returns assuming $100 invested monthly from 2000
results = []

for index in df_clean['Index'].unique():
    index_data = df_clean[df_clean['Index'] == index].copy()
    
    if index_data.empty:
        continue
    
    # Sort by date
    index_data = index_data.sort_values('Date')
    
    # Extract year-month for grouping
    index_data['YearMonth'] = index_data['Date'].dt.to_period('M')
    
    # Get first trading day of each month (for monthly investment)
    monthly_first = index_data.groupby('YearMonth').first().reset_index()
    
    if monthly_first.empty:
        continue
    
    # Calculate monthly investment returns (assuming $100 invested at the start of each month)
    total_invested = 0
    total_shares = 0
    
    for _, row in monthly_first.iterrows():
        if pd.notna(row['Adj Close']) and row['Adj Close'] > 0:
            total_invested += 100  # $100 invested monthly
            total_shares += 100 / row['Adj Close']
    
    # Get final value (using the last available price)
    final_price = index_data['Adj Close'].iloc[-1]
    final_value = total_shares * final_price
    
    # Calculate total return
    if total_invested > 0:
        total_return = (final_value - total_invested) / total_invested * 100
        
        # Get the country
        country = index_to_country.get(index, 'Unknown')
        
        results.append({
            'Index': index,
            'Country': country,
            'Total_Invested': total_invested,
            'Final_Value': final_value,
            'Total_Return_Percent': total_return,
            'Months_Invested': len(monthly_first)
        })

# Sort by total return percentage and get top 5
top_5_indices = sorted(results, key=lambda x: x['Total_Return_Percent'], reverse=True)[:5]

result_json = json.dumps(top_5_indices, indent=2)

print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
