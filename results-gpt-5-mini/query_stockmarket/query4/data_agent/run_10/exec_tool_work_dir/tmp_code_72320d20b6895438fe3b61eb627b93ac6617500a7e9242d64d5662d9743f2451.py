code = """import json
# load the stockinfo result and the list of tables
with open(var_call_f1r85XmWDTSl5Ddo53iy59CI, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_6Z6sS3PLvRX8NaXWX42bHpQu, 'r') as f:
    tables = json.load(f)

# extract symbols and mapping from company description
symbols = []
company_map = {}
for rec in stockinfo:
    sym = rec.get('Symbol')
    if sym:
        symbols.append(sym)
        company_map[sym] = rec.get('Company Description')

# intersect with available tables
available_syms = [s for s in symbols if s in tables]

# build UNION ALL SQL across available symbols
selects = []
for s in available_syms:
    # quote table name
    tbl = f'"{s}"'
    sel = (
        f"SELECT '{s}' AS symbol, SUM(CASE WHEN \"Close\" > \"Open\" THEN 1 ELSE 0 END) AS up, "
        f"SUM(CASE WHEN \"Close\" < \"Open\" THEN 1 ELSE 0 END) AS down "
        f"FROM {tbl} WHERE \"Date\" >= '2017-01-01' AND \"Date\" <= '2017-12-31'"
    )
    selects.append(sel)

if not selects:
    sql = ''
else:
    sql = '\nUNION ALL\n'.join(selects) + '\n'

# print result as JSON string
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_f1r85XmWDTSl5Ddo53iy59CI': 'file_storage/call_f1r85XmWDTSl5Ddo53iy59CI.json', 'var_call_6Z6sS3PLvRX8NaXWX42bHpQu': 'file_storage/call_6Z6sS3PLvRX8NaXWX42bHpQu.json'}

exec(code, env_args)
