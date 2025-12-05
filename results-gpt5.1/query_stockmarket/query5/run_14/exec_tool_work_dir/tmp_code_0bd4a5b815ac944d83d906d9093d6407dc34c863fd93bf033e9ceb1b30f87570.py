code = """import json, pandas as pd
from pathlib import Path

symbols_file = var_call_PJl2gfe4K15X7PNhmtrbDtrW
symbols = pd.read_json(symbols_file)

results = []

import duckdb
con = duckdb.connect(database='stocktrade_database', read_only=True)

for sym in symbols['Symbol']:
    try:
        df = con.execute(f"SELECT Date, High, Low FROM '{sym}' WHERE Date >= '2019-01-01' AND Date <= '2019-12-31';").df()
    except Exception:
        continue
    if df.empty:
        continue
    df['range_ratio'] = (df['High'] - df['Low']) / df['Low']
    count = int((df['range_ratio'] > 0.20).sum())
    if count > 0:
        results.append({'Symbol': sym, 'days_over_20pct': count})

res_df = pd.DataFrame(results)
if not res_df.empty:
    top5 = res_df.sort_values('days_over_20pct', ascending=False).head(5)
    merged = top5.merge(symbols, on='Symbol', how='left')
    out = merged[['Symbol', 'Company Description', 'days_over_20pct']].to_dict(orient='records')
else:
    out = []

result_json = json.dumps(out)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_9rLzvbwozttVBtJtJ9W93vfs': 'file_storage/call_9rLzvbwozttVBtJtJ9W93vfs.json', 'var_call_PJl2gfe4K15X7PNhmtrbDtrW': 'file_storage/call_PJl2gfe4K15X7PNhmtrbDtrW.json'}

exec(code, env_args)
