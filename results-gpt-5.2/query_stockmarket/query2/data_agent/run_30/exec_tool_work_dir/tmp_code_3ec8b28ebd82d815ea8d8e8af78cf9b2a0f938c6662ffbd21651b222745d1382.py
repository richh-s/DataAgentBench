code = """import json, pandas as pd

# load symbols (NYSE Arca ETFs)
path = var_call_rtrl8RNO3l8To1mSqWStympT
with open(path, 'r') as f:
    syms = [r['symbol'] for r in json.load(f)]

# load available price tables
path2 = var_call_YeDPrvgXGIqbJWv3usn3iXl3
with open(path2, 'r') as f:
    tables = set(json.load(f))

syms_avail = [s for s in syms if s in tables]

# chunk symbols for SQL IN lists
chunks = [syms_avail[i:i+200] for i in range(0, len(syms_avail), 200)]

queries = []
for ch in chunks:
    # DuckDB can query across tables via union all
    parts = []
    for s in ch:
        parts.append(f"SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")
    queries.append(" UNION ALL ".join(parts))

result_sql = "SELECT symbol, max_adj_close FROM (" + (" UNION ALL ".join([f"({q})" for q in queries])) + ") WHERE max_adj_close > 200 ORDER BY symbol"

out = {"sql": result_sql, "n_syms_arca_etf": len(syms), "n_syms_avail": len(syms_avail)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_rtrl8RNO3l8To1mSqWStympT': 'file_storage/call_rtrl8RNO3l8To1mSqWStympT.json', 'var_call_YeDPrvgXGIqbJWv3usn3iXl3': 'file_storage/call_YeDPrvgXGIqbJWv3usn3iXl3.json'}

exec(code, env_args)
