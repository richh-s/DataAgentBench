code = """import json, pandas as pd

# Load NYSE Arca ETF symbols from file
path = var_call_iiQ5zxHzDoZ5DGwobdUxljuZ
with open(path, 'r') as f:
    etf_records = json.load(f)

symbols = [r['Symbol'] for r in etf_records]

# Build DuckDB SQL using those symbols
# We'll create a UNION ALL query over each symbol table to find those with Adj Close > 200 in 2015
union_parts = []
for sym in symbols:
    # DuckDB uses identifiers without quoting here; symbols appear to be valid table names
    part = f"SELECT '{sym}' AS Symbol FROM '{sym}' WHERE strftime('%Y', Date) = '2015' AND ""Adj Close"" > 200 GROUP BY Symbol"
    union_parts.append(part)

if union_parts:
    full_query = " UNION ALL ".join(union_parts)
else:
    full_query = "SELECT NULL AS Symbol WHERE 1=0"

result = {'duckdb_query': full_query}

res_json = json.dumps(result)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_iiQ5zxHzDoZ5DGwobdUxljuZ': 'file_storage/call_iiQ5zxHzDoZ5DGwobdUxljuZ.json', 'var_call_Eb0HWx5SFjTAXk3iXhs9Hq6u': 'file_storage/call_Eb0HWx5SFjTAXk3iXhs9Hq6u.json'}

exec(code, env_args)
