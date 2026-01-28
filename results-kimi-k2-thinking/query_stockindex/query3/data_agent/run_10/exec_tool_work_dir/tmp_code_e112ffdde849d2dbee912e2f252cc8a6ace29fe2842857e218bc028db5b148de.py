code = """import pandas as pd
import numpy as np
import json

# Get data from the storage variable
result_key = 'var_functions.query_db:26'
file_path = '/tmp/tmpu4l8a_7i/index_trade_data.json'

try:
    with open(file_path, 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])
    
    # Create country mapping for each index
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
    
    # Add country column
    df['Country'] = df['Index'].map(country_map)
    
    # Group by index and get price range
    stats = []
    for idx in df['Index'].unique():
        idx_data = df[df['Index'] == idx]
        stats.append({
            'Index': idx,
            'Country': country_map[idx],
            'Records': len(idx_data),
            'Start_Date': idx_data['Date'].min().strftime('%Y-%m-%d'),
            'End_Date': idx_data['Date'].max().strftime('%Y-%m-%d'),
            'Start_Price': idx_data['CloseUSD'].iloc[0],
            'End_Price': idx_data['CloseUSD'].iloc[-1]
        })
    
    stats_df = pd.DataFrame(stats)
    stats_df['Price_Change_Pct'] = (stats_df['End_Price'] / stats_df['Start_Price'] - 1) * 100
    
    # Sort by price change percentage
    stats_df = stats_df.sort_values('Price_Change_Pct', ascending=False)
    
    print('__RESULT__:')
    print(stats_df.to_json(orient='records', indent=2))
    
except FileNotFoundError as e:
    print('__RESULT__:')
    print(json.dumps(f"File not found error: {e}"))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': 'Error: File not found at /tmp/tmpu4l8a_7i/index_trade_data.json', 'var_functions.query_db:12': [{'Index': '000001.SS', 'earliest_date': '2000-01-04 00:00:00', 'latest_date': 'September 30, 2015 at 12:00 AM', 'total_days': '4354'}, {'Index': '399001.SZ', 'earliest_date': '2000-01-05 00:00:00', 'latest_date': 'September 30, 2015 at 12:00 AM', 'total_days': '4355'}, {'Index': 'GDAXI', 'earliest_date': '2000-01-05 00:00:00', 'latest_date': 'September 30, 2016 at 12:00 AM', 'total_days': '5590'}, {'Index': 'GSPTSE', 'earliest_date': '2000-01-05 00:00:00', 'latest_date': 'September 30, 2016 at 12:00 AM', 'total_days': '6506'}, {'Index': 'HSI', 'earliest_date': '2000-01-14 00:00:00', 'latest_date': 'September 30, 2019 at 12:00 AM', 'total_days': '5604'}, {'Index': 'IXIC', 'earliest_date': '2000-01-06 00:00:00', 'latest_date': 'September 30, 2015 at 12:00 AM', 'total_days': '7351'}, {'Index': 'J203.JO', 'earliest_date': '2012-02-08 00:00:00', 'latest_date': 'September 30, 2019 at 12:00 AM', 'total_days': '1854'}, {'Index': 'N100', 'earliest_date': '2000-01-10 00:00:00', 'latest_date': 'September 30, 2019 at 12:00 AM', 'total_days': '4245'}, {'Index': 'N225', 'earliest_date': '2000-01-04 00:00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_days': '7979'}, {'Index': 'NSEI', 'earliest_date': '2007-09-25 00:00:00', 'latest_date': 'September 30, 2014 at 12:00 AM', 'total_days': '2577'}, {'Index': 'NYA', 'earliest_date': '2000-01-03 00:00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_days': '7960'}, {'Index': 'SSMI', 'earliest_date': '2000-01-05 00:00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_days': '5188'}, {'Index': 'TWII', 'earliest_date': '2000-01-17 00:00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_days': '4385'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'Index': 'J203.JO', 'record_count': '1854'}, {'Index': 'N225', 'record_count': '7979'}, {'Index': 'GSPTSE', 'record_count': '6506'}, {'Index': 'NSEI', 'record_count': '2577'}, {'Index': 'GDAXI', 'record_count': '5590'}, {'Index': 'IXIC', 'record_count': '7351'}, {'Index': 'HSI', 'record_count': '5604'}, {'Index': 'NYA', 'record_count': '7960'}, {'Index': '000001.SS', 'record_count': '4354'}, {'Index': 'SSMI', 'record_count': '5188'}, {'Index': 'TWII', 'record_count': '4385'}, {'Index': 'N100', 'record_count': '4245'}, {'Index': '399001.SZ', 'record_count': '4355'}], 'var_functions.execute_python:24': "Available storage variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:8', 'var_functions.execute_python:10', 'var_functions.query_db:12', 'var_functions.query_db:18', 'var_functions.query_db:22']", 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
