code = """import json
import os
import re
from datetime import datetime

# Load trade data
trade_data_key = 'var_functions.query_db:6'
if trade_data_key in locals():
    trade_data = locals()[trade_data_key]
else:
    trade_data = None

# Load data (file path or direct)
if isinstance(trade_data, str) and os.path.exists(trade_data):
    with open(trade_data, 'r') as f:
        index_trade = json.load(f)
else:
    index_trade = trade_data

print('Total records:', len(index_trade))

# Asia indices present in data
asia_indices = ['000001.SS', '399001.SZ', 'HSI', 'N225', 'NSEI', 'TWII']

# Filter Asia indices and dates from 2020 onwards
asia_records = []
for record in index_trade:
    idx = record.get('Index')
    if idx in asia_indices:
        date_str = record.get('Date', '')
        # Check if year 2020-2023 appears in date string
        if any(year in date_str for year in ['2020', '2021', '2022', '2023']):
            asia_records.append(record)

print(f'Asia records from 2020+: {len(asia_records)}')

# Calculate intraday volatility
volatility_by_index = {idx: [] for idx in asia_indices}

for record in asia_records:
    try:
        open_val = float(record.get('Open', 0))
        high_val = float(record.get('High', 0))
        low_val = float(record.get('Low', 0))
        
        if open_val > 0:
            volatility = (high_val - low_val) / open_val
            idx = record['Index']
            volatility_by_index[idx].append(volatility)
    except:
        continue

# Calculate averages
results = {}
for idx, vols in volatility_by_index.items():
    if vols:
        avg_vol = sum(vols) / len(vols)
        results[idx] = {'avg_volatility': avg_vol, 'days': len(vols)}

# Sort by volatility
top_indices = sorted(results.items(), key=lambda x: x[1]['avg_volatility'], reverse=True)

print('\nResults:')
for idx, data in top_indices:
    print(f'{idx}: {data["avg_volatility"]:.6f} across {data["days"]} days')

result = None
if top_indices:
    result = {
        'index_symbol': top_indices[0][0],
        'avg_volatility': top_indices[0][1]['avg_volatility']
    }

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'total_records': 48151, 'first_record': {'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, 'last_record': {'Index': 'J203.JO', 'Date': '31 May 2021, 00:00', 'Open': '67554.85938', 'High': '68140.85156', 'Low': '67554.85938', 'Close': '67964.03906', 'Adj Close': '67964.03906', 'CloseUSD': '4757.4827342'}, 'unique_indices': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII']}}

exec(code, env_args)
