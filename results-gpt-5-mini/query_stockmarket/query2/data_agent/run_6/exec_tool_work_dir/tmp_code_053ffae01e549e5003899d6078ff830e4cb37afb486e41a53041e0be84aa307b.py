code = """import json
with open(var_call_OA5c55w6JsC8kjxHPlWH1BwK) as f:
    etf_records = json.load(f)
symbols = [r['Symbol'] for r in etf_records]
with open(var_call_H1CE2LVMDOMyJX0LZCSItIcn) as f:
    tables = json.load(f)
table_set = set(tables)
common = [s for s in symbols if s in table_set]
parts = []
for s in common:
    part = "SELECT '" + s + "' AS symbol, MAX(\"Adj Close\") AS max_adj FROM \"" + s + "\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'"
    parts.append(part)
if parts:
    sql = " UNION ALL ".join(parts) + " ORDER BY symbol"
else:
    sql = ""
res = {"sql": sql, "symbols_count": len(common), "symbols": common}
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_EX7fJ1N82JvZuW4MmN0Y3kC2': ['stockinfo'], 'var_call_H1CE2LVMDOMyJX0LZCSItIcn': 'file_storage/call_H1CE2LVMDOMyJX0LZCSItIcn.json', 'var_call_OA5c55w6JsC8kjxHPlWH1BwK': 'file_storage/call_OA5c55w6JsC8kjxHPlWH1BwK.json'}

exec(code, env_args)
