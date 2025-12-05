code = """import json, pandas as pd

# Load ETF symbols from NYSE Arca
path = var_call_id2bpRnt0OETzPJpHCyOwvDc
with open(path, 'r') as f:
    etf_records = json.load(f)

etf_symbols = [r['Symbol'] for r in etf_records]

# Build DuckDB SQL to scan each symbol table for 2015 Adj Close > 200
conditions = []
for sym in etf_symbols:
    # DuckDB table names with special chars might be tricky, but these symbols are standard
    conditions.append(f"SELECT DISTINCT '{sym}' AS Symbol FROM '{sym}' WHERE strftime('%Y', Date) = '2015' AND ""Adj Close"" > 200")

union_sql = " UNION ALL ".join(conditions)

result = {
    'duckdb_query': union_sql[:10000],
    'symbol_count': len(etf_symbols)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_id2bpRnt0OETzPJpHCyOwvDc': 'file_storage/call_id2bpRnt0OETzPJpHCyOwvDc.json', 'var_call_x5aOibK7pYjytfD71prwSmum': 'file_storage/call_x5aOibK7pYjytfD71prwSmum.json'}

exec(code, env_args)
