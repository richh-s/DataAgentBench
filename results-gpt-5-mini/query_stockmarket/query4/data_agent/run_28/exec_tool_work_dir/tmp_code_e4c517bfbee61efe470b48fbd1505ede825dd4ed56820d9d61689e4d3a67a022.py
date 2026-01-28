code = """import json
with open(var_call_0OQoxi0RGALCl4N4gLElsShB) as f:
    stockinfo = json.load(f)
with open(var_call_XsIeG3HYTleq4ExFbL3Whb4D) as f:
    tables = json.load(f)

sym_to_name = {}
for r in stockinfo:
    sym = r.get('Symbol')
    name = r.get('Company Description')
    if sym:
        sym_to_name[sym] = name

available_symbols = [s for s in sym_to_name.keys() if s in tables]

parts = []
for sym in available_symbols:
    part = "SELECT '%s' AS symbol, SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) AS up, SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) AS down FROM \"%s\" WHERE \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31'" % (sym, sym)
    parts.append(part)

sql = (" UNION ALL ".join(parts) + ";") if parts else ""

output = {"sql": sql, "symbols_count": len(available_symbols)}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_0OQoxi0RGALCl4N4gLElsShB': 'file_storage/call_0OQoxi0RGALCl4N4gLElsShB.json', 'var_call_XsIeG3HYTleq4ExFbL3Whb4D': 'file_storage/call_XsIeG3HYTleq4ExFbL3Whb4D.json'}

exec(code, env_args)
