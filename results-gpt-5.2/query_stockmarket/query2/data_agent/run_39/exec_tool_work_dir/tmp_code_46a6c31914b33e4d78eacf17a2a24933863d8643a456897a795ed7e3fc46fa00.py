code = """import json

path_etf = var_call_RiPZWWF1mTryWxhHo7gaq8ws
with open(path_etf, 'r') as f:
    etf_recs = json.load(f)
etf_symbols = sorted({r.get('symbol') for r in etf_recs if r.get('symbol')})

path_tbl = var_call_4WNlDK7WYm54JxmY57bjQxWF
with open(path_tbl, 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

symbols = [s for s in etf_symbols if s in tables_set]

subqs = []
for s in symbols:
    subqs.append("SELECT '{sym}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{sym}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(sym=s))

if not subqs:
    payload = {"symbols": [], "count": 0}
    print('__RESULT__:')
    print(json.dumps(payload))
else:
    union_query = " UNION ALL ".join(subqs)
    final_query = "SELECT symbol FROM ({u}) t WHERE max_adj_close > 200 ORDER BY symbol".format(u=union_query)
    payload = {"final_query": final_query, "n_candidates": len(symbols)}
    print('__RESULT__:')
    print(json.dumps(payload))"""

env_args = {'var_call_RiPZWWF1mTryWxhHo7gaq8ws': 'file_storage/call_RiPZWWF1mTryWxhHo7gaq8ws.json', 'var_call_4WNlDK7WYm54JxmY57bjQxWF': 'file_storage/call_4WNlDK7WYm54JxmY57bjQxWF.json'}

exec(code, env_args)
