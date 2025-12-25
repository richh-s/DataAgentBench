code = """import json, sqlite3, duckdb, pandas as pd, os
from datetime import datetime

path = var_call_ETD8LRq2IyIVE8RkiQWVx2h0
with open(path, 'r') as f:
    stockinfo = json.load(f)

symbols = [r['Symbol'] for r in stockinfo]

con = duckdb.connect(database='stocktrade_database', read_only=True)

rows = []
for sym in symbols:
    try:
        df = con.execute(f"SELECT Date, High, Low FROM '{sym}' WHERE Date >= '2019-01-01' AND Date <= '2019-12-31';").fetchdf()
    except Exception:
        continue
    if df.empty:
        continue
    df['Low_nonzero'] = df['Low'].replace(0, pd.NA)
    cond = (df['High'] - df['Low']) > 0.2 * df['Low_nonzero']
    count = int(cond.fillna(False).sum())
    if count > 0:
        rows.append({'Symbol': sym, 'Days': count})

res_df = pd.DataFrame(rows)
if not res_df.empty:
    top5 = res_df.sort_values('Days', ascending=False).head(5)
    sym_top = top5['Symbol'].tolist()
else:
    sym_top = []

name_map = {r['Symbol']: r['CompanyDescription'] for r in stockinfo}

def extract_name(desc):
    if not desc:
        return None
    parts = desc.split(' specializes')[0].split(' is ')[0].split(' operates')[0].split(' provides')[0]
    return parts.strip().rstrip('.')

companies = [extract_name(name_map.get(s)) for s in sym_top]

result = companies

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ldnGsTLXJb5HSWW6RQ0FCm6O': 'file_storage/call_ldnGsTLXJb5HSWW6RQ0FCm6O.json', 'var_call_ETD8LRq2IyIVE8RkiQWVx2h0': 'file_storage/call_ETD8LRq2IyIVE8RkiQWVx2h0.json', 'var_call_dcOkgZDTejAlrd7wgwFAzuoN': [{'1': '1'}]}

exec(code, env_args)
