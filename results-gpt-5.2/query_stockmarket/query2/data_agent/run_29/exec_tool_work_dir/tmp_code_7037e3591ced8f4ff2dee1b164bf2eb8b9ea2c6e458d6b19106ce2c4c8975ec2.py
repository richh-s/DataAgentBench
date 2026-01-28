code = """import json, pandas as pd

sym_src = var_call_FwNcDF3iwlazdyPwGJi8JE2b
if isinstance(sym_src, str):
    with open(sym_src, 'r') as f:
        sym_recs = json.load(f)
else:
    sym_recs = sym_src
etf_syms = sorted({r['symbol'] for r in sym_recs if r.get('symbol')})

tbl_src = var_call_A8o08Mw0I7XOaFqIfRijWItO
if isinstance(tbl_src, str):
    with open(tbl_src, 'r') as f:
        tables = json.load(f)
else:
    tables = tbl_src
avail = set(tables)

syms = [s for s in etf_syms if s in avail]

batch_size = 60
out = []
for i in range(0, len(syms), batch_size):
    batch = syms[i:i+batch_size]
    parts = []
    for s in batch:
        parts.append("SELECT '{sym}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{sym}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(sym=s))
    q = " UNION ALL ".join(parts) + ";"
    # query_db must be called as a tool; not available inside python environment
    # Instead, we output the batch queries for external execution (not possible here)

print('__RESULT__:')
print(json.dumps({'error':'Cannot call query_db from execute_python in this environment. Need sequential query_db tool calls.'}))"""

env_args = {'var_call_FwNcDF3iwlazdyPwGJi8JE2b': 'file_storage/call_FwNcDF3iwlazdyPwGJi8JE2b.json', 'var_call_A8o08Mw0I7XOaFqIfRijWItO': 'file_storage/call_A8o08Mw0I7XOaFqIfRijWItO.json'}

exec(code, env_args)
