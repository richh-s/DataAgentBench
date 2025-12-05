code = """import json, pandas as pd
from pathlib import Path

file_path = var_call_EZ0hHvOu5JoA6c0j4aM7412F
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

north_american_indices = ['NYA','IXIC','GSPTSE']
na_df = df[df['Index'].isin(north_american_indices)].copy()

up_down = na_df.assign(
    up = na_df['Close'] > na_df['Open'],
    down = na_df['Close'] < na_df['Open']
).groupby('Index').agg({'up':'sum','down':'sum'})

result = []
for idx, row in up_down.iterrows():
    if row['up'] > row['down']:
        result.append({'Index': idx, 'up_days': int(row['up']), 'down_days': int(row['down'])})

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_XkxMMi6cCSq7EjFd4i7T6qAf': ['index_info'], 'var_call_vy2PbP3KAkaSkOMAZGArXaZR': ['index_trade'], 'var_call_cDvZuKexd5forftgVM6FQt9Y': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_uOzLF5bCrg0Hv5J7MNqhc4hj': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'IXIC'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_EZ0hHvOu5JoA6c0j4aM7412F': 'file_storage/call_EZ0hHvOu5JoA6c0j4aM7412F.json'}

exec(code, env_args)
