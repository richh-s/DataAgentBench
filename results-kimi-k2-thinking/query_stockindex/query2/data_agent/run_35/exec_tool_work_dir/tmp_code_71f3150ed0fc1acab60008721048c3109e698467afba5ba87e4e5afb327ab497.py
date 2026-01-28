code = """import json
import pandas as pd

# Access the file path from storage
file_path = locals()['var_functions.query_db:8']

# Load the data
with open(file_path, 'r') as file:
    data = json.load(file)

# Create DataFrame and process data
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Convert numeric columns
numeric_cols = ['Open', 'High', 'Low', 'Close']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col])

# Determine up days vs down days
df['is_up'] = df['Close'] > df['Open']
df['is_down'] = df['Close'] < df['Open']

# Group by index and count up/down days
results = []
for idx in df['Index'].unique():
    idx_data = df[df['Index'] == idx]
    up_days = int(idx_data['is_up'].sum())
    down_days = int(idx_data['is_down'].sum())
    results.append({
        'Index': idx,
        'UpDays': up_days,
        'DownDays': down_days,
        'NetDays': up_days - down_days
    })

# Filter for indices with more up days than down days
winners = [r for r in results if r['NetDays'] > 0]

print('__RESULT__:')
print(json.dumps({'results': results, 'winners': winners}, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
