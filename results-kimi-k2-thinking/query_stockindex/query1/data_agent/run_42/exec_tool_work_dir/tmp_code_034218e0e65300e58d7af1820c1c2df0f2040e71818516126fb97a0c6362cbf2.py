code = """import json
import os

# Load trade data
trade_data_key = 'var_functions.query_db:6'
if trade_data_key in locals():
    trade_data = locals()[trade_data_key]
else:
    trade_data = None

# Load data safely
try:
    if isinstance(trade_data, str):
        with open(trade_data, 'r') as f:
            index_trade = json.load(f)
    else:
        index_trade = trade_data
except:
    index_trade = []

print(f'Loaded {len(index_trade)} total records')

# Define Asia indices that are actually in our data
asia_indices = {
    '000001.SS': 'Shanghai Composite',
    '399001.SZ': 'Shenzhen Component',
    'HSI': 'Hang Seng Index',
    'N225': 'Nikkei 225',
    'NSEI': 'NIFTY 50',
    'TWII': 'Taiwan Weighted Index'
}

# Filter for Asia indices
asia_data = []
for record in index_trade:
    if record.get('Index') in asia_indices:
        asia_data.append(record)

print(f'Found {len(asia_data)} Asia region records')
print('Asia indices present:', list(set([r['Index'] for r in asia_data])))

# Calculate intraday volatility for each record from 2020 onwards
volatility_data = {}
for record in asia_data:
    # Parse date (handle different formats)
    date_str = record.get('Date', '')
    if '2020' in date_str or '2021' in date_str or '2022' in date_str or '2023' in date_str:
        try:
            # Extract numeric values
            open_price = float(record.get('Open', 0))
            high_price = float(record.get('High', 0))
            low_price = float(record.get('Low', 0))
            
            if open_price > 0:
                # Calculate intraday volatility: (High - Low) / Open
                volatility = (high_price - low_price) / open_price
                idx = record['Index']
                
                if idx not in volatility_data:
                    volatility_data[idx] = []
                volatility_data[idx].append(volatility)
                
        except (ValueError, TypeError) as e:
            continue

# Calculate average volatility for each index
results = {}
for idx, volatilities in volatility_data.items():
    if volatilities:
        avg_volatility = sum(volatilities) / len(volatilities)
        results[idx] = {
            'index_name': asia_indices[idx],
            'avg_volatility': avg_volatility,
            'data_points': len(volatilities)
        }

# Sort by average volatility
top_volatile = sorted(results.items(), key=lambda x: x[1]['avg_volatility'], reverse=True)

print('\nAverage Intraday Volatility by Asia Index (since 2020):')
for idx, data in top_volatile:
    print(f"{idx} ({data['index_name']}): {data['avg_volatility']:.6f} ({data['data_points']} days)")

if top_volatile:
    highest = top_volatile[0]
    result = {
        'index_symbol': highest[0],
        'index_name': highest[1]['index_name'],
        'avg_volatility': highest[1]['avg_volatility'],
        'data_points': highest[1]['data_points']
    }
else:
    result = None

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'total_records': 48151, 'first_record': {'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, 'last_record': {'Index': 'J203.JO', 'Date': '31 May 2021, 00:00', 'Open': '67554.85938', 'High': '68140.85156', 'Low': '67554.85938', 'Close': '67964.03906', 'Adj Close': '67964.03906', 'CloseUSD': '4757.4827342'}, 'unique_indices': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII']}}

exec(code, env_args)
