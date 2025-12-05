code = """import json, pandas as pd, os

path = var_call_KDs6joxRY1vKE4nX2hNlQyDo
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Determine up and down days per index
summary = df.groupby('Index').apply(lambda g: pd.Series({
    'up_days': (g['Close']>g['Open']).sum(),
    'down_days': (g['Close']<g['Open']).sum()
})).reset_index()

# North American indices in this dataset: US (IXIC, NYA, GSPC?) and Canada (GSPTSE)
na_indices = ['IXIC','NYA','GSPTSE']
summary_na = summary[summary['Index'].isin(na_indices)].copy()
summary_na['more_up_than_down'] = summary_na['up_days'] > summary_na['down_days']

result = summary_na.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_9VZQSkzMXskfuaYVqXOQJGfe': ['index_info'], 'var_call_aO4zEUGDvy0pD4kst0H4yBTL': ['index_trade'], 'var_call_wfzXPqS55fGKXgSDtsFfaXqe': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_KDs6joxRY1vKE4nX2hNlQyDo': 'file_storage/call_KDs6joxRY1vKE4nX2hNlQyDo.json'}

exec(code, env_args)
