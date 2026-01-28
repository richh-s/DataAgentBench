code = """import json, pandas as pd

# Load capital market symbols
cap_path = var_call_ZOv1HX3wecOlh9OtBRKoVhew
with open(cap_path, 'r') as f:
    cap = json.load(f)
df_cap = pd.DataFrame(cap)
cap_syms = set(df_cap['Symbol'].astype(str))

# Load available trade tables
tbl_path = var_call_4NDKOmo1WXnwcECZ5AGvHHrf
with open(tbl_path, 'r') as f:
    tbls = json.load(f)
trade_syms = set(tbls)

syms = sorted(list(cap_syms & trade_syms))

# Build UNION ALL query across symbols to count qualifying days in 2019
parts = []
for s in syms:
    # DuckDB table names may need quoting if special chars; assume standard tickers A-Z0-9.
    parts.append(
        f"SELECT '{s}' AS Symbol, COUNT(*) AS days_exceed_20pct "
        f"FROM \"{s}\" "
        f"WHERE Date >= '2019-01-01' AND Date < '2020-01-01' "
        f"  AND Low > 0 "
        f"  AND (High - Low) / Low > 0.20"
    )

query = "\nUNION ALL\n".join(parts)
query = f"SELECT Symbol, days_exceed_20pct FROM (\n{query}\n) ORDER BY days_exceed_20pct DESC, Symbol ASC LIMIT 5;"

print('__RESULT__:')
print(json.dumps({'symbols': syms, 'query': query}))"""

env_args = {'var_call_ZOv1HX3wecOlh9OtBRKoVhew': 'file_storage/call_ZOv1HX3wecOlh9OtBRKoVhew.json', 'var_call_4NDKOmo1WXnwcECZ5AGvHHrf': 'file_storage/call_4NDKOmo1WXnwcECZ5AGvHHrf.json'}

exec(code, env_args)
