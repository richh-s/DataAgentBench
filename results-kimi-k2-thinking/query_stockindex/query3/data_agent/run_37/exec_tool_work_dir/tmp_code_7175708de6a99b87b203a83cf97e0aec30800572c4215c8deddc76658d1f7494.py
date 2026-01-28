code = """import json
import os
import pandas as pd
from datetime import datetime
import numpy as np

# Get the file path from storage
file_path = locals().get('var_functions.query_db:14')

# Read the full data from the file
if isinstance(file_path, str) and os.path.exists(file_path):
    with open(file_path, 'r') as f:
        trade_data = json.load(f)
else:
    trade_data = locals().get('var_functions.query_db:14', [])

print('Loaded', len(trade_data), 'trading records')

# Create DataFrame and clean data
df = pd.DataFrame(trade_data)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

# Filter data from 2000-01-01 onwards
df = df[df['Date'] >= '2000-01-01'].copy()
df = df.sort_values(['Index', 'Date']).reset_index(drop=True)

print('Filtered data:', len(df), 'records from', df['Date'].min(), 'to', df['Date'].max())
print('Indices available:', list(df['Index'].unique()))

# Index symbol to exchange mapping (based on common knowledge)
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

# Exchange to country/region mapping
exchange_mapping = {
    'New York Stock Exchange': ('United States', 'North America'),
    'NASDAQ': ('United States', 'North America'),
    'Hong Kong Stock Exchange': ('Hong Kong', 'Asia'),
    'Shanghai Stock Exchange': ('China', 'Asia'),
    'Tokyo Stock Exchange': ('Japan', 'Asia'),
    'Euronext': ('Netherlands/France/Belgium/Portugal', 'Europe'),
    'Shenzhen Stock Exchange': ('China', 'Asia'),
    'Toronto Stock Exchange': ('Canada', 'North America'),
    'National Stock Exchange of India': ('India', 'Asia'),
    'Frankfurt Stock Exchange': ('Germany', 'Europe'),
    'SIX Swiss Exchange': ('Switzerland', 'Europe'),
    'Taiwan Stock Exchange': ('Taiwan', 'Asia'),
    'Johannesburg Stock Exchange': ('South Africa', 'Africa')
}

# Add country and region info to data
def get_country_info(index_symbol):
    exchange = index_to_exchange.get(index_symbol, 'Unknown')
    if exchange != 'Unknown':
        country, region = exchange_mapping.get(exchange, ('Unknown', 'Unknown'))
        return country, region, exchange
    return 'Unknown', 'Unknown', 'Unknown'

# Apply mapping
country_info = df['Index'].apply(get_country_info)
df['Country'] = [info[0] for info in country_info]
df['Region'] = [info[1] for info in country_info]
df['Exchange'] = [info[2] for info in country_info]

print('\nData summary:')
summary = df.groupby(['Index', 'Country']).size().reset_index(name='Records')
print(summary.to_string(index=False))

# Calculate returns for regular monthly investments
def calculate_monthly_returns(group):
    # Get first trading day of each month
    group['YearMonth'] = group['Date'].dt.to_period('M')
    monthly_first = group.groupby('YearMonth').first().reset_index()
    
    if len(monthly_first) < 2:
        return None
    
    # Calculate monthly returns for regular investment
    monthly_first['Return'] = monthly_first['CloseUSD'].pct_change()
    
    # For regular monthly investment, calculate cumulative returns
    # Assuming $100 invested at the beginning of each month
    investment = 100
    shares = 0
    total_invested = 0
    
    for i, row in monthly_first.iterrows():
        if pd.notna(row['CloseUSD']):
            shares += investment / row['CloseUSD']
            total_invested += investment
    
    # Final value
    final_value = shares * monthly_first['CloseUSD'].iloc[-1]
    total_return = (final_value - total_invested) / total_invested
    
    return {
        'total_return': total_return,
        'final_value': final_value,
        'total_invested': total_invested,
        'months': len(monthly_first)
    }

# Calculate returns for each index
results = []
for idx in df['Index'].unique():
    if idx in index_to_exchange:  # Only include known indices
        group = df[df['Index'] == idx].copy()
        result = calculate_monthly_returns(group)
        if result:
            country, region, exchange = get_country_info(idx)
            results.append({
                'Index': idx,
                'Exchange': exchange,
                'Country': country,
                'Region': region,
                'TotalReturn': result['total_return'],
                'FinalValue': result['final_value'],
                'TotalInvested': result['total_invested'],
                'Months': result['months']
            })

# Sort by total return and get top 5
top_5 = sorted(results, key=lambda x: x['TotalReturn'], reverse=True)[:5]

print('\nTop 5 indices by regular monthly investment returns:')
for i, item in enumerate(top_5, 1):
    print(f"{i}. {item['Index']} ({item['Country']}) - Return: {item['TotalReturn']:.2%}")

# Save results
results_file = '/tmp/monthly_investment_returns.json'
with open(results_file, 'w') as f:
    json.dump(top_5, f, indent=2)

print('__RESULT__:')
print(json.dumps({
    'top_5_indices': top_5,
    'results_file': results_file
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:7': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:8': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:9': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': 'January 15, 1987 at 12:00 AM', 'Open': '2559.100098', 'High': '2559.100098', 'Low': '2559.100098', 'Close': '2559.100098', 'Adj Close': '2559.100098', 'CloseUSD': '332.68301274'}, {'Index': 'HSI', 'Date': 'January 16, 1987 at 12:00 AM', 'Open': '2542.600098', 'High': '2542.600098', 'Low': '2542.600098', 'Close': '2542.600098', 'Adj Close': '2542.600098', 'CloseUSD': '330.53801274'}, {'Index': 'HSI', 'Date': 'January 19, 1987 at 12:00 AM', 'Open': '2460.5', 'High': '2460.5', 'Low': '2460.5', 'Close': '2460.5', 'Adj Close': '2460.5', 'CloseUSD': '319.865'}, {'Index': 'HSI', 'Date': 'January 21, 1987 at 12:00 AM', 'Open': '2533.899902', 'High': '2533.899902', 'Low': '2533.899902', 'Close': '2533.899902', 'Adj Close': '2533.899902', 'CloseUSD': '329.40698726000005'}, {'Index': 'HSI', 'Date': '22 Jan 1987, 00:00', 'Open': '2536.899902', 'High': '2536.899902', 'Low': '2536.899902', 'Close': '2536.899902', 'Adj Close': '2536.899902', 'CloseUSD': '329.79698726000004'}, {'Index': 'HSI', 'Date': 'January 23, 1987 at 12:00 AM', 'Open': '2499.399902', 'High': '2499.399902', 'Low': '2499.399902', 'Close': '2499.399902', 'Adj Close': '2499.399902', 'CloseUSD': '324.92198726000004'}, {'Index': 'HSI', 'Date': 'January 26, 1987 at 12:00 AM', 'Open': '2484.399902', 'High': '2484.399902', 'Low': '2484.399902', 'Close': '2484.399902', 'Adj Close': '2484.399902', 'CloseUSD': '322.97198726000005'}, {'Index': 'HSI', 'Date': '27 Jan 1987, 00:00', 'Open': '2524.0', 'High': '2524.0', 'Low': '2524.0', 'Close': '2524.0', 'Adj Close': '2524.0', 'CloseUSD': '328.12'}], 'var_functions.execute_python:13': {'index_info_count': 14, 'index_trade_sample_count': 10, 'sample_trades': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': 'January 15, 1987 at 12:00 AM', 'Open': '2559.100098', 'High': '2559.100098', 'Low': '2559.100098', 'Close': '2559.100098', 'Adj Close': '2559.100098', 'CloseUSD': '332.68301274'}]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
