code = """import json
import pandas as pd
import numpy as np

# The result is stored as a file path string
file_path = var_functions.query_db:10
print('File path:', file_path)

# Check file existence and size
import os
if os.path.exists(file_path):
    size_mb = os.path.getsize(file_path) / (1024 * 1024)
    print('File exists, size:', size_mb, 'MB')
else:
    print('File does not exist')

# Load data from file
with open(file_path, 'r') as f:
    all_data = json.load(f)

print('Records loaded:', len(all_data))

# Convert to DataFrame
df = pd.DataFrame(all_data)

# Convert data types
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['Date', 'CloseUSD'])

print('Clean records:', len(df))
print('Indices:', sorted(df['Index'].unique()))

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

results = []
for index_name in sorted(df['Index'].unique()):
    idx_data = df[df['Index'] == index_name].copy()
    idx_data = idx_data.sort_values('Date')
    idx_data = idx_data[idx_data['Date'] >= '2000-01-01']
    
    if len(idx_data) < 12:
        continue
    
    monthly_investment = 100.0
    total_invested = 0.0
    total_shares = 0.0
    
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    monthly_prices = idx_data.groupby('YearMonth').first()['CloseUSD'].dropna()
    
    for price in monthly_prices:
        if price > 0:
            total_invested += monthly_investment
            total_shares += monthly_investment / price
    
    if total_invested == 0:
        continue
    
    final_price = idx_data.iloc[-1]['CloseUSD']
    final_value = total_shares * final_price
    total_return = final_value - total_invested
    return_percent = (total_return / total_invested) * 100.0
    
    days = (idx_data['Date'].max() - idx_data['Date'].min()).days
    years = days / 365.25
    
    annualized_return = 0.0
    if years > 0:
        annualized_return = ((final_value / total_invested)  ** (1.0 / years) - 1.0) * 100.0
    
    country = index_to_country.get(index_name, 'Unknown')
    
    results.append({
        'Index': index_name,
        'Country': country,
        'Total_Invested': round(total_invested, 2),
        'Final_Value': round(final_value, 2),
        'Return_Percent': round(return_percent, 2),
        'Years': round(years, 1),
        'Annualized_Return': round(annualized_return, 2)
    })

# Sort by return percent
top_5 = sorted(results, key=lambda x: x['Return_Percent'], reverse=True)[:5]

print('\nTop 5:')
for item in top_5:
    print(item)

# Return as JSON string
result_str = json.dumps(top_5)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GDAXI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'GSPTSE', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'first_date': '2000-01-14 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'first_date': '2000-01-06 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'J203.JO', 'first_date': '2012-02-08 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N100', 'first_date': '2000-01-10 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'NSEI', 'first_date': '2007-09-25 00:00:00', 'last_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'NYA', 'first_date': '2000-01-03 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'SSMI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'first_date': '2000-01-17 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
