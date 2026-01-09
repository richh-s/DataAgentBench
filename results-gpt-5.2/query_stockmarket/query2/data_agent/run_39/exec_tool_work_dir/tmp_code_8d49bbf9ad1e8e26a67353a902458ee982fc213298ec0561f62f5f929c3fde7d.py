code = """import json, pandas as pd

# load ETF symbols (NYSE Arca) from sqlite result file
path_etf = var_call_RiPZWWF1mTryWxhHo7gaq8ws
with open(path_etf, 'r') as f:
    etf_recs = json.load(f)
etf_symbols = sorted({r['symbol'] for r in etf_recs if r.get('symbol')})

# load available price tables from duckdb list_db file
path_tbl = var_call_4WNlDK7WYm54JxmY57bjQxWF
with open(path_tbl, 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

# keep only ETFs that have a price table
symbols = [s for s in etf_symbols if s in tables_set]

# build a UNION ALL query to find those with max Adj Close > 200 in 2015
subqs = []
for s in symbols:
    # Quote table name for DuckDB
    subqs.append(f"SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")

# If no symbols, return empty
if not subqs:
    result = {"etfs": [], "total": 0}
    out = json.dumps(result)
    print('__RESULT__:')
    print(out)
else:
    union_query = " UNION ALL ".join(subqs)
    final_query = f"SELECT symbol FROM ({union_query}) t WHERE max_adj_close > 200 ORDER BY symbol;"
    out = json.dumps({"query": final_query, "n_candidates": len(symbols)})
    print('__RESULT__:')
    print(out)"""

env_args = {'var_call_RiPZWWF1mTryWxhHo7gaq8ws': 'file_storage/call_RiPZWWF1mTryWxhHo7gaq8ws.json', 'var_call_4WNlDK7WYm54JxmY57bjQxWF': 'file_storage/call_4WNlDK7WYm54JxmY57bjQxWF.json'}

exec(code, env_args)
