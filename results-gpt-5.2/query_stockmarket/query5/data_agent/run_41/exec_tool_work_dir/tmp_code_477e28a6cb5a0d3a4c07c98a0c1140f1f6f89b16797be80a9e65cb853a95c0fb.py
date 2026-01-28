code = """import json, pandas as pd

obj = var_call_8z0hOoCRDAGDWUY6KxgLogHY
if isinstance(obj, str):
    with open(obj, 'r') as f:
        symbols = json.load(f)
else:
    symbols = obj

df = pd.DataFrame(symbols)
tickers = sorted(df['Symbol'].dropna().unique().tolist())

parts = []
for t in tickers:
    safe_t = t.replace('"','""')
    q = (
        f"SELECT '{safe_t}' AS Symbol, COUNT(*)::BIGINT AS days_exceeded "
        f"FROM \"{safe_t}\" "
        f"WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' "
        f"AND Low > 0 AND (High - Low) / Low > 0.2"
    )
    parts.append(q)

query = "\nUNION ALL\n".join(parts) + "\nORDER BY days_exceeded DESC, Symbol ASC\nLIMIT 50;"

print('__RESULT__:')
print(json.dumps({'query': query, 'n_tickers': len(tickers)}))"""

env_args = {'var_call_8z0hOoCRDAGDWUY6KxgLogHY': 'file_storage/call_8z0hOoCRDAGDWUY6KxgLogHY.json'}

exec(code, env_args)
