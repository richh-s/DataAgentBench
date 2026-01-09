code = """import json

path = var_call_YAZ1UBW4wtS43a3iKLtc8A4R
with open(path, 'r') as f:
    etf_syms = [r['symbol'] for r in json.load(f)]

path2 = var_call_KtCAfDmfZykEJa88Eee5Y2tI
with open(path2, 'r') as f:
    price_tables = set(json.load(f))

syms = [s for s in etf_syms if s in price_tables]

chunk_size = 250
chunks = [syms[i:i+chunk_size] for i in range(0, len(syms), chunk_size)]

queries = []
for chunk in chunks:
    union_sql = " UNION ALL ".join([
        "SELECT '"+s+"' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \""+s+"\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'"
        for s in chunk
    ])
    q = "WITH maxes AS (" + union_sql + ") SELECT symbol, max_adj_close_2015 FROM maxes WHERE max_adj_close_2015 > 200"
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'n_chunks': len(queries), 'first_query_len': len(queries[0])}))"""

env_args = {'var_call_YAZ1UBW4wtS43a3iKLtc8A4R': 'file_storage/call_YAZ1UBW4wtS43a3iKLtc8A4R.json', 'var_call_KtCAfDmfZykEJa88Eee5Y2tI': 'file_storage/call_KtCAfDmfZykEJa88Eee5Y2tI.json', 'var_call_KVfk3Dv7tGpgDdPLXoxjCBaR': {'n_syms': 1435}, 'var_call_XRCU3IQ8FJS0gUfyMrQJq0n2': [], 'var_call_g8XLWLIyUF3cAeCakTmS1Jhp': {'n_syms': 1435, 'n_safe_syms': 1435, 'example_unsafe': []}}

exec(code, env_args)
