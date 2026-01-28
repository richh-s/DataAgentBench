code = """import json
import pandas as pd
import numpy as np

# Get the file path containing all trade data
file_path = var_functions.query_db:56

# Load the data
with open(file_path, 'r') as f:
    data = json.load(f)

print('Loaded records:', len(data))

# Create DataFrame and clean data
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter valid data from 2000 onwards
mask = (df['Date'] >= '2000-01-01') & (df['CloseUSD'] > 0)
mask = mask & df['Date'].notna() & df['CloseUSD'].notna()
df_clean = df[mask].copy()

print('Valid 2000+ records:', len(df_clean))
print('Indices:', sorted(df_clean['Index'].unique()))

# Country mapping
country_map = {}
country_map['NYA'] = 'United States'
country_map['IXIC'] = 'United States'
country_map['HSI'] = 'Hong Kong'
country_map['000001.SS'] = 'China'
country_map['399001.SZ'] = 'China'
country_map['N225'] = 'Japan'
country_map['N100'] = 'Europe'
country_map['GDAXI'] = 'Germany'
country_map['NSEI'] = 'India'
country_map['GSPTSE'] = 'Canada'
country_map['SSMI'] = 'Switzerland'
country_map['TWII'] = 'Taiwan'
country_map['J203.JO'] = 'South Africa'

# Calculate DCA returns
results = []

for idx in df_clean['Index'].unique():
    sub = df_clean[df_clean['Index'] == idx].copy()
    
    # Need minimum data
    if len(sub) < 12:
        continue
    
    sub = sub.sort_values('Date')
    sub['Month'] = sub['Date'].dt.to_period('M')
    monthly = sub.groupby('Month').first().reset_index()
    
    # DCA calculation
    invested = 0.0
    shares = 0.0
    for i, row in monthly.iterrows():
        price = row['CloseUSD']
        if price > 0:
            invested = invested + 100.0
            shares = shares + (100.0 / price)
    
    if invested == 0:
        continue
    
    # Final value
    final_price = sub['CloseUSD'].iloc[-1]
    final_value = shares * final_price
    return_pct = ((final_value / invested) - 1.0) * 100.0
    
    country_val = country_map.get(idx, 'Unknown')
    results.append({'Index': idx, 'Country': country_val, 'Return_Percent': round(return_pct, 2)})

# Get top 5
top_5 = sorted(results, key=lambda x: x['Return_Percent'], reverse=True)[:5]

print('Top 5:', top_5)

result_str = json.dumps(top_5)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GDAXI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'GSPTSE', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'first_date': '2000-01-14 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'first_date': '2000-01-06 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'J203.JO', 'first_date': '2012-02-08 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N100', 'first_date': '2000-01-10 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'NSEI', 'first_date': '2007-09-25 00:00:00', 'last_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'NYA', 'first_date': '2000-01-03 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'SSMI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'first_date': '2000-01-17 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.execute_python:30': [], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': [{'Index': 'J203.JO', 'start_date': '2012-02-08 00:00:00', 'end_date': 'September 30, 2019 at 12:00 AM', 'records': '1854'}, {'Index': 'HSI', 'start_date': '2000-01-14 00:00:00', 'end_date': 'September 30, 2019 at 12:00 AM', 'records': '5604'}, {'Index': 'NYA', 'start_date': '2000-01-03 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'records': '7960'}, {'Index': 'N100', 'start_date': '2000-01-10 00:00:00', 'end_date': 'September 30, 2019 at 12:00 AM', 'records': '4245'}, {'Index': '399001.SZ', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2015 at 12:00 AM', 'records': '4355'}, {'Index': 'N225', 'start_date': '2000-01-04 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'records': '7979'}, {'Index': 'GSPTSE', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2016 at 12:00 AM', 'records': '6506'}, {'Index': 'NSEI', 'start_date': '2007-09-25 00:00:00', 'end_date': 'September 30, 2014 at 12:00 AM', 'records': '2577'}, {'Index': 'GDAXI', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2016 at 12:00 AM', 'records': '5590'}, {'Index': '000001.SS', 'start_date': '2000-01-04 00:00:00', 'end_date': 'September 30, 2015 at 12:00 AM', 'records': '4354'}, {'Index': 'SSMI', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'records': '5188'}, {'Index': 'TWII', 'start_date': '2000-01-17 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'records': '4385'}, {'Index': 'IXIC', 'start_date': '2000-01-06 00:00:00', 'end_date': 'September 30, 2015 at 12:00 AM', 'records': '7351'}], 'var_functions.query_db:54': [{'Index': '000001.SS', 'start_date': '2000-01-04 00:00:00', 'end_date': 'September 30, 2015 at 12:00 AM', 'records': '4354', 'min_price': '161.9355176', 'max_price': '965.80492192'}, {'Index': '399001.SZ', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2015 at 12:00 AM', 'records': '4355', 'min_price': '411.37601568', 'max_price': '3124.9840624'}, {'Index': 'GDAXI', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2016 at 12:00 AM', 'records': '5590', 'min_price': '1158.0727878', 'max_price': '18934.3761734'}, {'Index': 'GSPTSE', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2016 at 12:00 AM', 'records': '6506', 'min_price': '1122.40904067', 'max_price': '16477.325352599997'}, {'Index': 'HSI', 'start_date': '2000-01-14 00:00:00', 'end_date': 'September 30, 2019 at 12:00 AM', 'records': '5604', 'min_price': '265.27799688', 'max_price': '4310.0357417000005'}, {'Index': 'IXIC', 'start_date': '2000-01-06 00:00:00', 'end_date': 'September 30, 2015 at 12:00 AM', 'records': '7351', 'min_price': '55.48', 'max_price': '14138.78027'}, {'Index': 'J203.JO', 'start_date': '2012-02-08 00:00:00', 'end_date': 'September 30, 2019 at 12:00 AM', 'records': '1854', 'min_price': '2302.1214454000005', 'max_price': '4805.917265800001'}, {'Index': 'N100', 'start_date': '2000-01-10 00:00:00', 'end_date': 'September 30, 2019 at 12:00 AM', 'records': '4245', 'min_price': '531.27340122', 'max_price': '1541.6163939'}, {'Index': 'N225', 'start_date': '2000-01-04 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'records': '7979', 'min_price': '10.2677002', 'max_price': '388.7694141'}, {'Index': 'NSEI', 'start_date': '2007-09-25 00:00:00', 'end_date': 'September 30, 2014 at 12:00 AM', 'records': '2577', 'min_price': '25.24199951', 'max_price': '155.8279981'}, {'Index': 'NYA', 'start_date': '2000-01-03 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'records': '7960', 'min_price': '347.769989', 'max_price': '16590.42969'}, {'Index': 'SSMI', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'records': '5188', 'min_price': '1466.19902664', 'max_price': '12683.026932900002'}, {'Index': 'TWII', 'start_date': '2000-01-17 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'records': '4385', 'min_price': '137.8504004', 'max_price': '703.8360156'}], 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json'}

exec(code, env_args)
