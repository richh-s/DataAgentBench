code = """import json, pandas as pd, duckdb, os

# Load ETF symbols from file
path = var_call_QzNtiNDUc0AuCoE7O5c82kWR
with open(path, 'r') as f:
    etf_records = json.load(f)

symbols = [r['Symbol'] for r in etf_records]

# Connect to DuckDB database
con = duckdb.connect(database='stocktrade_database', read_only=True)

qualifying = []
for sym in symbols:
    try:
        df = con.execute(f"SELECT \"Adj Close\" FROM '{sym}' WHERE strftime('%Y', Date) = '2015' AND \"Adj Close\" > 200 LIMIT 1;").fetchdf()
    except Exception:
        continue
    if not df.empty:
        qualifying.append(sym)

result = {"etf_symbols": qualifying, "count": len(qualifying)}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_QzNtiNDUc0AuCoE7O5c82kWR': 'file_storage/call_QzNtiNDUc0AuCoE7O5c82kWR.json', 'var_call_rOudpGJmet5Kebl3vKlGUbjt': 'file_storage/call_rOudpGJmet5Kebl3vKlGUbjt.json'}

exec(code, env_args)
