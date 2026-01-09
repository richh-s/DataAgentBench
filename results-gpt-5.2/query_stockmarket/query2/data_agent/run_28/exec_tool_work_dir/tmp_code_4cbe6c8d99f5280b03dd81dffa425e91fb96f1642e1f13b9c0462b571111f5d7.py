code = """import json, pandas as pd

# load ETF list from stockinfo query result (may be a file path)
info_src = var_call_SobbbbZXILGybWnUoxXTVWWx
if isinstance(info_src, str):
    with open(info_src, 'r') as f:
        etfs = json.load(f)
else:
    etfs = info_src

trade_tables_src = var_call_QhxtRLpkISLHodfoZTe1ZO6J
if isinstance(trade_tables_src, str):
    with open(trade_tables_src, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = trade_tables_src

etf_syms = sorted({r['symbol'] for r in etfs})
trade_set = set(trade_tables)
syms = [s for s in etf_syms if s in trade_set]

# chunk symbols to keep query sizes manageable
chunks = [syms[i:i+200] for i in range(0, len(syms), 200)]

queries = []
for ch in chunks:
    parts = []
    for s in ch:
        parts.append(f"SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")
    q = " UNION ALL ".join(parts)
    queries.append(q)

out = {'queries': queries, 'n_symbols': len(syms)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_SobbbbZXILGybWnUoxXTVWWx': 'file_storage/call_SobbbbZXILGybWnUoxXTVWWx.json', 'var_call_QhxtRLpkISLHodfoZTe1ZO6J': 'file_storage/call_QhxtRLpkISLHodfoZTe1ZO6J.json'}

exec(code, env_args)
