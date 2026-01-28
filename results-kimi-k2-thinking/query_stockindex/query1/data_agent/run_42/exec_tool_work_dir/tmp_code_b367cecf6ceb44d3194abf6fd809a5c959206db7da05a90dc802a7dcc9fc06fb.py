code = """import json
import os

# Load trade data
trade_data_key = 'var_functions.query_db:6'
if trade_data_key in locals():
    trade_data = locals()[trade_data_key]
else:
    trade_data = None

try:
    if isinstance(trade_data, str):
        with open(trade_data, 'r') as f:
            index_trade = json.load(f)
    else:
        index_trade = trade_data
except:
    index_trade = []

# Asia indices mapping based on the hint
asia_indices = {
    'N225': 'Tokyo Stock Exchange',      # Nikkei 225
    'HSI': 'Hong Kong Stock Exchange',   # Hang Seng Index
    '000001.SS': 'Shanghai Stock Exchange',  # Shanghai Composite
    'NSEI': 'National Stock Exchange of India',  # NIFTY 50
    'TWII': 'Taiwan Stock Exchange'      # Taiwan Weighted Index
}

# Filter for Asia indices from 2020 onwards
filtered_data = []
for record in index_trade:
    idx = record.get('Index')
    if idx in asia_indices:
        filtered_data.append(record)

print('Filtered Asia records:', len(filtered_data))
print('Unique Asia indices found:', sorted(set([r.get('Index') for r in filtered_data])))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'total_records': 48151, 'first_record': {'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, 'last_record': {'Index': 'J203.JO', 'Date': '31 May 2021, 00:00', 'Open': '67554.85938', 'High': '68140.85156', 'Low': '67554.85938', 'Close': '67964.03906', 'Adj Close': '67964.03906', 'CloseUSD': '4757.4827342'}, 'unique_indices': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII']}}

exec(code, env_args)
