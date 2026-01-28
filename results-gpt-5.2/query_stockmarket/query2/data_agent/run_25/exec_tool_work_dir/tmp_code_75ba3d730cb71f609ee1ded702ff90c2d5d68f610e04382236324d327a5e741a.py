code = """import json
p = var_call_v8UAmsuj3jIxT9Csk8ySlzip
with open(p,'r') as f:
    etfs = json.load(f)
syms = sorted({r['Symbol'] for r in etfs if r.get('Symbol')})

# build union query in chunks
chunk_size = 80
chunks = [syms[i:i+chunk_size] for i in range(0, len(syms), chunk_size)]
chunk_queries = []
for chunk in chunks:
    parts = []
    for s in chunk:
        parts.append("SELECT * FROM (SELECT '{}' AS symbol FROM \"{}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1)".format(s,s))
    chunk_queries.append(" UNION ALL ".join(parts) + ";")

print('__RESULT__:')
print(json.dumps({'n_chunks': len(chunk_queries), 'first_preview': chunk_queries[0][:400], 'chunk_queries': chunk_queries}))"""

env_args = {'var_call_v8UAmsuj3jIxT9Csk8ySlzip': 'file_storage/call_v8UAmsuj3jIxT9Csk8ySlzip.json', 'var_call_7cQ5gSCfYebF9BuEJ5E83c8m': 'file_storage/call_7cQ5gSCfYebF9BuEJ5E83c8m.json', 'var_call_iqqiSjgzDqx5k2lcbtWs0Kwd': {'a': 1}, 'var_call_55B0w63JGtXHNC0oo41XEXig': {'path': 'file_storage/call_v8UAmsuj3jIxT9Csk8ySlzip.json'}, 'var_call_Sr6a395shngtKwEEkSKtxgBA': {'n': 1435, 'first10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_call_QrwaOA1A0ZWk3ANi7o0NzSbG': {'tables_n': 2753, 'has_AGG': True, 'sample': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ', 'ABEQ', 'ABMD', 'ACAD', 'ACES', 'ACIO', 'ACLS', 'ACSG', 'ACSI', 'ACT', 'ACWF', 'ACWI', 'ACWV', 'ACWX', 'ACY', 'ADAP']}, 'var_call_fKSdP5osJUXKnkDW8NEKP5mb': {'syms_in_n': 1435, 'syms_missing_n': 0}, 'var_call_cGpWuFuWR7mdRb3dBPffDcKb': {'test': "SELECT 'AAA' AS symbol"}, 'var_call_Vg09BbEVnHU1B16EcsMyuj2x': [{'max_adj_close': 'nan'}], 'var_call_Px6JuEjnXD02bHaV1FHJlxuD': [], 'var_call_ESZwozt3urbNmLanHqoJVHv8': [{'s': 'A'}], 'var_call_ZgaAXrSBcH6V0aGZxGGDGyVt': [{'name': 'AAAU'}, {'name': 'AADR'}, {'name': 'AAME'}, {'name': 'AAWW'}, {'name': 'AAXJ'}], 'var_call_wSaiZS1hDne5EjSBQr9ZcFmP': []}

exec(code, env_args)
