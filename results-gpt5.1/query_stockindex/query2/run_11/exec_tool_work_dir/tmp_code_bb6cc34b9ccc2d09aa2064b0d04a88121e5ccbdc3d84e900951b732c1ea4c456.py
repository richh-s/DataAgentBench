code = """import json, pandas as pd
import os

path = var_call_4P3Ru0tWFcZSA4vbil4MTGRh
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','Close']:
    df[col] = df[col].astype(float)

north_american_indices = ['NYA','IXIC','GSPTSE']

mask = df['Index'].isin(north_american_indices)
na = df[mask].copy()

up_down = na.groupby('Index').apply(lambda g: pd.Series({
    'up_days': (g['Close']>g['Open']).sum(),
    'down_days': (g['Close']<g['Open']).sum()
})).reset_index()

res = up_down[up_down['up_days']>up_down['down_days']]['Index'].tolist()

result = json.dumps({'indices_with_more_up_than_down_days_2018_North_America': res})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_3YXHpjVAM66bPEXvQUhjupio': ['index_info'], 'var_call_ZMEWXMEn89Qg7pvQ6k5pozlJ': ['index_trade'], 'var_call_y90LMBLYppflGWff4WeBsKa3': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_ocNZXYYX9JSkRUrhi5VEI3pT': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_4P3Ru0tWFcZSA4vbil4MTGRh': 'file_storage/call_4P3Ru0tWFcZSA4vbil4MTGRh.json'}

exec(code, env_args)
