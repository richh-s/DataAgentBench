code = """import json
# find ETFs on NYSE Arca that have max Adj Close > 200 during 2015
p = var_call_v8UAmsuj3jIxT9Csk8ySlzip
with open(p,'r') as f:
    etfs = json.load(f)

syms = sorted({r['Symbol'] for r in etfs if r.get('Symbol')})

sql_list = []
for sym in syms:
    sql_list.append("SELECT '{}' AS symbol FROM \"{}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1".format(sym, sym))

# chunk into groups to be executed sequentially outside python
chunk_size = 200
chunks = [sql_list[i:i+chunk_size] for i in range(0, len(sql_list), chunk_size)]
chunk_sql = [" UNION ALL ".join(c) for c in chunks]

print('__RESULT__:')
print(json.dumps({'n_chunks': len(chunk_sql), 'first_chunk_preview': chunk_sql[0][:300], 'chunk_sql': chunk_sql}))"""

env_args = {'var_call_v8UAmsuj3jIxT9Csk8ySlzip': 'file_storage/call_v8UAmsuj3jIxT9Csk8ySlzip.json', 'var_call_7cQ5gSCfYebF9BuEJ5E83c8m': 'file_storage/call_7cQ5gSCfYebF9BuEJ5E83c8m.json', 'var_call_iqqiSjgzDqx5k2lcbtWs0Kwd': {'a': 1}, 'var_call_55B0w63JGtXHNC0oo41XEXig': {'path': 'file_storage/call_v8UAmsuj3jIxT9Csk8ySlzip.json'}, 'var_call_Sr6a395shngtKwEEkSKtxgBA': {'n': 1435, 'first10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_call_QrwaOA1A0ZWk3ANi7o0NzSbG': {'tables_n': 2753, 'has_AGG': True, 'sample': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ', 'ABEQ', 'ABMD', 'ACAD', 'ACES', 'ACIO', 'ACLS', 'ACSG', 'ACSI', 'ACT', 'ACWF', 'ACWI', 'ACWV', 'ACWX', 'ACY', 'ADAP']}, 'var_call_fKSdP5osJUXKnkDW8NEKP5mb': {'syms_in_n': 1435, 'syms_missing_n': 0}, 'var_call_cGpWuFuWR7mdRb3dBPffDcKb': {'test': "SELECT 'AAA' AS symbol"}, 'var_call_Vg09BbEVnHU1B16EcsMyuj2x': [{'max_adj_close': 'nan'}]}

exec(code, env_args)
