code = """import json, pandas as pd
syms = json.load(open(var_call_ByUHgLwN173t1iWxDozlCoTI))
meta = pd.read_json(var_call_PUe6KdUev4CgynNT4bGypf6f)
nyse_syms = set(meta['Symbol'])
common = [s for s in syms if s in nyse_syms]
common = common[:100]
import duckdb
con = duckdb.connect(database='stocktrade_database', read_only=True)
rows = []
for sym in common:
    df = con.execute(f"SELECT Date, Open, Close FROM '{sym}' WHERE Date LIKE '2017-%'").fetchdf()
    if df.empty: continue
    up = (df['Close']>df['Open']).sum()
    down = (df['Close']<df['Open']).sum()
    if up>down:
        rows.append({'Symbol': sym, 'up': int(up), 'down': int(down)})
res = pd.DataFrame(rows).sort_values('up', ascending=False).head(5)
res = res.merge(meta[['Symbol','company']], on='Symbol', how='left')
answer = res['company'].tolist()
import json as j
out = j.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_ByUHgLwN173t1iWxDozlCoTI': 'file_storage/call_ByUHgLwN173t1iWxDozlCoTI.json', 'var_call_PUe6KdUev4CgynNT4bGypf6f': 'file_storage/call_PUe6KdUev4CgynNT4bGypf6f.json'}

exec(code, env_args)
