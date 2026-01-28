code = """import json, pandas as pd

path_info = var_call_lsWEadc109kwWv5jdXkUgWbB
with open(path_info, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

path_tbl = var_call_VDn7pDm6A1YBRdsQaIjs0gEy
with open(path_tbl, 'r') as f:
    tbls = json.load(f)
tbls_set = set(tbls)

info_df = info_df[info_df['Symbol'].isin(tbls_set)].copy()
syms = info_df['Symbol'].tolist()

parts = []
for s in syms:
    parts.append("SELECT '"+s+"' AS Symbol, SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close<Open THEN 1 ELSE 0 END) AS down_days FROM \""+s+"\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'")

batch_size = 200
batches = [parts[i:i+batch_size] for i in range(0, len(parts), batch_size)]

print('__RESULT__:')
print(json.dumps({'n_symbols': len(syms), 'n_batches': len(batches)}))"""

env_args = {'var_call_lsWEadc109kwWv5jdXkUgWbB': 'file_storage/call_lsWEadc109kwWv5jdXkUgWbB.json', 'var_call_VDn7pDm6A1YBRdsQaIjs0gEy': 'file_storage/call_VDn7pDm6A1YBRdsQaIjs0gEy.json'}

exec(code, env_args)
