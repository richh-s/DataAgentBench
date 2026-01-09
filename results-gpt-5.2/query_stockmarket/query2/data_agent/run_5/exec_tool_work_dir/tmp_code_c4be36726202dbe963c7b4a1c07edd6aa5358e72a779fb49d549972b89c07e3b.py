code = """import json, pandas as pd

# Load ETF symbols listed on NYSE Arca (from sqlite result)
path_info = var_call_kponoIuDHUEwq9e7xalQW6GZ
with open(path_info, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)
etf_symbols = set(info_df['Symbol'].tolist())

# Load available trade tables
path_tbls = var_call_TwzwBf2CmUgz31GMXGZ9o0lB
with open(path_tbls, 'r') as f:
    tbls = json.load(f)
trade_tables = set(tbls)

symbols = sorted(etf_symbols & trade_tables)

# Build a UNION ALL query to get max Adj Close in 2015 for each symbol
parts = []
for s in symbols:
    # duckdb identifiers: use double quotes
    parts.append(f"SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")

# If no symbols, return empty
if not parts:
    result = {"etfs": [], "total": 0}
    out = json.dumps(result)
    print('__RESULT__:')
    print(out)
else:
    union_query = "\nUNION ALL\n".join(parts)
    final_query = f"SELECT symbol, max_adj_close FROM ({union_query}) t WHERE max_adj_close > 200 ORDER BY symbol;"
    out = {"duckdb_query": final_query, "n_symbols": len(symbols)}
    print('__RESULT__:')
    print(json.dumps(out))"""

env_args = {'var_call_kponoIuDHUEwq9e7xalQW6GZ': 'file_storage/call_kponoIuDHUEwq9e7xalQW6GZ.json', 'var_call_TwzwBf2CmUgz31GMXGZ9o0lB': 'file_storage/call_TwzwBf2CmUgz31GMXGZ9o0lB.json'}

exec(code, env_args)
