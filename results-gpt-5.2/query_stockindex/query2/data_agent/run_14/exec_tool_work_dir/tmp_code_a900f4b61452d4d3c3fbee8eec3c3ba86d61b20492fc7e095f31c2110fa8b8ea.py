code = """import json, pandas as pd

df = pd.DataFrame(var_call_SKPaGMMtxlsMQo1uPFFcq2WY)
# cast counts
for c in ['up_days','down_days']:
    df[c]=pd.to_numeric(df[c])
df = df[df['up_days']>df['down_days']].copy()
name_map = {
    'IXIC':'NASDAQ Composite (US)',
    'NYA':'NYSE Composite (US)',
    'GSPTSE':'S&P/TSX Composite (Canada)'
}
df['name']=df['Index'].map(name_map).fillna(df['Index'])
result = df[['Index','name','up_days','down_days']].sort_values('Index').to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_WHatvS9q9WLeU4dSFsuPvxSs': ['index_info'], 'var_call_uC8C2tPWdKxoS8wfSw14Q5xx': ['index_trade'], 'var_call_w8zWJMEfgjd0NStuDicrc6ac': [], 'var_call_FHUY8NpTcZmq0ssw6o7ci6pi': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_SKPaGMMtxlsMQo1uPFFcq2WY': [{'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'NYA', 'up_days': '37.0', 'down_days': '42.0'}]}

exec(code, env_args)
