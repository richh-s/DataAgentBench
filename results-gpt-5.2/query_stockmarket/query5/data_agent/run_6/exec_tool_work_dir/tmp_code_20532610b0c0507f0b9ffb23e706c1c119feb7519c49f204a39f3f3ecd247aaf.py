code = """import json, pandas as pd

with open(var_call_1M2WJBSzBWCBsrqxUcSSQvFy, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

with open(var_call_6zdVBkckwn2R8JwOU8xeyNkR, 'r') as f:
    tbls = set(json.load(f))

info_df = info_df[info_df['Symbol'].isin(tbls)].copy()
syms = [s for s in info_df['Symbol'].tolist() if s.replace('_','').isalnum()]

parts = []
for s in syms:
    parts.append("SELECT '{sym}' AS Symbol, COUNT(*) AS cnt FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2".format(sym=s))

query = " UNION ALL ".join(parts)

print('__RESULT__:')
print(json.dumps({'n_parts': len(parts), 'query_len': len(query)}))"""

env_args = {'var_call_1M2WJBSzBWCBsrqxUcSSQvFy': 'file_storage/call_1M2WJBSzBWCBsrqxUcSSQvFy.json', 'var_call_6zdVBkckwn2R8JwOU8xeyNkR': 'file_storage/call_6zdVBkckwn2R8JwOU8xeyNkR.json', 'var_call_neNIOvU1Qz4tQrb5hXX8vBjb': 'file_storage/call_neNIOvU1Qz4tQrb5hXX8vBjb.json'}

exec(code, env_args)
