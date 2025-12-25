code = """import json
import pandas as pd

file_path = var_call_lN9MSQUnTToSVu4Ba3O10Y6D
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open', 'Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

na_indices = ['NYA', 'IXIC', 'GSPTSE']

results = []
for idx in na_indices:
    sub = df[df['Index'] == idx].copy()
    up_days = (sub['Close'] > sub['Open']).sum()
    down_days = (sub['Close'] < sub['Open']).sum()
    results.append({'Index': idx, 'up_days': int(up_days), 'down_days': int(down_days), 'more_up_than_down': bool(up_days > down_days)})

result_json = json.dumps(results)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_call_J5s5s6inkFdoQ9Hectvx6Za2': ['index_info'], 'var_call_rBy7m3qZWJimKvF6cYXQfDlg': ['index_trade'], 'var_call_0BxcFsX0b5zraS9srZZOHNTs': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_iWbYfz41DMdIBINUdZD3HHJM': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'J203.JO'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_lN9MSQUnTToSVu4Ba3O10Y6D': 'file_storage/call_lN9MSQUnTToSVu4Ba3O10Y6D.json'}

exec(code, env_args)
