code = """import json, duckdb, sqlite3, pandas as pd

# Load NYSE non-ETF symbols list from stockinfo_database result file
path = var_call_2tXRnltR0C4ryGrPbnV5Vdw3
rows = json.load(open(path))
nyse_symbols = [r['Symbol'] for r in rows]

# Connect to DuckDB file behind logical DB (assumed path)
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

# Now filter out ETFs by joining back to rows
meta = {r['Symbol']: r['Company Description'] for r in rows}

# Sort by difference between up and down days, descending, then by up_days desc
results_sorted = sorted(results, key=lambda x: (x['up_days']-x['down_days'], x['up_days']), reverse=True)

# Take top 5 and map to company names (use Company Description as name proxy)
top5 = []
for r in results_sorted[:5]:
    desc = meta.get(r['Symbol'], '')
    name = desc.split(' is ')[0].split(' specializes')[0].split(' operates')[0].split(' provides')[0]
    top5.append({'Symbol': r['Symbol'], 'Name': name, 'up_days': r['up_days'], 'down_days': r['down_days']})

out = json.dumps(top5)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_d6lExvPvRkqHu3VTCimig2lt': 'file_storage/call_d6lExvPvRkqHu3VTCimig2lt.json', 'var_call_2tXRnltR0C4ryGrPbnV5Vdw3': 'file_storage/call_2tXRnltR0C4ryGrPbnV5Vdw3.json'}

exec(code, env_args)
