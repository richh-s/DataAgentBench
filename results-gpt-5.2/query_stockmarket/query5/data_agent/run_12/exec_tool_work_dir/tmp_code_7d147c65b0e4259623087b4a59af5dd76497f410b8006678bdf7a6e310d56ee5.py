code = """import json, pandas as pd
cap_path = var_call_0cRCwuXzy0ygPKXxZNGk722D
with open(cap_path,'r') as f:
    cap = json.load(f)
df = pd.DataFrame(cap)
syms = sorted(df['Symbol'].astype(str).unique().tolist())
# produce batched insert statements
batch_size = 400
stmts = []
for i in range(0, len(syms), batch_size):
    chunk = syms[i:i+batch_size]
    values = ",".join(["('" + s.replace("'","''") + "')" for s in chunk])
    stmts.append("INSERT INTO cap_syms VALUES " + values + ";")
print('__RESULT__:')
print(json.dumps({'n_syms': len(syms), 'stmts': stmts[:3], 'n_stmts': len(stmts)}))"""

env_args = {'var_call_0cRCwuXzy0ygPKXxZNGk722D': 'file_storage/call_0cRCwuXzy0ygPKXxZNGk722D.json', 'var_call_QmgXm74iO39N022IImWIvqGm': 'file_storage/call_QmgXm74iO39N022IImWIvqGm.json', 'var_call_zTLM20Bmr7M3fKcKo1DvPtSn': [{'n': '2753'}], 'var_call_h51wwCkiysxkDmLSM3Cf4KkN': 'ok', 'var_call_gU1inhWjtJB83dKl1Uyc4NpZ': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_g3aJ41FzlR1ToEDcKF29GHzL': []}

exec(code, env_args)
