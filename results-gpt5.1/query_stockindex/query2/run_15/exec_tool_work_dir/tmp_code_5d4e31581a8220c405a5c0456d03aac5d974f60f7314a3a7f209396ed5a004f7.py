code = """import json, pandas as pd, os

path = var_call_cS75nmSioh0usM95gJJ88Xgr
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

mask_2018 = df['Date'].str.startswith('2018-')
df_2018 = df[mask_2018].copy()

up = df_2018[df_2018['Close'] > df_2018['Open']].groupby('Index').size()
down = df_2018[df_2018['Close'] < df_2018['Open']].groupby('Index').size()

result_indices = []
for idx in sorted(df_2018['Index'].unique()):
    up_days = int(up.get(idx, 0))
    down_days = int(down.get(idx, 0))
    if up_days > down_days:
        result_indices.append({'Index': idx, 'up_days': up_days, 'down_days': down_days})

res_json = json.dumps(result_indices)
print('__RESULT__:')
print(res_json)"""

env_args = {'var_call_7b0NDPIZbs0eSITTB2BfJOmh': ['index_info'], 'var_call_aIizDlOpjLXGDqOomeygKhYo': ['index_trade'], 'var_call_86vSrHKfPD5LKGDX9Qec4VqA': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_lU9BvLpA7Dl2DXCTIcvZwYOL': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_call_cS75nmSioh0usM95gJJ88Xgr': 'file_storage/call_cS75nmSioh0usM95gJJ88Xgr.json'}

exec(code, env_args)
