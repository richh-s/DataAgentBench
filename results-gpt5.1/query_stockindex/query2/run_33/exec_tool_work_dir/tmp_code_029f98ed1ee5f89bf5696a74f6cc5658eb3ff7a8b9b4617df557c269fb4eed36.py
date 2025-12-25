code = """import json, pandas as pd

path = var_call_OunRzvNknYcQgGThNXVALnE0
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

north_american_indices = ['NYA','IXIC','GSPTSE']
sub = df[df['Index'].isin(north_american_indices)]

result = []
for idx, g in sub.groupby('Index'):
    up = (g['Close'] > g['Open']).sum()
    down = (g['Close'] < g['Open']).sum()
    if up > down:
        result.append({'Index': idx, 'up_days': int(up), 'down_days': int(down)})

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_EYTiux8RB3jFFFyIW0u9sWFW': ['index_info'], 'var_call_53LMwuhNNZBkpiHv8gq6sKT2': ['index_trade'], 'var_call_26d11hfwh6dmzeADDPdJsA6Y': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_tXHze4DoaUURzuWGUYSNpBx5': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_OunRzvNknYcQgGThNXVALnE0': 'file_storage/call_OunRzvNknYcQgGThNXVALnE0.json'}

exec(code, env_args)
