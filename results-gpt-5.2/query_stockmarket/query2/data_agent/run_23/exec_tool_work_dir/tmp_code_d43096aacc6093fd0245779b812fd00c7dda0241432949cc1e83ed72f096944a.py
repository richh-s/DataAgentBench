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

# batch symbols
batch_size = 200
batches = [syms[i:i+batch_size] for i in range(0, len(syms), batch_size)]

print('__RESULT__:')
print(json.dumps({'n_syms': len(syms), 'n_batches': len(batches), 'batches': batches[:5]}))"""

env_args = {'var_call_L7ddSgvG4pwxWupzI6Jilkxd': 'file_storage/call_L7ddSgvG4pwxWupzI6Jilkxd.json', 'var_call_h8spSELnHicwBjN3VuyEck6c': 'file_storage/call_h8spSELnHicwBjN3VuyEck6c.json', 'var_call_wERm2QHfA2RBc64TBAhT7uxH': {'ok': True}, 'var_call_AWJg34e7rBqyftomAJ8IkUFQ': [{'name': 'AAAU'}], 'var_call_4mAtZaLzNVFHo1lAqNHCJ4kZ': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'AAME'}, {'Symbol': 'AAWW'}, {'Symbol': 'AAXJ'}], 'var_call_y4ad1lBzUMoMZ5Pz0hpvjNNG': {'note': 'skip python build; will query per symbol'}}

exec(code, env_args)
