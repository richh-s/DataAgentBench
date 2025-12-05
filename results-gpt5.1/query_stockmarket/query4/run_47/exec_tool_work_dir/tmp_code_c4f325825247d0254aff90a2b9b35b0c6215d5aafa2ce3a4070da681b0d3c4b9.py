code = """import json, duckdb, os

# Load stock symbols from file
path = var_call_IynisZvqASrOgHHfw8h001XA
with open(path, 'r') as f:
    symbols = json.load(f)

# Load NYSE non-ETF, non-test symbols
path2 = var_call_cnRbf7z3OcI7tjE8iNHwelcy
with open(path2, 'r') as f:
    nyse_meta = json.load(f)
nyse_symbols = {row['Symbol']: row['Company Description'] for row in nyse_meta}

con = duckdb.connect(database='stocktrade_database', read_only=True)

results = []
for sym in symbols:
    if sym not in nyse_symbols:
        continue
    try:
        df = con.execute(f"SELECT Date, Open, Close FROM '{sym}' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31';").fetchdf()
    except Exception:
        continue
    if df.empty:
        continue
    up = (df['Close'] > df['Open']).sum()
    down = (df['Close'] < df['Open']).sum()
    if up > down:
        results.append({'Symbol': sym, 'Company Description': nyse_symbols[sym], 'up_days': int(up), 'down_days': int(down)})

results_sorted = sorted(results, key=lambda x: x['up_days']-x['down_days'], reverse=True)[:5]

answer = [r['Company Description'] for r in results_sorted]

import json as _json
res_json = _json.dumps(answer)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_IynisZvqASrOgHHfw8h001XA': 'file_storage/call_IynisZvqASrOgHHfw8h001XA.json', 'var_call_cnRbf7z3OcI7tjE8iNHwelcy': 'file_storage/call_cnRbf7z3OcI7tjE8iNHwelcy.json'}

exec(code, env_args)
