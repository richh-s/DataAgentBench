code = """import json
path = var_call_XArukLoIiG8IwQBYi6WYLKRp
with open(path,'r') as f:
    arca = json.load(f)
arca_syms = sorted({r['symbol'] for r in arca if r.get('symbol')})

p2 = var_call_VrauVfIKb2oALgma41QeGrur
with open(p2,'r') as f:
    tables = json.load(f)
price_tables = set(tables)

syms = [s for s in arca_syms if s in price_tables]

chunks = [syms[i:i+120] for i in range(0, len(syms), 120)]
queries = []
for ch in chunks:
    parts = []
    for t in ch:
        parts.append("SELECT '{sym}' AS symbol FROM \"{tbl}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1".format(sym=t, tbl=t))
    queries.append(' UNION ALL '.join(parts))

print('__RESULT__:')
print(json.dumps({'n_symbols_considered': len(syms), 'n_chunks': len(chunks), 'chunk0_len': len(chunks[0]), 'q0_preview': queries[0][:300]}))"""

env_args = {'var_call_XArukLoIiG8IwQBYi6WYLKRp': 'file_storage/call_XArukLoIiG8IwQBYi6WYLKRp.json', 'var_call_VrauVfIKb2oALgma41QeGrur': 'file_storage/call_VrauVfIKb2oALgma41QeGrur.json', 'var_call_5yd6iK4Ba3Pm0UC8gOD6H3DI': {'ok': True}, 'var_call_ThGGdCRH3ze8tkwCMGRjOqom': [{'test': 'SPY'}], 'var_call_etnvztMNBYEzOZWPAzj6RYex': [{'n': '2752'}], 'var_call_RJSEkI7sbGwtxux8PAqFBRDw': {'n': 1435, 'first10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_call_37Fe3e7asxW2cgGOOnceRcRR': {'n_tables': 2753, 'has_AAAU': True}}

exec(code, env_args)
