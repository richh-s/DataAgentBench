code = """import json
import pandas as pd
import numpy as np
from pathlib import Path

# Load data from the file path
file_path = locals()['var_functions.query_db:50']

with open(file_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame and process
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Remove invalid data
df = df.dropna(subset=['Date', 'CloseUSD'])

# Filter from 2000 onwards
df_2000 = df[df['Date'] >= '2000-01-01'].copy()

# Create country mapping for indices
country_map = {
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'HSI': 'Hong Kong',
    'IXIC': 'USA',
    'J203.JO': 'South Africa',
    'N100': 'Netherlands',
    'N225': 'Japan',
    'NSEI': 'India',
    'NYA': 'USA',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan'
}

# Calculate DCA returns for each index
dca_results = []

for idx in df_2000['Index'].unique():
    idx_data = df_2000[df_2000['Index'] == idx].sort_values('Date').copy()
    
    if len(idx_data) < 12:  # Need at least 1 year of data
        continue
    
    # Track monthly investments (first trading day of each month)
    monthly_investments = []
    prev_month_year = (0, 0)  # (year, month)
    
    for _, row in idx_data.iterrows():
        current_month_year = (row['Date'].year, row['Date'].month)
        if current_month_year != prev_month_year:
            prev_month_year = current_month_year
            price = row['CloseUSD']
            shares = 100 / price  # Invest $100 each month
            monthly_investments.append({
                'price': price,
                'shares': shares,
                'investment': 100
            })
    
    # Calculate total returns
    total_invested = len(monthly_investments) * 100
    total_shares = sum(inv['shares'] for inv in monthly_investments)
    final_price = idx_data.iloc[-1]['CloseUSD']
    final_value = total_shares * final_price
    total_return_pct = ((final_value - total_invested) / total_invested) * 100
    
    # Calculate annualized return
    start_date = idx_data.iloc[0]['Date']
    end_date = idx_data.iloc[-1]['Date']
    years = (end_date - start_date).days / 365.25
    
    if years > 0:
        annualized_return = ((final_value / total_invested) ** (1/years) - 1) * 100
    else:
        annualized_return = 0
    
    dca_results.append({
        'Index': idx,
        'Country': country_map.get(idx, 'Unknown'),
        'Monthly_Investments': len(monthly_investments),
        'Total_Invested': round(total_invested, 2),
        'Final_Value': round(final_value, 2),
        'Total_Return_Pct': round(total_return_pct, 2),
        'Annualized_Return_Pct': round(annualized_return, 2),
        'Start_Date': start_date.strftime('%Y-%m-%d'),
        'End_Date': end_date.strftime('%Y-%m-%d'),
        'Years': round(years, 2)
    })

# Sort by total return percentage (descending) and get top 5
top_5 = sorted(dca_results, key=lambda x: x['Total_Return_Pct'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top_5, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': 'Error: File not found at /tmp/tmpu4l8a_7i/index_trade_data.json', 'var_functions.query_db:12': [{'Index': '000001.SS', 'earliest_date': '2000-01-04 00:00:00', 'latest_date': 'September 30, 2015 at 12:00 AM', 'total_days': '4354'}, {'Index': '399001.SZ', 'earliest_date': '2000-01-05 00:00:00', 'latest_date': 'September 30, 2015 at 12:00 AM', 'total_days': '4355'}, {'Index': 'GDAXI', 'earliest_date': '2000-01-05 00:00:00', 'latest_date': 'September 30, 2016 at 12:00 AM', 'total_days': '5590'}, {'Index': 'GSPTSE', 'earliest_date': '2000-01-05 00:00:00', 'latest_date': 'September 30, 2016 at 12:00 AM', 'total_days': '6506'}, {'Index': 'HSI', 'earliest_date': '2000-01-14 00:00:00', 'latest_date': 'September 30, 2019 at 12:00 AM', 'total_days': '5604'}, {'Index': 'IXIC', 'earliest_date': '2000-01-06 00:00:00', 'latest_date': 'September 30, 2015 at 12:00 AM', 'total_days': '7351'}, {'Index': 'J203.JO', 'earliest_date': '2012-02-08 00:00:00', 'latest_date': 'September 30, 2019 at 12:00 AM', 'total_days': '1854'}, {'Index': 'N100', 'earliest_date': '2000-01-10 00:00:00', 'latest_date': 'September 30, 2019 at 12:00 AM', 'total_days': '4245'}, {'Index': 'N225', 'earliest_date': '2000-01-04 00:00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_days': '7979'}, {'Index': 'NSEI', 'earliest_date': '2007-09-25 00:00:00', 'latest_date': 'September 30, 2014 at 12:00 AM', 'total_days': '2577'}, {'Index': 'NYA', 'earliest_date': '2000-01-03 00:00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_days': '7960'}, {'Index': 'SSMI', 'earliest_date': '2000-01-05 00:00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_days': '5188'}, {'Index': 'TWII', 'earliest_date': '2000-01-17 00:00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_days': '4385'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'Index': 'J203.JO', 'record_count': '1854'}, {'Index': 'N225', 'record_count': '7979'}, {'Index': 'GSPTSE', 'record_count': '6506'}, {'Index': 'NSEI', 'record_count': '2577'}, {'Index': 'GDAXI', 'record_count': '5590'}, {'Index': 'IXIC', 'record_count': '7351'}, {'Index': 'HSI', 'record_count': '5604'}, {'Index': 'NYA', 'record_count': '7960'}, {'Index': '000001.SS', 'record_count': '4354'}, {'Index': 'SSMI', 'record_count': '5188'}, {'Index': 'TWII', 'record_count': '4385'}, {'Index': 'N100', 'record_count': '4245'}, {'Index': '399001.SZ', 'record_count': '4355'}], 'var_functions.execute_python:24': "Available storage variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:8', 'var_functions.execute_python:10', 'var_functions.query_db:12', 'var_functions.query_db:18', 'var_functions.query_db:22']", 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': "File not found error: [Errno 2] No such file or directory: '/tmp/tmpu4l8a_7i/index_trade_data.json'", 'var_functions.execute_python:34': "Available storage variables: ['var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:8', 'var_functions.query_db:12', 'var_functions.query_db:18', 'var_functions.query_db:22', 'var_functions.query_db:26']", 'var_functions.execute_python:36': "Query DB variables: ['var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:8', 'var_functions.query_db:12', 'var_functions.query_db:18', 'var_functions.query_db:22', 'var_functions.query_db:26']", 'var_functions.query_db:40': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.execute_python:42': "Processed 1000 records, indices: ['TWII']", 'var_functions.execute_python:46': {'var_functions.list_db:0': "<class 'list'> len=1", 'var_functions.query_db:2': "<class 'list'> len=13", 'var_functions.query_db:5': "<class 'list'> len=14", 'var_functions.query_db:8': "<class 'str'>", 'var_functions.execute_python:10': "<class 'str'>", 'var_functions.query_db:12': "<class 'list'> len=13", 'var_functions.query_db:18': "<class 'str'>", 'var_functions.query_db:22': "<class 'list'> len=13", 'var_functions.execute_python:24': "<class 'str'>", 'var_functions.query_db:26': "<class 'str'>", 'var_functions.execute_python:28': "<class 'str'>", 'var_functions.execute_python:34': "<class 'str'>", 'var_functions.execute_python:36': "<class 'str'>", 'var_functions.query_db:40': "<class 'list'> len=14", 'var_functions.execute_python:42': "<class 'str'>", '__builtins__': "<class 'dict'>", 'json': "<class 'module'>", 'pd': "<class 'module'>", 'np': "<class 'module'>"}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:54': {'message': 'Loaded 21342 records from 2000-01-03 00:00:00 to 2021-06-02 00:00:00', 'indices': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII']}}

exec(code, env_args)
