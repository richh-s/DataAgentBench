code = """import pandas as pd
import json
import numpy as np

# Get the data from the storage variable
storage_key = 'var_functions.query_db:26'
if storage_key in locals():
    file_path = locals()[storage_key]
    if isinstance(file_path, str):
        with open(file_path, 'r') as f:
            data = json.load(f)
    else:
        data = file_path
else:
    # Fallback - use the other query result
    data = locals().get('var_functions.query_db:18', [])

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Create country mapping
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

# Calculate returns for each index
results = []
for idx in df['Index'].unique():
    idx_data = df[df['Index'] == idx].sort_values('Date')
    
    # Dollar cost averaging: invest $100 at the start of each month
    monthly_data = []
    current_month = None
    
    for _, row in idx_data.iterrows():
        month_key = (row['Date'].year, row['Date'].month)
        if month_key != current_month:
            current_month = month_key
            monthly_data.append({
                'price': row['CloseUSD'],
                'investment': 100,
                'shares': 100 / row['CloseUSD']
            })
    
    if monthly_data:
        total_invested = sum(m['investment'] for m in monthly_data)
        total_shares = sum(m['shares'] for m in monthly_data)
        final_price = idx_data.iloc[-1]['CloseUSD']
        final_value = total_shares * final_price
        total_return = ((final_value - total_invested) / total_invested) * 100
        
        results.append({
            'Index': idx,
            'Country': country_map[idx],
            'Total_Return_Pct': total_return,
            'Investment_Period': f"{idx_data.iloc[0]['Date'].strftime('%Y-%m')} to {idx_data.iloc[-1]['Date'].strftime('%Y-%m')}",
            'Monthly_Investments': len(monthly_data)
        })

# Sort and get top 5
top_5 = sorted(results, key=lambda x: x['Total_Return_Pct'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top_5, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': 'Error: File not found at /tmp/tmpu4l8a_7i/index_trade_data.json', 'var_functions.query_db:12': [{'Index': '000001.SS', 'earliest_date': '2000-01-04 00:00:00', 'latest_date': 'September 30, 2015 at 12:00 AM', 'total_days': '4354'}, {'Index': '399001.SZ', 'earliest_date': '2000-01-05 00:00:00', 'latest_date': 'September 30, 2015 at 12:00 AM', 'total_days': '4355'}, {'Index': 'GDAXI', 'earliest_date': '2000-01-05 00:00:00', 'latest_date': 'September 30, 2016 at 12:00 AM', 'total_days': '5590'}, {'Index': 'GSPTSE', 'earliest_date': '2000-01-05 00:00:00', 'latest_date': 'September 30, 2016 at 12:00 AM', 'total_days': '6506'}, {'Index': 'HSI', 'earliest_date': '2000-01-14 00:00:00', 'latest_date': 'September 30, 2019 at 12:00 AM', 'total_days': '5604'}, {'Index': 'IXIC', 'earliest_date': '2000-01-06 00:00:00', 'latest_date': 'September 30, 2015 at 12:00 AM', 'total_days': '7351'}, {'Index': 'J203.JO', 'earliest_date': '2012-02-08 00:00:00', 'latest_date': 'September 30, 2019 at 12:00 AM', 'total_days': '1854'}, {'Index': 'N100', 'earliest_date': '2000-01-10 00:00:00', 'latest_date': 'September 30, 2019 at 12:00 AM', 'total_days': '4245'}, {'Index': 'N225', 'earliest_date': '2000-01-04 00:00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_days': '7979'}, {'Index': 'NSEI', 'earliest_date': '2007-09-25 00:00:00', 'latest_date': 'September 30, 2014 at 12:00 AM', 'total_days': '2577'}, {'Index': 'NYA', 'earliest_date': '2000-01-03 00:00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_days': '7960'}, {'Index': 'SSMI', 'earliest_date': '2000-01-05 00:00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_days': '5188'}, {'Index': 'TWII', 'earliest_date': '2000-01-17 00:00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_days': '4385'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'Index': 'J203.JO', 'record_count': '1854'}, {'Index': 'N225', 'record_count': '7979'}, {'Index': 'GSPTSE', 'record_count': '6506'}, {'Index': 'NSEI', 'record_count': '2577'}, {'Index': 'GDAXI', 'record_count': '5590'}, {'Index': 'IXIC', 'record_count': '7351'}, {'Index': 'HSI', 'record_count': '5604'}, {'Index': 'NYA', 'record_count': '7960'}, {'Index': '000001.SS', 'record_count': '4354'}, {'Index': 'SSMI', 'record_count': '5188'}, {'Index': 'TWII', 'record_count': '4385'}, {'Index': 'N100', 'record_count': '4245'}, {'Index': '399001.SZ', 'record_count': '4355'}], 'var_functions.execute_python:24': "Available storage variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:8', 'var_functions.execute_python:10', 'var_functions.query_db:12', 'var_functions.query_db:18', 'var_functions.query_db:22']", 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': "File not found error: [Errno 2] No such file or directory: '/tmp/tmpu4l8a_7i/index_trade_data.json'"}

exec(code, env_args)
