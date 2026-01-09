code = """import json, pandas as pd

# load symbols from stockinfo query
sym_src = var_call_FwNcDF3iwlazdyPwGJi8JE2b
if isinstance(sym_src, str):
    with open(sym_src, 'r') as f:
        sym_recs = json.load(f)
else:
    sym_recs = sym_src
etf_syms = sorted({r['symbol'] for r in sym_recs if r.get('symbol')})

# load available tables in trade db
tbl_src = var_call_A8o08Mw0I7XOaFqIfRijWItO
if isinstance(tbl_src, str):
    with open(tbl_src, 'r') as f:
        tables = json.load(f)
else:
    tables = tbl_src
avail = set(tables)

syms = [s for s in etf_syms if s in avail]

# batch query max adj close in 2015 per symbol
batch_size = 80
out = []
for i in range(0, len(syms), batch_size):
    batch = syms[i:i+batch_size]
    parts = []
    for s in batch:
        # Date is string; compare lexicographically
        parts.append(f"SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")
    q = " UNION ALL ".join(parts) + ";"
    res = functions.query_db(db_name='stocktrade_database', query=q)
    out.extend(res)

# filter > 200
res_df = pd.DataFrame(out)
if not res_df.empty:
    res_df['max_adj_close'] = pd.to_numeric(res_df['max_adj_close'], errors='coerce')
    res_df = res_df[res_df['max_adj_close'] > 200].sort_values(['symbol'])

symbols = res_df['symbol'].tolist() if not res_df.empty else []
answer = {"symbols": symbols, "total": len(symbols)}

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_FwNcDF3iwlazdyPwGJi8JE2b': 'file_storage/call_FwNcDF3iwlazdyPwGJi8JE2b.json', 'var_call_A8o08Mw0I7XOaFqIfRijWItO': 'file_storage/call_A8o08Mw0I7XOaFqIfRijWItO.json'}

exec(code, env_args)
