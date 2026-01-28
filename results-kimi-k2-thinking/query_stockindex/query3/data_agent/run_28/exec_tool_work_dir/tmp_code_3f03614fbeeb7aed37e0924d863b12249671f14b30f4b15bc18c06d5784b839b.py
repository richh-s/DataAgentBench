code = """import json
import pandas as pd
import numpy as np
import os

# Load trade data from file
file_path = var_functions.query_db:10
with open(file_path, 'r') as f:
    data = json.load(f)

print('Loaded', len(data), 'records')

# Convert to DataFrame and clean data
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['Date', 'CloseUSD'])

print('Clean records:', len(df))
print('Date range:', df['Date'].min(), 'to', df['Date'].max())
print('Indices:', sorted(df['Index'].unique()))

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

# Calculate DCA returns
results = []
months_invested = []

for idx in sorted(df['Index'].unique()):
    sub = df[df['Index'] == idx].copy()
    sub = sub[sub['Date'] >= '2000-01-01'].sort_values('Date')
    
    if len(sub) < 12:
        continue
    
    # Group by month and get first price of each month
    sub['Month'] = sub['Date'].dt.to_period('M')
    monthly = sub.groupby('Month').first().reset_index()
    
    if len(monthly) == 0:
        continue
    
    # Calculate DCA
    total_invested = 0.0
    total_shares = 0.0
    
    for _, row in monthly.iterrows():
        price = row['CloseUSD']
        if price > 0 and not pd.isna(price):
            total_invested += 100.0
            total_shares += 100.0 / price
    
    if total_invested == 0:
        continue
    
    # Calculate returns
    final_price = sub['CloseUSD'].iloc[-1]
    final_value = total_shares * final_price
    total_return = final_value - total_invested
    return_pct = (total_return / total_invested) * 100.0
    
    # Calculate time period
    days = (sub['Date'].iloc[-1] - sub['Date'].iloc[0]).days
    years = days / 365.25
    
    country = index_to_country.get(idx, 'Unknown')
    
    results.append({
        'Index': idx,
        'Country': country,
        'Total_Invested': round(total_invested, 2),
        'Final_Value': round(final_value, 2),
        'Return_Percent': round(return_pct, 2),
        'Years': round(years, 1),
        'Months': len(monthly)
    })
    
    months_invested.append(len(monthly))

print('Processed indices:', len(results))
print('Average months invested:', np.mean(months_invested))

# Sort by return percentage
top_5 = sorted(results, key=lambda x: x['Return_Percent'], reverse=True)[:5]

print('Top 5:')
for item in top_5:
    print(item)

# Return results as JSON
result_json = json.dumps(top_5)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GDAXI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'GSPTSE', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'first_date': '2000-01-14 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'first_date': '2000-01-06 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'J203.JO', 'first_date': '2012-02-08 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N100', 'first_date': '2000-01-10 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'NSEI', 'first_date': '2007-09-25 00:00:00', 'last_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'NYA', 'first_date': '2000-01-03 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'SSMI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'first_date': '2000-01-17 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.execute_python:30': []}

exec(code, env_args)
