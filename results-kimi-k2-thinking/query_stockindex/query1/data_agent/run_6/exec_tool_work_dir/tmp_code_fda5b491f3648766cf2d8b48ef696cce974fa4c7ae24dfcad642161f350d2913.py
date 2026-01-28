code = """import json, pandas as pd, re
from datetime import datetime

file_path = str(locals()['var_functions.query_db:8'])

with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Create DataFrame
df = pd.DataFrame(trade_data)

print(f'Total records: {len(df)}')
print(f'Columns: {list(df.columns)}')
print(f'Indices: {sorted(df["Index"].unique())}')

# Show sample dates
print('\nSample dates:')
for i in range(min(5, len(df))):
    print(f"  {df.iloc[i]['Date']}")"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'index_name': 'J203.JO'}, {'index_name': 'N225'}, {'index_name': 'GSPTSE'}, {'index_name': 'NSEI'}, {'index_name': 'GDAXI'}, {'index_name': 'IXIC'}, {'index_name': 'HSI'}, {'index_name': 'NYA'}, {'index_name': '000001.SS'}, {'index_name': 'SSMI'}, {'index_name': 'TWII'}, {'index_name': 'N100'}, {'index_name': '399001.SZ'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.execute_python:7': {'asia_indices': ['N225', 'HSI', '000001.SS', '399001.SZ', 'TWII', 'NSEI']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': {'total_records': 20187, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'unique_indices': ['HSI', '000001.SS', 'N225', '399001.SZ', 'NSEI', 'TWII']}, 'var_functions.execute_python:24': [{'index': '399001.SZ', 'avg_volatility': 0.019375, 'trading_days': 39}, {'index': 'NSEI', 'avg_volatility': 0.017565, 'trading_days': 34}, {'index': 'HSI', 'avg_volatility': 0.014769, 'trading_days': 40}, {'index': 'N225', 'avg_volatility': 0.014314, 'trading_days': 40}, {'index': '000001.SS', 'avg_volatility': 0.01418, 'trading_days': 29}, {'index': 'TWII', 'avg_volatility': 0.013563, 'trading_days': 45}], 'var_functions.execute_python:28': []}

exec(code, env_args)
