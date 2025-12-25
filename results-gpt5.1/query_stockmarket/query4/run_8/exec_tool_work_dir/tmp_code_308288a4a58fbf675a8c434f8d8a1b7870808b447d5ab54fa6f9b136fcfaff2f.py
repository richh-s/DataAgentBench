code = """import json, duckdb, pandas as pd
from pathlib import Path

symbols_info = json.load(open(var_call_PKQwMqCUCB2KHJNd4ftViaKY))
syms = [r['Symbol'] for r in symbols_info]

con = duckdb.connect(database='stocktrade_database', read_only=True)
results = []
for sym in syms:
    try:
        df = con.execute(f"SELECT Date, Open, Close FROM '{sym}' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'").fetchdf()
    except Exception:
        continue
    if df.empty:
        continue
    up = (df['Close'] > df['Open']).sum()
    down = (df['Close'] < df['Open']).sum()
    if up > down:
        results.append({'Symbol': sym, 'up_days': int(up), 'down_days': int(down)})

res_df = pd.DataFrame(results)
res_df['net_up'] = res_df['up_days'] - res_df['down_days']
res_df = res_df.sort_values(['net_up','up_days'], ascending=[False,False]).head(5)

name_map = {r['Symbol']: r['name'] for r in symbols_info}
res_df['name'] = res_df['Symbol'].map(name_map)

answer = res_df[['name']].to_dict(orient='records')

out = json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_cZnGQQLFbouV58FM5Fqycamm': 'file_storage/call_cZnGQQLFbouV58FM5Fqycamm.json', 'var_call_PKQwMqCUCB2KHJNd4ftViaKY': 'file_storage/call_PKQwMqCUCB2KHJNd4ftViaKY.json'}

exec(code, env_args)
