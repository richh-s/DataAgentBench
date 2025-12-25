code = """import json
import duckdb

# Load symbols list file path from storage
symbols = var_call_imHpQLK8GtzBoRC61f6UZlB0

with open(symbols, 'r') as f:
    tickers = json.load(f)

# Load NYSE non-ETF symbols with names
info_path = var_call_eZCQirylvhqCj09Gt92OArMj
with open(info_path, 'r') as f:
    info = json.load(f)

nyse_symbols = {row['Symbol']: row['CompanyName'] for row in info}

con = duckdb.connect(database='stocktrade_database', read_only=True)

results = []
for sym in tickers:
    if sym not in nyse_symbols:
        continue
    try:
        df = con.execute(f"SELECT Date, Open, Close FROM '{sym}' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'").fetch_df()
    except Exception:
        continue
    if df.empty:
        continue
    up = (df['Close'] > df['Open']).sum()
    down = (df['Close'] < df['Open']).sum()
    total = up + down
    if total == 0:
        continue
    if up > down:
        results.append({'Symbol': sym, 'UpDays': int(up), 'DownDays': int(down), 'TotalDays': int(total)})

# sort by difference up-down desc, then by total days desc as tie-breaker
results_sorted = sorted(results, key=lambda x: (x['UpDays'] - x['DownDays'], x['TotalDays']), reverse=True)[:5]

# map to company names
output = []
for r in results_sorted:
    output.append({'Symbol': r['Symbol'], 'CompanyName': nyse_symbols.get(r['Symbol'], '')})

res_json = json.dumps(output)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_imHpQLK8GtzBoRC61f6UZlB0': 'file_storage/call_imHpQLK8GtzBoRC61f6UZlB0.json', 'var_call_eZCQirylvhqCj09Gt92OArMj': 'file_storage/call_eZCQirylvhqCj09Gt92OArMj.json'}

exec(code, env_args)
