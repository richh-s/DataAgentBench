code = """import json, pandas as pd

raw = var_call_nRg4zi2zm0tDJpk3JAndwSRL
if isinstance(raw, str):
    nyse_recs = json.load(open(raw,'r'))
else:
    nyse_recs = raw
nyse_df = pd.DataFrame(nyse_recs)
nyse_syms = set(nyse_df['Symbol'].astype(str))

raw2 = var_call_2eLtZz9Xkk8ZzWBJcJg9PuVs
if isinstance(raw2, str):
    trade_tables = json.load(open(raw2,'r'))
else:
    trade_tables = raw2

candidates = sorted(nyse_syms.intersection(set(trade_tables)))

chunks = [candidates[i:i+200] for i in range(0, len(candidates), 200)]
queries = []
for ch in chunks:
    parts = []
    for sym in ch:
        q = (
            "SELECT '" + sym + "' AS Symbol, "
            "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
            "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
            "FROM \"" + sym + "\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
        )
        parts.append(q)
    queries.append(" UNION ALL ".join(parts))

out = {"candidate_count": len(candidates), "query_chunks": queries}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_nRg4zi2zm0tDJpk3JAndwSRL': 'file_storage/call_nRg4zi2zm0tDJpk3JAndwSRL.json', 'var_call_2eLtZz9Xkk8ZzWBJcJg9PuVs': 'file_storage/call_2eLtZz9Xkk8ZzWBJcJg9PuVs.json'}

exec(code, env_args)
