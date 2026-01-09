code = """import json, pandas as pd

path_info = var_call_x1jXusftMO2wxSRYRNEpSjmA
with open(path_info, 'r') as f:
    info = json.load(f)
df_info = pd.DataFrame(info)

path_tbl = var_call_MsWxQiKnjVzbXQOwPnsP05OQ
with open(path_tbl, 'r') as f:
    tbls = json.load(f)
set_tbls = set(tbls)

symbols = sorted(set(df_info['symbol']).intersection(set_tbls))
chunks = [symbols[i:i+200] for i in range(0, len(symbols), 200)]

queries = []
for ch in chunks:
    parts = []
    for sym in ch:
        q = (
            "SELECT '" + sym + "' AS symbol, "
            "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
            "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
            "FROM \"" + sym + "\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
        )
        parts.append(q)
    queries.append(' UNION ALL '.join(parts))

print('__RESULT__:')
print(json.dumps({'n_symbols': len(symbols), 'n_queries': len(queries), 'queries': queries[:3]}))"""

env_args = {'var_call_x1jXusftMO2wxSRYRNEpSjmA': 'file_storage/call_x1jXusftMO2wxSRYRNEpSjmA.json', 'var_call_MsWxQiKnjVzbXQOwPnsP05OQ': 'file_storage/call_MsWxQiKnjVzbXQOwPnsP05OQ.json'}

exec(code, env_args)
