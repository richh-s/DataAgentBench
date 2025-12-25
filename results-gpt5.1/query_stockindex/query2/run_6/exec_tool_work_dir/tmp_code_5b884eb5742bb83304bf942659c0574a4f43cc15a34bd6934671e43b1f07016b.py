code = """import json, pandas as pd

path = var_call_rQkkTYVXtDP8JlpvQQQw2ia4
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','Close']:
    df[col] = pd.to_numeric(df[col])

na_indices = ['NYA','IXIC','GSPTSE']
na_df = df[df['Index'].isin(na_indices)].copy()

summary = na_df.assign(
    up = na_df['Close'] > na_df['Open'],
    down = na_df['Close'] < na_df['Open']
).groupby('Index')[['up','down']].sum()

result = []
for idx, row in summary.iterrows():
    if row['up'] > row['down']:
        result.append(idx)

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_yIkEh4ld4ZKqwWFWYn7RkdST': ['index_info'], 'var_call_RGVqTKuync2E4ltALVFooai2': ['index_trade'], 'var_call_49G5AhpnEV1ZMzIiPz32QJ9l': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_19musTQNbRIc7LDFfCNjLqni': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_rQkkTYVXtDP8JlpvQQQw2ia4': 'file_storage/call_rQkkTYVXtDP8JlpvQQQw2ia4.json'}

exec(code, env_args)
