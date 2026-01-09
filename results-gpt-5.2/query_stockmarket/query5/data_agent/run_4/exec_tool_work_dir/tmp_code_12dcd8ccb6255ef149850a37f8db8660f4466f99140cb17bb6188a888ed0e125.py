code = """import json, pandas as pd

cap_path = var_call_ZOv1HX3wecOlh9OtBRKoVhew
with open(cap_path, 'r') as f:
    cap = json.load(f)
df_cap = pd.DataFrame(cap)
cap_syms = set(df_cap['Symbol'].astype(str))

tbl_path = var_call_4NDKOmo1WXnwcECZ5AGvHHrf
with open(tbl_path, 'r') as f:
    tbls = json.load(f)
trade_syms = set(tbls)

syms = sorted(list(cap_syms & trade_syms))

parts = []
for s in syms:
    parts.append(
        "SELECT '{s}' AS Symbol, COUNT(*) AS days_exceed_20pct "
        "FROM \"{s}\" "
        "WHERE Date >= '2019-01-01' AND Date < '2020-01-01' "
        "  AND Low > 0 "
        "  AND (High - Low) / Low > 0.20".format(s=s)
    )

union_q = "\nUNION ALL\n".join(parts)
final_q = "SELECT Symbol, days_exceed_20pct FROM (\n{u}\n) ORDER BY days_exceed_20pct DESC, Symbol ASC LIMIT 5;".format(u=union_q)

print('__RESULT__:')
print(json.dumps({'final_query': final_q, 'n_symbols': len(syms)}))"""

env_args = {'var_call_ZOv1HX3wecOlh9OtBRKoVhew': 'file_storage/call_ZOv1HX3wecOlh9OtBRKoVhew.json', 'var_call_4NDKOmo1WXnwcECZ5AGvHHrf': 'file_storage/call_4NDKOmo1WXnwcECZ5AGvHHrf.json'}

exec(code, env_args)
