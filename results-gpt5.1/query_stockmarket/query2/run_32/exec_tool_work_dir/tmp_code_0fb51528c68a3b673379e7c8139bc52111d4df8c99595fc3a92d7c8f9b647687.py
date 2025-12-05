code = """import json, pandas as pd
from datetime import datetime

# Load ETF symbols from file
with open(var_call_ns812X1uazipzQmTLMgrv9EG, 'r') as f:
    etf_rows = json.load(f)

etf_symbols = [row['Symbol'] for row in etf_rows]

# Load all stocktrade tables list
with open(var_call_uoj0YyqKrT6pPkD98kn3a3qk, 'r') as f:
    all_tables = json.load(f)

# Intersect to get symbols that have price data
symbols = sorted(set(etf_symbols).intersection(all_tables))

# Build DuckDB SQL using UNION ALL
parts = []
for sym in symbols:
    parts.append(f"SELECT '{sym}' AS Symbol, \"Date\", \"Adj Close\" FROM '{sym}' WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31' AND \"Adj Close\" > 200")

if parts:
    union_sql = " UNION ALL ".join(parts)
else:
    union_sql = "SELECT NULL AS Symbol, NULL AS Date, NULL AS \"Adj Close\" WHERE 1=0"

result = {
    'symbols': symbols,
    'duckdb_sql': union_sql[:9900]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ns812X1uazipzQmTLMgrv9EG': 'file_storage/call_ns812X1uazipzQmTLMgrv9EG.json', 'var_call_uoj0YyqKrT6pPkD98kn3a3qk': 'file_storage/call_uoj0YyqKrT6pPkD98kn3a3qk.json'}

exec(code, env_args)
