code = """import json, pandas as pd

path_info = var_call_kponoIuDHUEwq9e7xalQW6GZ
with open(path_info, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)
etf_symbols = set(info_df['Symbol'].tolist())

path_tbls = var_call_TwzwBf2CmUgz31GMXGZ9o0lB
with open(path_tbls, 'r') as f:
    tbls = json.load(f)
trade_tables = set(tbls)

symbols = sorted(etf_symbols & trade_tables)

parts = []
for s in symbols:
    parts.append(
        "SELECT '{sym}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{sym}\" "
        "WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(sym=s)
    )

if not parts:
    result = {"etfs": [], "total": 0}
    print('__RESULT__:')
    print(json.dumps(result))
else:
    union_query = " UNION ALL ".join(parts)
    final_query = "SELECT symbol, max_adj_close FROM ({u}) t WHERE max_adj_close > 200 ORDER BY symbol".format(u=union_query)
    print('__RESULT__:')
    print(json.dumps({"duckdb_query": final_query, "n_symbols": len(symbols)}))"""

env_args = {'var_call_kponoIuDHUEwq9e7xalQW6GZ': 'file_storage/call_kponoIuDHUEwq9e7xalQW6GZ.json', 'var_call_TwzwBf2CmUgz31GMXGZ9o0lB': 'file_storage/call_TwzwBf2CmUgz31GMXGZ9o0lB.json'}

exec(code, env_args)
