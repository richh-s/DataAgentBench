code = """import json, duckdb, os

symbols_path = var_call_3rYrCjSAv58HX0d6nJNxh182
with open(symbols_path, 'r') as f:
    all_symbols = json.load(f)

info_path = var_call_AVYJebWhXSHh7D3JOkyerKfC
with open(info_path, 'r') as f:
    info_records = json.load(f)

info_map = {r['Symbol']: r['name'] for r in info_records}

con = duckdb.connect(database='stocktrade_database', read_only=True)

results = []
for sym in all_symbols:
    if sym not in info_map:
        continue
    try:
        df = con.execute(f"SELECT Date, Open, Close FROM '{sym}' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31';").fetch_df()
    except Exception:
        continue
    if df.empty:
        continue
    up = (df['Close'] > df['Open']).sum()
    down = (df['Close'] < df['Open']).sum()
    if up > down:
        results.append((sym, info_map[sym], up, down))

results.sort(key=lambda x: (-(x[2]-x[3]), -x[2]))

top5 = [r[1] for r in results[:5]]

import json as _json
res_json = _json.dumps(top5)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_3rYrCjSAv58HX0d6nJNxh182': 'file_storage/call_3rYrCjSAv58HX0d6nJNxh182.json', 'var_call_AVYJebWhXSHh7D3JOkyerKfC': 'file_storage/call_AVYJebWhXSHh7D3JOkyerKfC.json'}

exec(code, env_args)
