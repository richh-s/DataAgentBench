code = """import json, pandas as pd
from pathlib import Path

# Load full symbol list for NYSE Arca ETFs
path = Path(var_call_yxD1BwvtW2fcDdUbyQAXR2O9)
nyse_arca_etfs = pd.read_json(path).Symbol.tolist()

# Load available price tables
path2 = Path(var_call_VtowIwh6HR6V2l3VMkqd0jpu)
available_tables = set(pd.read_json(path2).tolist())

# Intersection of ETFs that have price data
symbols = sorted(set(nyse_arca_etfs) & available_tables)

# Build DuckDB SQL to scan each symbol table for 2015 adj close > 200
# Use UNION ALL of per-table queries, then distinct symbol list
queries = []
for sym in symbols:
    queries.append(f"SELECT DISTINCT '{sym}' AS Symbol FROM '{sym}' WHERE strftime('%Y', Date) = '2015' AND ""Adj Close"" > 200")

if queries:
    union_sql = " UNION ALL ".join(queries)
else:
    union_sql = "SELECT 'NONE' AS Symbol WHERE 1=0"

result = {
    "symbols": symbols,
    "union_sql": union_sql
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_yxD1BwvtW2fcDdUbyQAXR2O9': 'file_storage/call_yxD1BwvtW2fcDdUbyQAXR2O9.json', 'var_call_VtowIwh6HR6V2l3VMkqd0jpu': 'file_storage/call_VtowIwh6HR6V2l3VMkqd0jpu.json'}

exec(code, env_args)
