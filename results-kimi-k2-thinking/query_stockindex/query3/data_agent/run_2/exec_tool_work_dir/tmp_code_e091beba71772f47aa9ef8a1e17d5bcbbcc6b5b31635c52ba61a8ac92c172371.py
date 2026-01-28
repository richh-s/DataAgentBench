code = """import json
import pandas as pd

# Load the data file path
file_path_key = 'var_functions.query_db:52'
if file_path_key in globals():
    file_path = globals()[file_path_key]
elif file_path_key in locals():
    file_path = locals()[file_path_key]
else:
    file_path = None

print(f'File path: {file_path}')

if file_path:
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    print(f'Loaded {len(data)} records')
    print('Sample record:', data[0])
    
    # Create DataFrame
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=False)
    df['CloseUSD'] = df['CloseUSD'].astype(float)
    
    # Sort
    df = df.sort_values(['Index', 'Date'])
    
    # Get stats
    stats = {
        'total_records': len(df),
        'indices': sorted(df['Index'].unique().tolist()),
        'date_min': str(df['Date'].min()),
        'date_max': str(df['Date'].max())
    }
    
    print('__RESULT__:')
    print(json.dumps(stats))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': [{'Index': 'N225', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'GSPTSE', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'NSEI', 'first_date': '2007-09-25 00:00:00', 'last_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'GDAXI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'IXIC', 'first_date': '2000-01-06 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'HSI', 'first_date': '2000-01-14 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'NYA', 'first_date': '2000-01-03 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': '000001.SS', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'SSMI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'first_date': '2000-01-17 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'N100', 'first_date': '2000-01-10 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': '399001.SZ', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'J203.JO', 'first_date': '2012-02-08 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.list_db:26': ['index_info'], 'var_functions.query_db:28': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:30': [{'Index': 'N225', 'Date': '2000-01-04 00:00:00', 'Open': '18937.44922', 'High': '19187.60938', 'Low': '18937.44922', 'Close': '19002.85938', 'Adj Close': '19002.85938', 'CloseUSD': '190.0285938'}, {'Index': 'N225', 'Date': '2000-01-19 00:00:00', 'Open': '19181.86914', 'High': '19181.86914', 'Low': '18897.75', 'Close': '18897.75', 'Adj Close': '18897.75', 'CloseUSD': '188.9775'}, {'Index': 'N225', 'Date': '2000-01-20 00:00:00', 'Open': '18930.25977', 'High': '19167.0293', 'Low': '18921.10938', 'Close': '19008.00977', 'Adj Close': '19008.00977', 'CloseUSD': '190.0800977'}, {'Index': 'N225', 'Date': '2000-01-24 00:00:00', 'Open': '18878.46094', 'High': '19124.57031', 'Low': '18877.13086', 'Close': '19056.71094', 'Adj Close': '19056.71094', 'CloseUSD': '190.5671094'}, {'Index': 'N225', 'Date': '2000-01-25 00:00:00', 'Open': '19004.39063', 'High': '19131.18945', 'Low': '18815.36914', 'Close': '18895.5293', 'Adj Close': '18895.5293', 'CloseUSD': '188.955293'}], 'var_functions.execute_python:32': {'000001.SS': {'exchange': 'Shanghai Stock Exchange', 'country': 'China', 'name': 'Shanghai Composite'}, '399001.SZ': {'exchange': 'Shenzhen Stock Exchange', 'country': 'China', 'name': 'Shenzhen Component'}, 'GDAXI': {'exchange': 'Frankfurt Stock Exchange', 'country': 'Germany', 'name': 'DAX'}, 'GSPTSE': {'exchange': 'Toronto Stock Exchange', 'country': 'Canada', 'name': 'TSX Composite'}, 'HSI': {'exchange': 'Hong Kong Stock Exchange', 'country': 'Hong Kong', 'name': 'Hang Seng Index'}, 'IXIC': {'exchange': 'NASDAQ', 'country': 'United States', 'name': 'NASDAQ Composite'}, 'J203.JO': {'exchange': 'Johannesburg Stock Exchange', 'country': 'South Africa', 'name': 'JSE All Share'}, 'N100': {'exchange': 'Euronext', 'country': 'Netherlands/Belgium/France', 'name': 'Euronext 100'}, 'N225': {'exchange': 'Tokyo Stock Exchange', 'country': 'Japan', 'name': 'Nikkei 225'}, 'NSEI': {'exchange': 'National Stock Exchange of India', 'country': 'India', 'name': 'NIFTY 50'}, 'NYA': {'exchange': 'New York Stock Exchange', 'country': 'United States', 'name': 'NYSE Composite'}, 'SSMI': {'exchange': 'SIX Swiss Exchange', 'country': 'Switzerland', 'name': 'Swiss Market Index'}, 'TWII': {'exchange': 'Taiwan Stock Exchange', 'country': 'Taiwan', 'name': 'Taiwan Weighted Index'}}, 'var_functions.execute_python:36': {'valid_indices': ['000001.SS', '399001.SZ', 'GDAXI'], 'count': 3}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': [{'total_records': '54808'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:48': {'total_indices': 11, 'valid_indices': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'N100', 'N225', 'NYA', 'SSMI', 'TWII']}, 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
