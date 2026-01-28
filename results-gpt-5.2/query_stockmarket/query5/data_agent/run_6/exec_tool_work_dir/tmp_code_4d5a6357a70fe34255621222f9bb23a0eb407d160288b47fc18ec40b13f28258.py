code = """import json, pandas as pd

# load stockinfo
with open(var_call_1M2WJBSzBWCBsrqxUcSSQvFy, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

with open(var_call_6zdVBkckwn2R8JwOU8xeyNkR, 'r') as f:
    tbls = set(json.load(f))

info_df = info_df[info_df['Symbol'].isin(tbls)].copy()
# keep only symbols that are safe unquoted identifiers and not SQL keywords likely (we'll quote anyway)
syms = [s for s in info_df['Symbol'].tolist() if s.replace('_','').isalnum()]

# build query quoting identifiers with double quotes
parts=[]
for s in syms:
    parts.append(f"SELECT '{s}' AS Symbol, COUNT(*) AS cnt FROM \"{s}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2")
query = " UNION ALL ".join(parts)
print('__RESULT__:')
print(json.dumps({'n': len(parts), 'query': query[:1000]}))"""

env_args = {'var_call_1M2WJBSzBWCBsrqxUcSSQvFy': 'file_storage/call_1M2WJBSzBWCBsrqxUcSSQvFy.json', 'var_call_6zdVBkckwn2R8JwOU8xeyNkR': 'file_storage/call_6zdVBkckwn2R8JwOU8xeyNkR.json', 'var_call_neNIOvU1Qz4tQrb5hXX8vBjb': 'file_storage/call_neNIOvU1Qz4tQrb5hXX8vBjb.json'}

exec(code, env_args)
