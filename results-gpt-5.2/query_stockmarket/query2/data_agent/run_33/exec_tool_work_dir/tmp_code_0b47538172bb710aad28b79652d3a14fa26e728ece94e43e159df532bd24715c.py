code = """import json, pandas as pd

# load NYSE Arca ETFs
path = var_call_XArukLoIiG8IwQBYi6WYLKRp
with open(path, 'r') as f:
    arca = json.load(f)
arca_syms = sorted({r['symbol'] for r in arca if r.get('symbol')})

# load available price tables
p2 = var_call_VrauVfIKb2oALgma41QeGrur
with open(p2, 'r') as f:
    tables = json.load(f)
price_tables = set(tables)

syms = [s for s in arca_syms if s in price_tables]

# chunk symbols to avoid overly long SQL
chunks = [syms[i:i+150] for i in range(0, len(syms), 150)]
queries = []
for ch in chunks:
    parts = []
    for t in ch:
        # use date filter and adj close > 200
        parts.append(f"SELECT '{t}' AS symbol FROM \"{t}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1")
    q = " UNION ALL ".join(parts)
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'queries': queries, 'n_symbols_considered': len(syms)}))"""

env_args = {'var_call_XArukLoIiG8IwQBYi6WYLKRp': 'file_storage/call_XArukLoIiG8IwQBYi6WYLKRp.json', 'var_call_VrauVfIKb2oALgma41QeGrur': 'file_storage/call_VrauVfIKb2oALgma41QeGrur.json'}

exec(code, env_args)
