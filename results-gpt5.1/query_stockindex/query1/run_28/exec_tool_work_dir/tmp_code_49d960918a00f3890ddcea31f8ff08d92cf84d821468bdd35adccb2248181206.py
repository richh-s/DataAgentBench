code = """import pandas as pd, json, os, ast
path = var_call_qDVx2zfRmCJ50SnSHH9K9vGZ
with open(path, 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)
# coerce numeric columns
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')
# parse dates robustly and filter since 2020-01-01
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce')
df = df[df['Date_parsed'] >= '2020-01-01']
# compute intraday volatility
df = df.dropna(subset=['Open','High','Low'])
df = df[df['Open'] != 0]
df['vol'] = (df['High'] - df['Low']) / df['Open']
res = df.groupby('Index')['vol'].mean().sort_values(ascending=False)
result = {idx: float(val) for idx, val in res.items()}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_P0yfUlSD6Dta6quzekVqwA6t': ['index_info'], 'var_call_5GyY5LtS0YQH3BYpKIbDsKe4': ['index_trade'], 'var_call_ABvtFo70iXeVCuPtTx7LW85R': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_l37l8TcG7N4Zarqe6hxDCnoO': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}], 'var_call_SUbbt1zxNL1xRbeLGEp1Sa7z': ['N225', 'HSI', '000001.SS', '399001.SZ', 'NSEI', 'TWII'], 'var_call_qDVx2zfRmCJ50SnSHH9K9vGZ': 'file_storage/call_qDVx2zfRmCJ50SnSHH9K9vGZ.json'}

exec(code, env_args)
