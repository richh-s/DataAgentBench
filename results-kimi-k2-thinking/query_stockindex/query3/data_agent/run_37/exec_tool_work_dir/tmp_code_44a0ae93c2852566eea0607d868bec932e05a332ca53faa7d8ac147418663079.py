code = """import json
import pandas as pd
import numpy as np
from datetime import datetime

# Read the full data from the file
file_path = locals().get('var_functions.query_db:14')

if isinstance(file_path, str) and __import__('os').path.exists(file_path):
    with open(file_path, 'r') as f:
        trade_data = json.load(f)
else:
    trade_data = locals().get('var_functions.query_db:14', [])

print('Loaded', len(trade_data), 'trading records')

# Create DataFrame and clean data
df = pd.DataFrame(trade_data)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter data from 2000-01-01 onwards
df = df[df['Date'] >= '2000-01-01'].copy()
df = df.sort_values(['Index', 'Date']).reset_index(drop=True)

# Index symbol to exchange mapping
index_to_exchange = {
    'NYA': 'New York Stock Exchange',
    'IXIC': 'NASDAQ',
    'HSI': 'Hong Kong Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange',
    'N225': 'Tokyo Stock Exchange',
    'N100': 'Euronext',
    '399001.SZ': 'Shenzhen Stock Exchange',
    'GSPTSE': 'Toronto Stock Exchange',
    'NSEI': 'National Stock Exchange of India',
    'GDAXI': 'Frankfurt Stock Exchange',
    'SSMI': 'SIX Swiss Exchange',
    'TWII': 'Taiwan Stock Exchange',
    'J203.JO': 'Johannesburg Stock Exchange'
}

# Exchange to country mapping
exchange_to_country = {
    'New York Stock Exchange': 'United States',
    'NASDAQ': 'United States',
    'Hong Kong Stock Exchange': 'Hong Kong',
    'Shanghai Stock Exchange': 'China',
    'Tokyo Stock Exchange': 'Japan',
    'Euronext': 'Netherlands',
    'Shenzhen Stock Exchange': 'China',
    'Toronto Stock Exchange': 'Canada',
    'National Stock Exchange of India': 'India',
    'Frankfurt Stock Exchange': 'Germany',
    'SIX Swiss Exchange': 'Switzerland',
    'Taiwan Stock Exchange': 'Taiwan',
    'Johannesburg Stock Exchange': 'South Africa'
}

results = []

for idx in df['Index'].unique():
    if idx not in index_to_exchange:
        continue
    
    group = df[df['Index'] == idx].copy()
    group['YearMonth'] = group['Date'].dt.to_period('M')
    monthly_data = group.groupby('YearMonth').first().reset_index()
    
    if len(monthly_data) < 24:  # At least 2 years of data
        continue
    
    monthly_data = monthly_data.sort_values('YearMonth')
    
    # Calculate returns from regular monthly investments
    investment_per_month = 100
    total_invested = 0
    total_shares = 0
    
    for _, row in monthly_data.iterrows():
        if pd.notna(row['CloseUSD']) and row['CloseUSD'] > 0:
            total_shares += investment_per_month / row['CloseUSD']
            total_invested += investment_per_month
    
    if total_invested == 0:
        continue
    
    final_value = total_shares * monthly_data['CloseUSD'].iloc[-1]
    total_return = (final_value - total_invested) / total_invested
    
    exchange = index_to_exchange[idx]
    country = exchange_to_country[exchange]
    
    results.append({
        'Index': idx,
        'Country': country,
        'TotalReturn': total_return,
        'FinalValue': final_value,
        'TotalInvested': total_invested,
        'Months': len(monthly_data)
    })

# Sort by total return
top_5 = sorted(results, key=lambda x: x['TotalReturn'], reverse=True)[:5]

print('Top 5 indices:')
for i, item in enumerate(top_5, 1):
    ret = item['TotalReturn']
    print(i, item['Index'], item['Country'], 'Return:', round(ret * 100, 2))

print('__RESULT__:')
print(json.dumps({'top_5': top_5}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:7': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:8': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:9': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': 'January 15, 1987 at 12:00 AM', 'Open': '2559.100098', 'High': '2559.100098', 'Low': '2559.100098', 'Close': '2559.100098', 'Adj Close': '2559.100098', 'CloseUSD': '332.68301274'}, {'Index': 'HSI', 'Date': 'January 16, 1987 at 12:00 AM', 'Open': '2542.600098', 'High': '2542.600098', 'Low': '2542.600098', 'Close': '2542.600098', 'Adj Close': '2542.600098', 'CloseUSD': '330.53801274'}, {'Index': 'HSI', 'Date': 'January 19, 1987 at 12:00 AM', 'Open': '2460.5', 'High': '2460.5', 'Low': '2460.5', 'Close': '2460.5', 'Adj Close': '2460.5', 'CloseUSD': '319.865'}, {'Index': 'HSI', 'Date': 'January 21, 1987 at 12:00 AM', 'Open': '2533.899902', 'High': '2533.899902', 'Low': '2533.899902', 'Close': '2533.899902', 'Adj Close': '2533.899902', 'CloseUSD': '329.40698726000005'}, {'Index': 'HSI', 'Date': '22 Jan 1987, 00:00', 'Open': '2536.899902', 'High': '2536.899902', 'Low': '2536.899902', 'Close': '2536.899902', 'Adj Close': '2536.899902', 'CloseUSD': '329.79698726000004'}, {'Index': 'HSI', 'Date': 'January 23, 1987 at 12:00 AM', 'Open': '2499.399902', 'High': '2499.399902', 'Low': '2499.399902', 'Close': '2499.399902', 'Adj Close': '2499.399902', 'CloseUSD': '324.92198726000004'}, {'Index': 'HSI', 'Date': 'January 26, 1987 at 12:00 AM', 'Open': '2484.399902', 'High': '2484.399902', 'Low': '2484.399902', 'Close': '2484.399902', 'Adj Close': '2484.399902', 'CloseUSD': '322.97198726000005'}, {'Index': 'HSI', 'Date': '27 Jan 1987, 00:00', 'Open': '2524.0', 'High': '2524.0', 'Low': '2524.0', 'Close': '2524.0', 'Adj Close': '2524.0', 'CloseUSD': '328.12'}], 'var_functions.execute_python:13': {'index_info_count': 14, 'index_trade_sample_count': 10, 'sample_trades': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': 'January 15, 1987 at 12:00 AM', 'Open': '2559.100098', 'High': '2559.100098', 'Low': '2559.100098', 'Close': '2559.100098', 'Adj Close': '2559.100098', 'CloseUSD': '332.68301274'}]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
