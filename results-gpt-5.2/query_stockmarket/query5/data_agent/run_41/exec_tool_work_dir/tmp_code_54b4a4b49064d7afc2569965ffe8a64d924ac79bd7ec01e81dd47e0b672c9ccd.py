code = """import json, pandas as pd

# load symbols/company list
obj = var_call_8z0hOoCRDAGDWUY6KxgLogHY
if isinstance(obj, str):
    with open(obj, 'r') as f:
        symbols = json.load(f)
else:
    symbols = obj

df = pd.DataFrame(symbols)
tickers = sorted(df['Symbol'].dropna().unique().tolist())

# build a duckdb query that unions per-ticker counts for 2019 where (High-Low)/Low > 0.2
# guard Low > 0 to avoid division by zero
parts = []
for t in tickers:
    safe_t = t.replace('"','""')
    parts.append(
        f"SELECT '{safe_t}' AS Symbol, COUNT(*)::BIGINT AS days_exceeded "
        f"FROM \"{safe_t}\" "
        f"WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2"
    )

# chunk to avoid huge SQL strings? we'll just create full; if too large, it may error.
query = "\nUNION ALL\n".join(parts) + "\nORDER BY days_exceeded DESC, Symbol ASC\nLIMIT 50;"

print('__RESULT__:')
print(json.dumps({'query': query, 'n_tickers': len(tickers)}))"""

env_args = {'var_call_8z0hOoCRDAGDWUY6KxgLogHY': 'file_storage/call_8z0hOoCRDAGDWUY6KxgLogHY.json'}

exec(code, env_args)
