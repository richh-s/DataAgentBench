code = """import json, pandas as pd

with open(var_call_kponoIuDHUEwq9e7xalQW6GZ, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)
etf_symbols = set(info_df['Symbol'].tolist())

with open(var_call_TwzwBf2CmUgz31GMXGZ9o0lB, 'r') as f:
    tbls = json.load(f)
trade_tables = set(tbls)

symbols = sorted(etf_symbols & trade_tables)

parts = []
for s in symbols:
    q = (
        "SELECT '{sym}' AS symbol, MAX(\"Adj Close\") AS max_adj_close "
        "FROM \"{sym}\" "
        "WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'"
    ).format(sym=s)
    parts.append(q)

if not parts:
    result = {"duckdb_query": None, "n_symbols": 0}
else:
    union_query = " UNION ALL ".join(parts)
    final_query = "SELECT symbol, max_adj_close FROM ({u}) t WHERE max_adj_close > 200 ORDER BY symbol".format(u=union_query)
    result = {"duckdb_query": final_query, "n_symbols": len(symbols)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_kponoIuDHUEwq9e7xalQW6GZ': 'file_storage/call_kponoIuDHUEwq9e7xalQW6GZ.json', 'var_call_TwzwBf2CmUgz31GMXGZ9o0lB': 'file_storage/call_TwzwBf2CmUgz31GMXGZ9o0lB.json'}

exec(code, env_args)
