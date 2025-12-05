code = """import json
import duckdb

# Load symbol-name mapping from SQLite result
with open(var_call_OCF6KyOdjwOfeLCSLZGC40e0, 'r') as f:
    nyse_meta = json.load(f)

symbol_to_name = {row['Symbol']: row['name'] for row in nyse_meta}

# Connect to DuckDB database
con = duckdb.connect('stocktrade_database')

# We will iterate over all tables, compute 2017 up/down counts, filter to NYSE non-ETF symbols
all_tables = json.load(open(var_call_E0OapJ00GdMNOr0NDE5Ycfpj, 'r'))

records = []
for sym in all_tables:
    if sym not in symbol_to_name:
        continue
    try:
        df = con.execute(f"SELECT Date, Open, Close FROM '{sym}' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'").fetchdf()
    except Exception:
        continue
    if df.empty:
        continue
    up_days = (df['Close'] > df['Open']).sum()
    down_days = (df['Close'] < df['Open']).sum()
    total_days = len(df)
    if up_days > down_days:
        frac_up = up_days / total_days
        records.append((sym, symbol_to_name[sym], up_days, down_days, frac_up))

# Sort by fraction of up days descending, then by up_days desc
records.sort(key=lambda x: (-x[4], -x[2]))

top5 = records[:5]

result = [name for _, name, _, _, _ in top5]

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_E0OapJ00GdMNOr0NDE5Ycfpj': 'file_storage/call_E0OapJ00GdMNOr0NDE5Ycfpj.json', 'var_call_OCF6KyOdjwOfeLCSLZGC40e0': 'file_storage/call_OCF6KyOdjwOfeLCSLZGC40e0.json'}

exec(code, env_args)
