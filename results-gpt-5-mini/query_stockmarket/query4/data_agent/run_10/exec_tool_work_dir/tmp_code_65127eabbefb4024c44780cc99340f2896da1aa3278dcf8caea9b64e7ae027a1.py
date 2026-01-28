code = """import json
with open(var_call_f1r85XmWDTSl5Ddo53iy59CI, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_6Z6sS3PLvRX8NaXWX42bHpQu, 'r') as f:
    tables = json.load(f)

symbols = []
company_map = {}
for rec in stockinfo:
    sym = rec.get('Symbol')
    if sym:
        symbols.append(sym)
        company_map[sym] = rec.get('Company Description')

available_syms = [s for s in symbols if s in tables]
selects = []
for s in available_syms:
    tbl = '"' + s + '"'
    sel = ("SELECT '" + s + "' AS symbol, SUM(CASE WHEN \"Close\" > \"Open\" THEN 1 ELSE 0 END) AS up, "
           "SUM(CASE WHEN \"Close\" < \"Open\" THEN 1 ELSE 0 END) AS down "
           "FROM " + tbl + " WHERE \"Date\" >= '2017-01-01' AND \"Date\" <= '2017-12-31'")
    selects.append(sel)

if selects:
    sql = "\nUNION ALL\n".join(selects)
else:
    sql = ""

print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_f1r85XmWDTSl5Ddo53iy59CI': 'file_storage/call_f1r85XmWDTSl5Ddo53iy59CI.json', 'var_call_6Z6sS3PLvRX8NaXWX42bHpQu': 'file_storage/call_6Z6sS3PLvRX8NaXWX42bHpQu.json'}

exec(code, env_args)
