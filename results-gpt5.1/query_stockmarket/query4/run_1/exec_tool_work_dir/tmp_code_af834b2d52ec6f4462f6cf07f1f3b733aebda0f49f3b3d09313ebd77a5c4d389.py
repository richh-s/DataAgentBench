code = """import json, duckdb, pandas as pd
from pathlib import Path

symbols_path = var_call_KsO9bamDlYJkIJWBk1HReH2w
with open(symbols_path) as f:
    all_symbols = json.load(f)

info_path = var_call_vWJWKOsRDvMLn4I86nC9W4US
with open(info_path) as f:
    info = json.load(f)

nyse_non_etf = {row['Symbol']: row['name'] for row in info if row['Symbol'] in all_symbols}

con = duckdb.connect(database='stocktrade_database', read_only=True)

results = []
for sym in nyse_non_etf.keys():
    try:
        df = con.execute(f"SELECT Date, Open, Close FROM '{sym}' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'").df()
    except Exception:
        continue
    if df.empty:
        continue
    up = (df['Close'] > df['Open']).sum()
    down = (df['Close'] < df['Open']).sum()
    if up > down:
        results.append({'Symbol': sym, 'up_days': int(up), 'down_days': int(down)})

res_df = pd.DataFrame(results)
res_df.sort_values(['up_days','down_days'], ascending=[False,True], inplace=True)
Top5 = res_df.head(5)
Top5['name'] = Top5['Symbol'].map(nyse_non_etf)

answer = Top5[['name']].to_dict(orient='list')['name']

out = json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_KsO9bamDlYJkIJWBk1HReH2w': 'file_storage/call_KsO9bamDlYJkIJWBk1HReH2w.json', 'var_call_vWJWKOsRDvMLn4I86nC9W4US': 'file_storage/call_vWJWKOsRDvMLn4I86nC9W4US.json'}

exec(code, env_args)
