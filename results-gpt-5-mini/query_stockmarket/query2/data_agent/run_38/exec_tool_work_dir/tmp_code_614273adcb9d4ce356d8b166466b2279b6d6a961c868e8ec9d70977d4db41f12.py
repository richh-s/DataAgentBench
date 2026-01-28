code = """import json
# var_call_iy1Wl4j8WobUxW4UkYuf7dP0 is provided in storage and contains the path to the JSON file with the stockinfo query result
path = var_call_iy1Wl4j8WobUxW4UkYuf7dP0
with open(path, 'r') as f:
    data = json.load(f)
symbols = [r['Symbol'] for r in data]
# Build a UNION ALL query for DuckDB (stocktrade_database)
parts = []
for s in symbols:
    # Safe-guard: skip symbols that are empty
    if not s or not isinstance(s, str):
        continue
    # Use double quotes around table names to be safe
    part = f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
    parts.append(part)
if not parts:
    sql = "SELECT NULL as Symbol, NULL as max_adj WHERE 1=0;"
else:
    sql = "\nUNION ALL\n".join(parts)
    sql = "SELECT Symbol, max_adj FROM (\n" + sql + "\n) t WHERE max_adj > 200 ORDER BY Symbol;"
out = {"query": sql, "num_symbols": len(symbols)}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_iy1Wl4j8WobUxW4UkYuf7dP0': 'file_storage/call_iy1Wl4j8WobUxW4UkYuf7dP0.json'}

exec(code, env_args)
