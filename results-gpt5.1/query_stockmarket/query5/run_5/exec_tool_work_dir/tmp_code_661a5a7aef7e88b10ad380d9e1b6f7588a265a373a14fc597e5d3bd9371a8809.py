code = """import json
import pandas as pd

# Load full symbol list for NASDAQ Capital Market from JSON file
with open(var_call_lNPGRwGHeTZgSqRHrqBEloGo, 'r') as f:
    stockinfo_records = json.load(f)

symbols = [r['Symbol'] for r in stockinfo_records]

# Build DuckDB SQL to compute, for each symbol, the count of 2019 days with (High-Low)/Low > 0.2
# We will generate a UNION ALL query across all relevant symbol tables that exist in stocktrade_database.

# Load table list from DuckDB file
with open(var_call_VuZPSbgDhdXLEOCyvdWeHMJE, 'r') as f:
    trade_tables = set(json.load(f))

valid_symbols = [s for s in symbols if s in trade_tables]

union_parts = []
for sym in valid_symbols:
    part = f"SELECT '{sym}' AS Symbol, COUNT(*) AS cnt FROM '{sym}' WHERE substr(Date,1,4) = '2019' AND Low > 0 AND (High - Low)/Low > 0.2"
    union_parts.append(part)

if not union_parts:
    result = []
else:
    union_sql = " UNION ALL ".join(union_parts)
    outer_sql = f"SELECT Symbol, cnt FROM ({union_sql}) ORDER BY cnt DESC LIMIT 5"
    result = outer_sql

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_VuZPSbgDhdXLEOCyvdWeHMJE': 'file_storage/call_VuZPSbgDhdXLEOCyvdWeHMJE.json', 'var_call_lNPGRwGHeTZgSqRHrqBEloGo': 'file_storage/call_lNPGRwGHeTZgSqRHrqBEloGo.json'}

exec(code, env_args)
