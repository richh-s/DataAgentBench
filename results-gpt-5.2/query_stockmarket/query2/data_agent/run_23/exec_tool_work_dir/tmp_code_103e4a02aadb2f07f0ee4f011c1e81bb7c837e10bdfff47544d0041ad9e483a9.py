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
syms = [s for s in etf_syms if s in set(tables)]

s = syms[0] if syms else ''
ident = '"' + s.replace('"','""') + '"'
sym_sql = s.replace("'","''")
part = "SELECT '{}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close FROM {} WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(sym_sql, ident)

print('__RESULT__:')
print(json.dumps({'sym0': s, 'part': part, 'n_syms': len(syms)}))"""

env_args = {'var_call_L7ddSgvG4pwxWupzI6Jilkxd': 'file_storage/call_L7ddSgvG4pwxWupzI6Jilkxd.json', 'var_call_h8spSELnHicwBjN3VuyEck6c': 'file_storage/call_h8spSELnHicwBjN3VuyEck6c.json', 'var_call_wERm2QHfA2RBc64TBAhT7uxH': {'ok': True}}

exec(code, env_args)
