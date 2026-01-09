code = """import json

p = var_call_v8UAmsuj3jIxT9Csk8ySlzip
with open(p, 'r') as f:
    etfs = json.load(f)

symbols = sorted({r['Symbol'] for r in etfs if r.get('Symbol')})

p2 = var_call_7cQ5gSCfYebF9BuEJ5E83c8m
with open(p2, 'r') as f:
    tables = set(json.load(f))

symbols_in_db = [s for s in symbols if s in tables]

chunks = [symbols_in_db[i:i+200] for i in range(0, len(symbols_in_db), 200)]

sql_chunks = []
for chunk in chunks:
    union_parts = []
    for sym in chunk:
        union_parts.append("SELECT '{}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(sym, sym))
    sql = "SELECT symbol, max_adj_close FROM ({} ) t".format(" UNION ALL ".join(union_parts))
    sql_chunks.append(sql)

print('__RESULT__:')
print(json.dumps({'symbols_total': len(symbols), 'symbols_in_price_db': len(symbols_in_db), 'sql_chunks': sql_chunks}))"""

env_args = {'var_call_v8UAmsuj3jIxT9Csk8ySlzip': 'file_storage/call_v8UAmsuj3jIxT9Csk8ySlzip.json', 'var_call_7cQ5gSCfYebF9BuEJ5E83c8m': 'file_storage/call_7cQ5gSCfYebF9BuEJ5E83c8m.json'}

exec(code, env_args)
