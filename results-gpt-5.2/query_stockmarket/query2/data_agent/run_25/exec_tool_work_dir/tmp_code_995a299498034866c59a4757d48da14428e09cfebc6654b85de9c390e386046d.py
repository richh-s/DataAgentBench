code = """import json
p = var_call_v8UAmsuj3jIxT9Csk8ySlzip
with open(p,'r') as f:
    etfs = json.load(f)
syms = sorted({r['Symbol'] for r in etfs if r.get('Symbol')})

p2 = var_call_7cQ5gSCfYebF9BuEJ5E83c8m
with open(p2,'r') as f:
    tables = set(json.load(f))

syms_in = [s for s in syms if s in tables]

chunk_size = 120
chunks = [syms_in[i:i+chunk_size] for i in range(0, len(syms_in), chunk_size)]
sql_chunks = []
for chunk in chunks:
    union_parts = []
    for sym in chunk:
        union_parts.append("SELECT '{}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(sym, sym))
    sql_chunks.append("SELECT symbol, max_adj_close FROM (" + " UNION ALL ".join(union_parts) + ") t")

print('__RESULT__:')
print(json.dumps({'n_chunks': len(sql_chunks), 'first_sql_len': len(sql_chunks[0]), 'first_sql_preview': sql_chunks[0][:300]}))"""

env_args = {'var_call_v8UAmsuj3jIxT9Csk8ySlzip': 'file_storage/call_v8UAmsuj3jIxT9Csk8ySlzip.json', 'var_call_7cQ5gSCfYebF9BuEJ5E83c8m': 'file_storage/call_7cQ5gSCfYebF9BuEJ5E83c8m.json', 'var_call_iqqiSjgzDqx5k2lcbtWs0Kwd': {'a': 1}, 'var_call_55B0w63JGtXHNC0oo41XEXig': {'path': 'file_storage/call_v8UAmsuj3jIxT9Csk8ySlzip.json'}, 'var_call_Sr6a395shngtKwEEkSKtxgBA': {'n': 1435, 'first10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_call_QrwaOA1A0ZWk3ANi7o0NzSbG': {'tables_n': 2753, 'has_AGG': True, 'sample': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ', 'ABEQ', 'ABMD', 'ACAD', 'ACES', 'ACIO', 'ACLS', 'ACSG', 'ACSI', 'ACT', 'ACWF', 'ACWI', 'ACWV', 'ACWX', 'ACY', 'ADAP']}, 'var_call_fKSdP5osJUXKnkDW8NEKP5mb': {'syms_in_n': 1435, 'syms_missing_n': 0}}

exec(code, env_args)
