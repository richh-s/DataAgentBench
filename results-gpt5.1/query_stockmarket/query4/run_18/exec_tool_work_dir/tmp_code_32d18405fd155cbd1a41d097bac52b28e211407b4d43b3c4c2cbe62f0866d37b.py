code = """import json, duckdb, pandas as pd
from pathlib import Path

symbols_path = var_call_8bJSvFhGu1tNek99RyhTedLE
with open(symbols_path) as f:
    nyse_records = json.load(f)

nyse_symbols = [r['Symbol'] for r in nyse_records]

con = duckdb.connect(database='stocktrade_database', read_only=True)

results = []
for sym in nyse_symbols:
    try:
        df = con.execute(f"SELECT Date, Open, Close FROM '{sym}' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'").df()
    except Exception:
        continue
    if df.empty:
        continue
    up_days = (df['Close'] > df['Open']).sum()
    down_days = (df['Close'] < df['Open']).sum()
    if up_days > down_days:
        results.append({'Symbol': sym, 'up_days': int(up_days), 'down_days': int(down_days)})

res_df = pd.DataFrame(results)
res_df = res_df.sort_values('up_days', ascending=False).head(5)

name_map = {r['Symbol']: r['Company Description'] for r in nyse_records}
res_df['Company Description'] = res_df['Symbol'].map(name_map)

final = res_df[['Company Description']].to_dict(orient='records')

out = json.dumps(final)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_UCs7a231KgOSZ7hIMbh4DCh0': 'file_storage/call_UCs7a231KgOSZ7hIMbh4DCh0.json', 'var_call_8bJSvFhGu1tNek99RyhTedLE': 'file_storage/call_8bJSvFhGu1tNek99RyhTedLE.json'}

exec(code, env_args)
