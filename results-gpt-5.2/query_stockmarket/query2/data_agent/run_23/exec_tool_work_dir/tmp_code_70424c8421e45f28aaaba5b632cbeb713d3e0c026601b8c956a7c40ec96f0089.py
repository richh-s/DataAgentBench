code = """import json

p = var_call_L7ddSgvG4pwxWupzI6Jilkxd
if isinstance(p, str):
    with open(p, 'r') as f:
        etfs = json.load(f)
else:
    etfs = p

q = var_call_h8spSELnHicwBjN3VuyEck6c
if isinstance(q, str):
    with open(q, 'r') as f:
        tables = json.load(f)
else:
    tables = q

etf_syms = sorted({r['Symbol'] for r in etfs})
table_set = set(tables)
syms = [s for s in etf_syms if s in table_set]

parts = []
for s in syms:
    ident = '"' + s.replace('"','""') + '"'
    part = (
        "SELECT '" + s.replace("'","''") + "' AS Symbol, MAX(\"Adj Close\") AS max_adj_close "
        "FROM " + ident + " WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'"
    )
    parts.append(part)

if not parts:
    out = {"query": None, "n_syms": 0}
else:
    out = {"query": " UNION ALL ".join(parts), "n_syms": len(syms)}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_L7ddSgvG4pwxWupzI6Jilkxd': 'file_storage/call_L7ddSgvG4pwxWupzI6Jilkxd.json', 'var_call_h8spSELnHicwBjN3VuyEck6c': 'file_storage/call_h8spSELnHicwBjN3VuyEck6c.json'}

exec(code, env_args)
