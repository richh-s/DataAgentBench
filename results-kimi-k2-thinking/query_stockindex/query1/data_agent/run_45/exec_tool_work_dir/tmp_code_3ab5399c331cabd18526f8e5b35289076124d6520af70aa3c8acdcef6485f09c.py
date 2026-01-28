code = """import json
import pandas as pd
from datetime import datetime
import re

# Load data from variables
index_info = globals()['var_functions.query_db:2']

# Load trade data from file
trade_file = globals()['var_functions.query_db:3']
with open(trade_file, 'r') as f:
    trade_data = json.load(f)

# Create DataFrames
df_info = pd.DataFrame(index_info)
df_trade = pd.DataFrame(trade_data)

# Parse dates
def parse_date(date_str):
    date_str = str(date_str)
    if ' at ' in date_str:
        # Format: "January 02, 1987 at 12:00 AM"
        dt = pd.to_datetime(date_str, format='%B %d, %Y at %I:%M %p')
        return dt
    elif ',' in date_str and 'at' not in date_str:
        # Format: "31 Dec 1986, 00:00" or "22 Jan 1987, 00:00"
        try:
            dt = pd.to_datetime(date_str, format='%d %b %Y, %H:%M')
        except:
            dt = pd.to_datetime(date_str, format='%d %b %Y, %H:%M')
        return dt
    else:
        try:
            dt = pd.to_datetime(date_str)
        except:
            return None
    return dt

df_trade['ParsedDate'] = df_trade['Date'].apply(parse_date)

# Filter for 2020 and later
df_2020 = df_trade[df_trade['ParsedDate'] >= datetime(2020, 1, 1)].copy()

# Map exchanges to index symbols for Asia region
asia_exchange_map = {
    'Tokyo Stock Exchange': ['N225'],
    'Hong Kong Stock Exchange': ['HSI'],
    'Shanghai Stock Exchange': ['000001.SS', '000002.SS', '000300.SS'],
    'Shenzhen Stock Exchange': ['399001.SZ', '399006.SZ'],
    'National Stock Exchange of India': ['NSEI', '^NSEI', 'NIFTY'],
    'Korea Exchange': ['KS11', '^KS11', 'KOSPI'],
    'Taiwan Stock Exchange': ['TWII', '^TWII']
}

# Get unique indices from trade data
unique_indices = df_2020['Index'].unique()
print('__RESULT__:')
result = {
    'unique_indices': list(unique_indices),
    'asia_map': asia_exchange_map,
    'records_2020': len(df_2020)
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:26': {'records': 14, 'sample': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}]}}

exec(code, env_args)
