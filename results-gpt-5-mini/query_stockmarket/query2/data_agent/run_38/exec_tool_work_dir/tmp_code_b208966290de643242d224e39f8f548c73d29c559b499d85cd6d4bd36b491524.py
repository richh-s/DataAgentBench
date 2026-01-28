code = """import json
path = var_call_iy1Wl4j8WobUxW4UkYuf7dP0
with open(path, 'r') as f:
    data = json.load(f)
symbols = [r['Symbol'] for r in data if r.get('Symbol')]
parts = []
for s in symbols:
    dq = '"'
    part = "SELECT '{}' AS Symbol, MAX({}) AS max_adj FROM {} WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(s, dq + 'Adj Close' + dq, dq + s + dq)
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
