code = """import json, duckdb, pandas as pd
from pathlib import Path

symbols_file = Path(var_call_akrsxuPKWBL9A5GNgXjQ6PO2)
symbols = json.loads(symbols_file.read_text())
meta_file = Path(var_call_VqV5xzJAPIr6H9QsPQxB86Do)
meta = pd.read_json(meta_file)
meta = meta.set_index('Symbol')

con = duckdb.connect(database='stocktrade_database', read_only=True)

results = []
for sym in symbols:
    if sym not in meta.index: 
        continue
    try:
        df = con.execute(f"SELECT Date, Open, Close FROM '{sym}' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'").fetch_df()
    except Exception:
        continue
    if df.empty:
        continue
    up = (df['Close'] > df['Open']).sum()
    down = (df['Close'] < df['Open']).sum()
    if up > down:
        results.append({'Symbol': sym, 'up_days': int(up), 'down_days': int(down)})

res_df = pd.DataFrame(results)
res_df = res_df.sort_values('up_days', ascending=False).head(5)
res_df['name'] = res_df['Symbol'].map(meta['name'])

answer = res_df[['name']].to_dict(orient='records')

out = json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_akrsxuPKWBL9A5GNgXjQ6PO2': 'file_storage/call_akrsxuPKWBL9A5GNgXjQ6PO2.json', 'var_call_VqV5xzJAPIr6H9QsPQxB86Do': 'file_storage/call_VqV5xzJAPIr6H9QsPQxB86Do.json'}

exec(code, env_args)
