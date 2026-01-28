code = """import json
import pandas as pd

file_path = var_functions.query_db:8

with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])
for col in ['Open', 'High', 'Low', 'Close', 'Adj Close', 'CloseUSD']:
    df[col] = pd.to_numeric(df[col])

df['is_up'] = df['Close'] > df['Open']
df['is_down'] = df['Close'] < df['Open']

results = []
for idx in df['Index'].unique():
    idx_data = df[df['Index'] == idx]
    up_days = int(idx_data['is_up'].sum())
    down_days = int(idx_data['is_down'].sum())
    results.append({
        'Index': idx,
        'UpDays': up_days,
        'DownDays': down_days,
        'Net': up_days - down_days
    })

winners = [r for r in results if r['Net'] > 0]

print('__RESULT__:')
print(json.dumps({
    'all_indices': results,
    'winners': winners
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
