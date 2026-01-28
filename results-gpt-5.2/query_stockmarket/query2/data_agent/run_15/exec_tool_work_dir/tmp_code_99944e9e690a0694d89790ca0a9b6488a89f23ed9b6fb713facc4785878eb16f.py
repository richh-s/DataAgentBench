code = """import json
with open(var_call_SHDdrZidyTVCLBbYlkxeT7Vz,'r') as f:
    data = json.load(f)
syms = data['symbols']

parts = []
for s in syms:
    parts.append("SELECT '"+s+"' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \""+s+"\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'")

# chunk query strings
maxlen = 700000
chunks=[]
cur=[]
cur_len=0
for p in parts:
    add_len = len(p) + (11 if cur else 0)
    if cur and cur_len + add_len > maxlen:
        chunks.append(cur)
        cur=[p]
        cur_len=len(p)
    else:
        if cur:
            cur_len += 11 + len(p)
        else:
            cur_len += len(p)
        cur.append(p)
if cur:
    chunks.append(cur)

queries=[" UNION ALL ".join(c) for c in chunks]
print('__RESULT__:')
print(json.dumps({'n_chunks': len(queries), 'first_query_len': len(queries[0]) if queries else 0, 'first_query': queries[0][:500]}))"""

env_args = {'var_call_VGVpI3kO5XpwoFYTl8XTVeJE': 'file_storage/call_VGVpI3kO5XpwoFYTl8XTVeJE.json', 'var_call_JIIwmBkuzTk3s1YN9hLJvjTA': 'file_storage/call_JIIwmBkuzTk3s1YN9hLJvjTA.json', 'var_call_V8MhUQLNeBGUkhoLUHUtY1KW': {'n': 1435}, 'var_call_RwtnADUHw7UHekN3VQmAj6qL': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_tMvtkwNUD4qPnebzX6FZXcPl': 'file_storage/call_tMvtkwNUD4qPnebzX6FZXcPl.json', 'var_call_SHDdrZidyTVCLBbYlkxeT7Vz': 'file_storage/call_SHDdrZidyTVCLBbYlkxeT7Vz.json'}

exec(code, env_args)
