code = """import json

path = var_call_rtrl8RNO3l8To1mSqWStympT
with open(path, 'r') as f:
    syms = [r['symbol'] for r in json.load(f)]

path2 = var_call_YeDPrvgXGIqbJWv3usn3iXl3
with open(path2, 'r') as f:
    tables = set(json.load(f))

syms_avail = [s for s in syms if s in tables]

chunks = [syms_avail[i:i+150] for i in range(0, len(syms_avail), 150)]

subqueries = []
for ch in chunks:
    parts = []
    for s in ch:
        parts.append("SELECT '{sym}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{sym}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(sym=s))
    subqueries.append(" UNION ALL ".join(parts))

union_all = " UNION ALL ".join(["(" + q + ")" for q in subqueries])
sql = "SELECT symbol, max_adj_close FROM (" + union_all + ") t WHERE max_adj_close > 200 ORDER BY symbol"

out = {"sql": sql, "n_syms_arca_etf": len(syms), "n_syms_avail": len(syms_avail)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_rtrl8RNO3l8To1mSqWStympT': 'file_storage/call_rtrl8RNO3l8To1mSqWStympT.json', 'var_call_YeDPrvgXGIqbJWv3usn3iXl3': 'file_storage/call_YeDPrvgXGIqbJWv3usn3iXl3.json'}

exec(code, env_args)
