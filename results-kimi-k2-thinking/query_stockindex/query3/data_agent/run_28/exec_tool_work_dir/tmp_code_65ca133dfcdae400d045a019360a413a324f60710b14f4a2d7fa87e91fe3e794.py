code = """import json
import pandas as pd
import numpy as np
import os

# Load the trade data from file
file_path = var_functions.query_db:10
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert data types
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['Date', 'CloseUSD'])

print('Data loaded successfully')
print('Total records:', len(df))
print('Unique indices:', df['Index'].nunique())
print('All indices:', sorted(df['Index'].unique()))

# Map indices to countries
index_to_country = {
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
for index_name in sorted(df['Index'].unique()):
    idx_data = df[df['Index'] == index_name].copy()
    idx_data = idx_data[idx_data['Date'] >= '2000-01-01'].sort_values('Date')
    
    # Skip indices with less than 12 months of data
    if len(idx_data) < 12:
        continue
    
    # Get monthly prices (first trading day of each month)
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    monthly_prices = idx_data.groupby('YearMonth')['CloseUSD'].first()
    
    # Skip if no valid prices
    if len(monthly_prices) == 0 or monthly_prices.sum() == 0:
        continue
    
    # Dollar-cost averaging: invest $100 monthly
    total_invested = 0.0
    total_shares = 0.0
    
    for price in monthly_prices:
        if price > 0 and not pd.isna(price):
            total_invested += 100.0
            total_shares += 100.0 / price
    
    if total_invested == 0:
        continue
    
    # Calculate final value
    final_price = idx_data['CloseUSD'].iloc[-1]
    final_value = total_shares * final_price
    total_return = final_value - total_invested
    return_percent = (total_return / total_invested) * 100.0
    
    # Calculate time period
    days = (idx_data['Date'].iloc[-1] - idx_data['Date'].iloc[0]).days
    years = days / 365.25
    
    results.append({
        'Index': index_name,
        'Country': index_to_country.get(index_name, 'Unknown'),
        'Total_Invested': round(float(total_invested), 2),
        'Final_Value': round(float(final_value), 2),
        'Return_Percent': round(float(return_percent), 2),
        'Years': round(float(years), 1)
    })

# Sort by return percentage and get top 5
top_5_indices = sorted(results, key=lambda x: x['Return_Percent'], reverse=True)[:5]

print('Processed indices:', len(results))
print('Top 5 results:')
for item in top_5_indices:
    print(item)

# Return the top 5 in the required format
result_json = json.dumps(top_5_indices)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GDAXI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'GSPTSE', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'first_date': '2000-01-14 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'first_date': '2000-01-06 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'J203.JO', 'first_date': '2012-02-08 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N100', 'first_date': '2000-01-10 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'NSEI', 'first_date': '2007-09-25 00:00:00', 'last_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'NYA', 'first_date': '2000-01-03 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'SSMI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'first_date': '2000-01-17 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
