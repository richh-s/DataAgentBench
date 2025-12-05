code = """import json, duckdb, pandas as pd
from pathlib import Path

syms_path = var_call_tjnh6qXCN2sIBAGRMNxoSK2L
with open(syms_path) as f:
    syms = json.load(f)

con = duckdb.connect(database='stocktrade_database', read_only=True)

records = []
for row in syms:
    sym = row['Symbol']
    name = row['name']
    try:
        df = con.execute(f"SELECT Date, Open, Close FROM '{sym}' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31';").fetch_df()
    except Exception:
        continue
    if df.empty:
        continue
    up = (df['Close'] > df['Open']).sum()
    down = (df['Close'] < df['Open']).sum()
    if up > down:
        records.append({'Symbol': sym, 'name': name, 'up_days': int(up), 'down_days': int(down)})

records_sorted = sorted(records, key=lambda x: x['up_days'], reverse=True)[:5]
result = [r['name'] for r in records_sorted]

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_RANPJM7EJhzIakIlqKKKXIf5': 'file_storage/call_RANPJM7EJhzIakIlqKKKXIf5.json', 'var_call_tjnh6qXCN2sIBAGRMNxoSK2L': 'file_storage/call_tjnh6qXCN2sIBAGRMNxoSK2L.json'}

exec(code, env_args)
