code = """import json, pandas as pd

path = var_call_zhQ1Ou2OLVjoiukX9BlTjAY4
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','High','Low','Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# filter since 2020-01-01 by parsing flexible date strings
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df[df['Date'] >= '2020-01-01']

# Asia indices mapping based on symbols
asia_indices = ['N225','HSI','000001.SS','399001.SZ','TWII','NSEI']

asia_df = df[df['Index'].isin(asia_indices)].copy()
asia_df['intraday_vol'] = (asia_df['High'] - asia_df['Low']) / asia_df['Open']

result = asia_df.groupby('Index')['intraday_vol'].mean().sort_values(ascending=False)
result_dict = result.to_dict()

out = json.dumps(result_dict)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_yckXARN0ZnUrmYkjrNSErvEu': ['index_info'], 'var_call_DY8XJfZI9m6CBlyrKwfNq3d5': ['index_trade'], 'var_call_BiUCMlg7txmFiGbbbP9HOrPH': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}], 'var_call_zhQ1Ou2OLVjoiukX9BlTjAY4': 'file_storage/call_zhQ1Ou2OLVjoiukX9BlTjAY4.json'}

exec(code, env_args)
