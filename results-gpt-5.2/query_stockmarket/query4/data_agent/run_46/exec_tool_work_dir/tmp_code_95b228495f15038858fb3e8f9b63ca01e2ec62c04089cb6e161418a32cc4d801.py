code = """import json, pandas as pd

raw = var_call_nRg4zi2zm0tDJpk3JAndwSRL
nyse_recs = json.load(open(raw,'r')) if isinstance(raw,str) else raw
nyse_df = pd.DataFrame(nyse_recs)

raw2 = var_call_2eLtZz9Xkk8ZzWBJcJg9PuVs
trade_tables = json.load(open(raw2,'r')) if isinstance(raw2,str) else raw2

candidates = sorted(set(nyse_df['Symbol'].astype(str)).intersection(set(trade_tables)))

chunks = [candidates[i:i+200] for i in range(0, len(candidates), 200)]
queries = []
for ch in chunks:
    parts=[]
    for sym in ch:
        parts.append(
            "SELECT '"+sym+"' AS Symbol, "
            "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
            "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
            "FROM \""+sym+"\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
        )
    queries.append(" UNION ALL ".join(parts))

print('__RESULT__:')
print(json.dumps({'candidate_count': len(candidates), 'query_chunks': queries}))"""

env_args = {'var_call_nRg4zi2zm0tDJpk3JAndwSRL': 'file_storage/call_nRg4zi2zm0tDJpk3JAndwSRL.json', 'var_call_2eLtZz9Xkk8ZzWBJcJg9PuVs': 'file_storage/call_2eLtZz9Xkk8ZzWBJcJg9PuVs.json', 'var_call_O4764Qvq9h4CJVB5HUWDbnZv': 'file_storage/call_O4764Qvq9h4CJVB5HUWDbnZv.json'}

exec(code, env_args)
