code = """import json, pandas as pd, os
path = var_call_sFrxBFxzwpmFA1NgF6lqDuWf
with open(path, 'r') as f:
    data = json.load(f)
rows = []
for r in data:
    idx = r['Index']
    o = float(r['Open'])
    c = float(r['Close'])
    if c>o:
        ud='up'
    elif c<o:
        ud='down'
    else:
        ud='flat'
    rows.append({'Index':idx,'ud':ud})
df = pd.DataFrame(rows)
summary = df.groupby('Index')['ud'].value_counts().unstack(fill_value=0)
res = {}
for idx, row in summary.iterrows():
    up = row.get('up',0)
    down = row.get('down',0)
    if up>down:
        res[idx] = {'up_days':int(up),'down_days':int(down)}
result = json.dumps(res)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_z5EIA4u02szAdW3qzIpV3a9Q': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}], 'var_call_SHRf6vRD080k2r7Vo9gTzxTy': ['GSPTSE', 'IXIC', 'NYA'], 'var_call_sFrxBFxzwpmFA1NgF6lqDuWf': 'file_storage/call_sFrxBFxzwpmFA1NgF6lqDuWf.json'}

exec(code, env_args)
