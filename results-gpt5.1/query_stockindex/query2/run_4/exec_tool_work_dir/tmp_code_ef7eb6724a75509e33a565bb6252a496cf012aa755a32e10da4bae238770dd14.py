code = """import json, pandas as pd

path = var_call_5JxDW6buulJGJPNj7gPNM3v5
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','Close']:
    df[col] = df[col].astype(float)

north_american = ['IXIC','NYA','GSPTSE']
na_df = df[df['Index'].isin(north_american)]

up_down = na_df.assign(
    up = na_df['Close'] > na_df['Open'],
    down = na_df['Close'] < na_df['Open']
).groupby('Index')[['up','down']].sum()

indices_more_up = up_down[up_down['up'] > up_down['down']].index.tolist()

result = json.dumps(indices_more_up)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_3YMxSnvYqtwWcBYDMbc71ZpU': ['index_info'], 'var_call_GNACYLcnGX6I1INAe6cmfpy4': ['index_trade'], 'var_call_C2cgYb3T1eiJwRjgYKV951er': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_5JxDW6buulJGJPNj7gPNM3v5': 'file_storage/call_5JxDW6buulJGJPNj7gPNM3v5.json'}

exec(code, env_args)
