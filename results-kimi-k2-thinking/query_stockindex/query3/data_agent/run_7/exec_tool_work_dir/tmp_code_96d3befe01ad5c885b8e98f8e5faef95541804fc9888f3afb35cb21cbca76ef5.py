code = """import pandas as pd
import json
import numpy as np
from datetime import datetime

# Load the price data from the JSON file
price_data_file = locals()['var_functions.query_db:6']
if isinstance(price_data_file, str):
    with open(price_data_file, 'r') as f:
        price_data = json.load(f)
else:
    price_data = price_data_file

# Convert to DataFrame
df = pd.DataFrame(price_data)

# Convert Date to datetime and CloseUSD to float
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Filter data from 2000 to 2019 (common period, as some indices end earlier)
start_date = '2000-01-01'
end_date = '2019-12-31'
df_filtered = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)].copy()

# Get first trading day of each month for each index
df_filtered['YearMonth'] = df_filtered['Date'].dt.to_period('M')
monthly_prices = df_filtered.groupby(['Index', 'YearMonth']).first().reset_index()

# Map indices to countries based on exchange info
index_to_country = {
    'NYA': 'United States',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    'N225': 'Japan',
    'N100': 'Europe (Euronext)',
    'GDAXI': 'Germany',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'J203.JO': 'South Africa',
    '000001.SS': 'China (Shanghai)',
    '399001.SZ': 'China (Shenzhen)'
}

# Simulate DCA: invest $100 at the beginning of each month
dca_results = []

for index in monthly_prices['Index'].unique():
    index_data = monthly_prices[monthly_prices['Index'] == index].sort_values('Date')
    
    if len(index_data) < 12:  # Skip indices with less than a year of data
        continue
    
    total_invested = 0
    total_shares = 0
    
    for _, row in index_data.iterrows():
        price = row['CloseUSD']
        if pd.notna(price) and price > 0:
            # Invest $100 each month
            total_invested += 100
            total_shares += 100 / price
    
    # Calculate final value using the last available price
    final_price = index_data.iloc[-1]['CloseUSD']
    final_value = total_shares * final_price
    total_return = (final_value / total_invested) - 1
    
    dca_results.append({
        'Index': index,
        'Country': index_to_country.get(index, 'Unknown'),
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Total_Return': total_return,
        'Months': len(index_data),
        'Start_Date': index_data.iloc[0]['Date'].strftime('%Y-%m-%d'),
        'End_Date': index_data.iloc[-1]['Date'].strftime('%Y-%m-%d')
    })

# Convert to DataFrame and sort by total return
dca_df = pd.DataFrame(dca_results)
dca_df = dca_df.sort_values('Total_Return', ascending=False)

# Get top 5 indices
top_5_indices = dca_df.head(5)

print('__RESULT__:')
print(json.dumps(top_5_indices.to_dict('records'), indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': '000001.SS', 'max(Date)': 'September 30, 2015 at 12:00 AM', 'min(Date)': '2000-01-04 00:00:00', 'record_count': '4354'}, {'Index': '399001.SZ', 'max(Date)': 'September 30, 2015 at 12:00 AM', 'min(Date)': '2000-01-05 00:00:00', 'record_count': '4355'}, {'Index': 'GDAXI', 'max(Date)': 'September 30, 2016 at 12:00 AM', 'min(Date)': '2000-01-05 00:00:00', 'record_count': '5590'}, {'Index': 'GSPTSE', 'max(Date)': 'September 30, 2016 at 12:00 AM', 'min(Date)': '2000-01-05 00:00:00', 'record_count': '6506'}, {'Index': 'HSI', 'max(Date)': 'September 30, 2019 at 12:00 AM', 'min(Date)': '2000-01-14 00:00:00', 'record_count': '5604'}, {'Index': 'IXIC', 'max(Date)': 'September 30, 2015 at 12:00 AM', 'min(Date)': '2000-01-06 00:00:00', 'record_count': '7351'}, {'Index': 'J203.JO', 'max(Date)': 'September 30, 2019 at 12:00 AM', 'min(Date)': '2012-02-08 00:00:00', 'record_count': '1854'}, {'Index': 'N100', 'max(Date)': 'September 30, 2019 at 12:00 AM', 'min(Date)': '2000-01-10 00:00:00', 'record_count': '4245'}, {'Index': 'N225', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'min(Date)': '2000-01-04 00:00:00', 'record_count': '7979'}, {'Index': 'NSEI', 'max(Date)': 'September 30, 2014 at 12:00 AM', 'min(Date)': '2007-09-25 00:00:00', 'record_count': '2577'}, {'Index': 'NYA', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'min(Date)': '2000-01-03 00:00:00', 'record_count': '7960'}, {'Index': 'SSMI', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'min(Date)': '2000-01-05 00:00:00', 'record_count': '5188'}, {'Index': 'TWII', 'max(Date)': 'September 30, 2020 at 12:00 AM', 'min(Date)': '2000-01-17 00:00:00', 'record_count': '4385'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'data_loaded': '20886 records', 'date_range': '2000-01-03 00:00:00 to 2020-12-30 00:00:00', 'indices': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII']}}

exec(code, env_args)
