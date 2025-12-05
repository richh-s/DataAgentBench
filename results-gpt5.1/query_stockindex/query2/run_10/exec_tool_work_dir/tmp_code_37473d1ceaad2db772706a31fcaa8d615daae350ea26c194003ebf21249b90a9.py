code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_QBJi4K2Nb1pNUymMA1IlSKz9)
records = json.loads(path.read_text())

df = pd.DataFrame(records)
for col in ['Open','Close']:
    df[col] = df[col].astype(float)

up_down = df.assign(
    up = df['Close'] > df['Open'],
    down = df['Close'] < df['Open']
).groupby('Index')[['up','down']].sum()

north_america = ['NYA','IXIC','GSPTSE']
result_indices = [idx for idx in up_down.index if idx in north_america and up_down.loc[idx,'up'] > up_down.loc[idx,'down']]

result = json.dumps(result_indices)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_0Vc6RcshCSIdUcfujb3ZvpAI': ['index_info'], 'var_call_kSpdVT8Ur6JwptowvQr934VM': ['index_trade'], 'var_call_8R54XorW5XRDuo6BrWnDj7Fv': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_yUPdCOzG4N9boQFSZ36NdfBH': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}], 'var_call_QBJi4K2Nb1pNUymMA1IlSKz9': 'file_storage/call_QBJi4K2Nb1pNUymMA1IlSKz9.json'}

exec(code, env_args)
