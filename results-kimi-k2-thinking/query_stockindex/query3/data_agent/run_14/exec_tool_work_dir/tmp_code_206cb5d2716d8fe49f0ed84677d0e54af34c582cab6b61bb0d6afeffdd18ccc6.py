code = """import pandas as pd
import json
import numpy as np
from datetime import datetime

# Read the trading data from storage
trade_result = locals()['var_functions.query_db:14']

# Load the data
if isinstance(trade_result, str) and trade_result.endswith('.json'):
    with open(trade_result, 'r') as f:
        trade_data = json.load(f)
else:
    trade_data = trade_result

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert CloseUSD to numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Convert Date to datetime using explicit format
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S')

print("Data loaded successfully")
print(f"Total records: {len(df)}")
print(f"Indices: {sorted(df['Index'].unique())}")
print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")

print("__RESULT__:")
print(json.dumps({"status": "success", "records": len(df), "indices_count": len(df['Index'].unique()), "date_min": str(df['Date'].min()), "date_max": str(df['Date'].max())}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.list_db:8': ['index_info'], 'var_functions.execute_python:12': [{'Index': 'N225', 'Exchange': 'Tokyo Stock Exchange', 'Country': 'Japan', 'Currency': 'JPY'}, {'Index': 'HSI', 'Exchange': 'Hong Kong Stock Exchange', 'Country': 'Hong Kong', 'Currency': 'HKD'}, {'Index': '000001.SS', 'Exchange': 'Shanghai Stock Exchange', 'Country': 'China', 'Currency': 'CNY'}, {'Index': '399001.SZ', 'Exchange': 'Shenzhen Stock Exchange', 'Country': 'China', 'Currency': 'CNY'}, {'Index': 'NYA', 'Exchange': 'New York Stock Exchange', 'Country': 'USA', 'Currency': 'USD'}, {'Index': 'IXIC', 'Exchange': 'NASDAQ', 'Country': 'USA', 'Currency': 'USD'}, {'Index': 'GDAXI', 'Exchange': 'Frankfurt Stock Exchange', 'Country': 'Germany', 'Currency': 'EUR'}, {'Index': 'N100', 'Exchange': 'Euronext', 'Country': 'Europe', 'Currency': 'EUR'}, {'Index': 'GSPTSE', 'Exchange': 'Toronto Stock Exchange', 'Country': 'Canada', 'Currency': 'CAD'}, {'Index': 'NSEI', 'Exchange': 'National Stock Exchange of India', 'Country': 'India', 'Currency': 'INR'}, {'Index': 'SSMI', 'Exchange': 'SIX Swiss Exchange', 'Country': 'Switzerland', 'Currency': 'CHF'}, {'Index': 'TWII', 'Exchange': 'Taiwan Stock Exchange', 'Country': 'Taiwan', 'Currency': 'TWD'}, {'Index': 'J203.JO', 'Exchange': 'Johannesburg Stock Exchange', 'Country': 'South Africa', 'Currency': 'ZAR'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
