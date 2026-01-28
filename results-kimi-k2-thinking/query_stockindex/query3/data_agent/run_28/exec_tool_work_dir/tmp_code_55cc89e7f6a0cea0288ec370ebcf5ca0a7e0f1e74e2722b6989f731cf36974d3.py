code = """import json
import pandas as pd
import numpy as np

# Load the complete dataset
file_path = var_functions.query_db:10
print('Loading data from:', file_path)

with open(file_path, 'r') as f:
    all_records = json.load(f)

print('Total records loaded:', len(all_records))

# Create DataFrame
df = pd.DataFrame(all_records)

# Convert data types
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter out invalid data
df = df.dropna(subset=['Date', 'CloseUSD'])
df = df[df['CloseUSD'] > 0]

print('Valid records after cleaning:', len(df))
print('Date range:', df['Date'].min(), 'to', df['Date'].max())
print('Unique indices:', sorted(df['Index'].unique()))

# Map index symbols to countries
country_map = {
    'NYA': 'United States',
    'IXIC': 'United States', 
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'N225': 'Japan',
    'N100': 'Europe',
    'GDAXI': 'Germany',
    'NSEI': 'India',
    'GSPTSE': 'Canada',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'J203.JO': 'South Africa'
}

# Calculate dollar-cost averaging returns for each index
results = []

for index_symbol in df['Index'].unique():
    # Get data for this index from 2000 onwards
    index_data = df[(df['Index'] == index_symbol) & (df['Date'] >= '2000-01-01')].copy()
    
    if len(index_data) < 12:  # Need at least 12 months
        continue
    
    # Sort by date
    index_data = index_data.sort_values('Date')
    
    # Get monthly prices (first trading day of each month)
    index_data['YearMonth'] = index_data['Date'].dt.to_period('M')
    monthly_prices = index_data.groupby('YearMonth')['CloseUSD'].first()
    
    if len(monthly_prices) == 0:
        continue
    
    # Dollar-cost averaging: invest $100 each month
    total_invested = 0.0
    total_shares = 0.0
    
    for price in monthly_prices:
        if price > 0 and not pd.isna(price):
            total_invested += 100.0
            total_shares += 100.0 / price
    
    if total_invested == 0:
        continue
    
    # Calculate final portfolio value
    final_price = index_data['CloseUSD'].iloc[-1]
    final_value = total_shares * final_price
    
    # Calculate returns
    total_return = final_value - total_invested
    return_percent = (total_return / total_invested) * 100.0
    
    # Get country
    country = country_map.get(index_symbol, 'Unknown')
    
    results.append({
        'Index': index_symbol,
        'Country': country,
        'Total_Invested': round(total_invested, 2),
        'Final_Value': round(final_value, 2),
        'Return_Percent': round(return_percent, 2),
        'Months': len(monthly_prices)
    })

print('Processed indices:', len(results))

# Sort by return percentage and get top 5
top_5 = sorted(results, key=lambda x: x['Return_Percent'], reverse=True)[:5]

print('Top 5 performing indices:')
for i, item in enumerate(top_5, 1):
    print(f"{i}. {item['Index']} ({item['Country']}): {item['Return_Percent']}% return")

# Return the final result as JSON
result_json = json.dumps(top_5)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GDAXI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'GSPTSE', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'first_date': '2000-01-14 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'first_date': '2000-01-06 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'J203.JO', 'first_date': '2012-02-08 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N100', 'first_date': '2000-01-10 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'NSEI', 'first_date': '2007-09-25 00:00:00', 'last_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'NYA', 'first_date': '2000-01-03 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'SSMI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'first_date': '2000-01-17 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.execute_python:30': []}

exec(code, env_args)
