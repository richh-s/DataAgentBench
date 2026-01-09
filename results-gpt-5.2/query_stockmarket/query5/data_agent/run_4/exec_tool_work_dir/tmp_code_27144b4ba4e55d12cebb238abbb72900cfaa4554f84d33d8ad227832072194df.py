code = """import json, pandas as pd

cap_path = var_call_ZOv1HX3wecOlh9OtBRKoVhew
with open(cap_path,'r') as f:
    cap = json.load(f)
df_cap = pd.DataFrame(cap)

# Take only symbols that are valid duckdb identifiers (letters/numbers)
df_cap = df_cap[df_cap['Symbol'].str.match(r'^[A-Z0-9]+$')]

# get trade tables list
with open(var_call_4NDKOmo1WXnwcECZ5AGvHHrf,'r') as f:
    tbls = set(json.load(f))

df_cap = df_cap[df_cap['Symbol'].isin(tbls)].copy()
syms = df_cap['Symbol'].unique().tolist()

parts = []
for s in syms:
    parts.append(f"SELECT '{s}' AS Symbol, COUNT(*) AS days_exceed_20pct FROM \"{s}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low > 0 AND (High - Low) / Low > 0.20")

final_q = "SELECT Symbol, days_exceed_20pct FROM (\n" + "\nUNION ALL\n".join(parts) + "\n) ORDER BY days_exceed_20pct DESC, Symbol ASC LIMIT 5"

print('__RESULT__:')
print(json.dumps({'final_query': final_q, 'n': len(parts)}))"""

env_args = {'var_call_ZOv1HX3wecOlh9OtBRKoVhew': 'file_storage/call_ZOv1HX3wecOlh9OtBRKoVhew.json', 'var_call_4NDKOmo1WXnwcECZ5AGvHHrf': 'file_storage/call_4NDKOmo1WXnwcECZ5AGvHHrf.json', 'var_call_649CkIaYwKfsQvEpFsYHeFNv': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'AAME'}, {'Symbol': 'AAWW'}, {'Symbol': 'AAXJ'}], 'var_call_76z57fb4vzRnHtBkDH8kLV4b': 'file_storage/call_76z57fb4vzRnHtBkDH8kLV4b.json', 'var_call_PKZc7WCFjASdkq6BlvzSLcrM': [{'1': '1'}]}

exec(code, env_args)
