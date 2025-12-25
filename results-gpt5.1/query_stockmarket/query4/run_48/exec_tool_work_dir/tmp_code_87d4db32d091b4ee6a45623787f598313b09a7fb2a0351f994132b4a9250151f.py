code = """import json
import duckdb

# load table list from file
with open(var_call_T5jIPdjNlVy0w0k2SitLfVjU, 'r') as f:
    symbols = json.load(f)

# load NYSE non-ETF symbols
with open(var_call_axrP0Ui27kUG8U9GzzBChKqA, 'r') as f:
    nyse_meta = json.load(f)
nyse_symbols = {row['Symbol']: row['name'] for row in nyse_meta}

con = duckdb.connect(database='stocktrade_database', read_only=True)

results = []
for sym in symbols:
    if sym not in nyse_symbols:
        continue
    try:
        q = f"SELECT SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM '{sym}' WHERE strftime('%Y', Date) = '2017';"
        up, down = con.execute(q).fetchone()
    except Exception:
        continue
    if up is None or down is None:
        continue
    if up > down:
        results.append((sym, nyse_symbols[sym], int(up), int(down)))

# sort by difference up_days - down_days descending
results.sort(key=lambda x: (x[2]-x[3], x[2]), reverse=True)

top5 = [r[1] for r in results[:5]]

out = json.dumps(top5)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_T5jIPdjNlVy0w0k2SitLfVjU': 'file_storage/call_T5jIPdjNlVy0w0k2SitLfVjU.json', 'var_call_axrP0Ui27kUG8U9GzzBChKqA': 'file_storage/call_axrP0Ui27kUG8U9GzzBChKqA.json'}

exec(code, env_args)
