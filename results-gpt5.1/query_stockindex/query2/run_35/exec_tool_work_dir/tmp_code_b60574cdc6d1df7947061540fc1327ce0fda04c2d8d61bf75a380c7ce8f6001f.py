code = """import json, pandas as pd
import os

path = var_call_Fu6Zoab5ceOS97Lae3bwzncd
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

north_american_indices = ['NYA','IXIC','GSPTSE']

res = []
for idx in north_american_indices:
    sub = df[df['Index']==idx]
    up = (sub['Close']>sub['Open']).sum()
    down = (sub['Close']<sub['Open']).sum()
    res.append({'Index': idx, 'up_days': int(up), 'down_days': int(down), 'more_up_than_down': bool(up>down)})

result = json.dumps(res)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_6jNDAmxvnbvAZGeuW38eeILA': ['index_info'], 'var_call_GQejekG18BuCUrvTlb7WhpDg': ['index_trade'], 'var_call_wS67aPZxmib49f08z5579Xx9': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_Ot94HXmPoey5PqbcaCUtGA5V': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_call_Fu6Zoab5ceOS97Lae3bwzncd': 'file_storage/call_Fu6Zoab5ceOS97Lae3bwzncd.json'}

exec(code, env_args)
