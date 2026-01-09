code = """import json

with open(var_call_SHDdrZidyTVCLBbYlkxeT7Vz,'r') as f:
    syms = json.load(f)['symbols']

dq = chr(34)
maxlen = 600000
chunks=[]
cur_parts=[]
cur_len=0
for s in syms:
    part = "SELECT '"+s+"' AS symbol, MAX("+dq+"Adj Close"+dq+") AS max_adj_close FROM "+dq+s+dq+" WHERE Date BETWEEN '2015-01-01' AND '2015-12-31'"
    add_len = len(part) + (11 if cur_parts else 0)
    if cur_parts and cur_len + add_len > maxlen:
        chunks.append(' UNION ALL '.join(cur_parts))
        cur_parts=[part]
        cur_len=len(part)
    else:
        if cur_parts:
            cur_len += 11 + len(part)
        else:
            cur_len += len(part)
        cur_parts.append(part)
if cur_parts:
    chunks.append(' UNION ALL '.join(cur_parts))

print('__RESULT__:')
print(json.dumps({'n_chunks': len(chunks), 'chunk_lens': [len(c) for c in chunks[:5]], 'total_syms': len(syms)}))"""

env_args = {'var_call_VGVpI3kO5XpwoFYTl8XTVeJE': 'file_storage/call_VGVpI3kO5XpwoFYTl8XTVeJE.json', 'var_call_JIIwmBkuzTk3s1YN9hLJvjTA': 'file_storage/call_JIIwmBkuzTk3s1YN9hLJvjTA.json', 'var_call_V8MhUQLNeBGUkhoLUHUtY1KW': {'n': 1435}, 'var_call_RwtnADUHw7UHekN3VQmAj6qL': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_tMvtkwNUD4qPnebzX6FZXcPl': 'file_storage/call_tMvtkwNUD4qPnebzX6FZXcPl.json', 'var_call_SHDdrZidyTVCLBbYlkxeT7Vz': 'file_storage/call_SHDdrZidyTVCLBbYlkxeT7Vz.json', 'var_call_Kf4HV43niPB26ReZBA5MpBcz': {'ok': True, 'x': 1}, 'var_call_u9MiIY3VUbNHTJe067dzeivO': [], 'var_call_Gv30R8ddPYnNpC8RXodyRh7w': [{'max_adj_close': '193.5270538330078'}], 'var_call_e63LRGc3ZRfhnrY67xTxEWey': [{'max_adj_close': '193.3121490478516'}], 'var_call_2ADN27QAJ1R7u2nOBCtER1ap': {'query_len': 3502, 'n_syms': 400, 'query_preview': "WITH sym(symbol) AS (VALUES ('AAAU'),('AADR'),('ABEQ'),('ACSG'),('ACWF'),('AFK'),('AFLG'),('AFMC'),('AFSM'),('AFTY'),('AGG'),('AGGP'),('AGGY'),('AGQ'),('AGZ'),('AIEQ'),('AIIQ'),('AMLP'),('AMOM'),('AMZ"}, 'var_call_AfjIuL7m6Y034hFuNfm4o97I': {'len': 6463, 'preview': 'SELECT \'AAAU\' AS symbol, MAX("Adj Close") AS max_adj_close FROM "AAAU" WHERE Date BETWEEN \'2015-01-01\' AND \'2015-12-31\' UNION ALL SELECT \'AADR\' AS symbol, MAX("Adj Close") AS max_adj_close FROM "AADR" WHERE Date BETWEEN \'2015-01-01\' AND \'2015-12-31\' UNION ALL SELECT \'ABEQ\' AS symbol, MAX("Adj Close"'}, 'var_call_qy4aHgHDa6rPfk0Qg7Z0STWY': [{'symbol': 'AAAU', 'max_adj_close': 'nan'}, {'symbol': 'AADR', 'max_adj_close': '39.58057403564453'}, {'symbol': 'ABEQ', 'max_adj_close': 'nan'}]}

exec(code, env_args)
