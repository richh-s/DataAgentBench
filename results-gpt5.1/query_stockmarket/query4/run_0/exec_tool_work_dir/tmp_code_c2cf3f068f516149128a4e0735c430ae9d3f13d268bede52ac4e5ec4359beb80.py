code = """import json, duckdb, sqlite3, pandas as pd
from pathlib import Path

symbols = [r["Symbol"] for r in json.load(open(var_call_A7Wo4XT5t14kdVtHrsAmHWaH))]

con = duckdb.connect(database='stocktrade_database', read_only=True)

results = []
for sym in symbols:
    try:
        df = con.execute(f"SELECT Date, Open, Close FROM '{sym}' WHERE Date LIKE '2017-%';").df()
    except Exception:
        continue
    if df.empty:
        continue
    up = (df['Close'] > df['Open']).sum()
    down = (df['Close'] < df['Open']).sum()
    if up > down:
        results.append((sym, up, down))

results.sort(key=lambda x: (x[1]-x[2]), reverse=True)

top5_symbols = [s for s,_,_ in results[:5]]

info = {r["Symbol"]: r["Company Description"] for r in json.load(open(var_call_A7Wo4XT5t14kdVtHrsAmHWaH)) if r["Symbol"] in top5_symbols}

answer = [info[s] for s in top5_symbols]

out = json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_7YSjVDkGdCDYGU3qfmgScG8k': 'file_storage/call_7YSjVDkGdCDYGU3qfmgScG8k.json', 'var_call_A7Wo4XT5t14kdVtHrsAmHWaH': 'file_storage/call_A7Wo4XT5t14kdVtHrsAmHWaH.json'}

exec(code, env_args)
