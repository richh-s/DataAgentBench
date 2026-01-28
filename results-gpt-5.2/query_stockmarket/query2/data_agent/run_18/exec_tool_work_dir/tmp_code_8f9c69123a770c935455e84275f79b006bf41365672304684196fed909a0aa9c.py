code = """import json, pandas as pd

# load symbols (NYSE Arca ETFs)
path = var_call_YAZ1UBW4wtS43a3iKLtc8A4R
with open(path, 'r') as f:
    etf_syms = [r['symbol'] for r in json.load(f)]

# load available price tables
path2 = var_call_KtCAfDmfZykEJa88Eee5Y2tI
with open(path2, 'r') as f:
    price_tables = set(json.load(f))

syms = [s for s in etf_syms if s in price_tables]

# build UNION query to find max Adj Close in 2015 per symbol, then filter >200
parts = []
for s in syms:
    # table name may need quoting if special chars; use double quotes
    parts.append(f"SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")

# chunk unions to avoid overly large queries
chunk_size = 400
chunks = [parts[i:i+chunk_size] for i in range(0, len(parts), chunk_size)]

print('__RESULT__:')
print(json.dumps({'n_syms': len(syms), 'n_chunks': len(chunks), 'first_chunk_len': len(chunks[0]) if chunks else 0}))"""

env_args = {'var_call_YAZ1UBW4wtS43a3iKLtc8A4R': 'file_storage/call_YAZ1UBW4wtS43a3iKLtc8A4R.json', 'var_call_KtCAfDmfZykEJa88Eee5Y2tI': 'file_storage/call_KtCAfDmfZykEJa88Eee5Y2tI.json'}

exec(code, env_args)
