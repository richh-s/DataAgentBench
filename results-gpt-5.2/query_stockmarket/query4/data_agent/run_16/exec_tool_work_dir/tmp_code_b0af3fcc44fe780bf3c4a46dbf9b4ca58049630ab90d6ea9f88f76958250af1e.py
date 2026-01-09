code = """import json, pandas as pd

with open(var_call_sPuptWK6vPMIEukyP6PhzyEY, 'r') as f:
    info = json.load(f)
with open(var_call_h1WcvUzmUip7YwjHzrIxBE7I, 'r') as f:
    tables = json.load(f)

info_df = pd.DataFrame(info)
info_df['Symbol'] = info_df['Symbol'].astype(str)

tables_set = set(map(str, tables))
info_df = info_df[info_df['Symbol'].isin(tables_set)].copy()

symbols = info_df['Symbol'].tolist()
chunks = [symbols[i:i+60] for i in range(0, len(symbols), 60)]
queries = []
for chunk in chunks:
    parts = []
    for sym in chunk:
        sql = (
            "SELECT '" + sym + "' AS Symbol, "
            "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
            "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
            "FROM \"" + sym + "\" "
            "WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
        )
        parts.append(sql)
    queries.append(" UNION ALL ".join(parts))

print('__RESULT__:')
print(json.dumps({'queries': queries, 'n_symbols': len(symbols), 'n_chunks': len(chunks)}))"""

env_args = {'var_call_sPuptWK6vPMIEukyP6PhzyEY': 'file_storage/call_sPuptWK6vPMIEukyP6PhzyEY.json', 'var_call_h1WcvUzmUip7YwjHzrIxBE7I': 'file_storage/call_h1WcvUzmUip7YwjHzrIxBE7I.json'}

exec(code, env_args)
