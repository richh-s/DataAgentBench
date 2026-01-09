code = """import json

with open(var_call_SHDdrZidyTVCLBbYlkxeT7Vz,'r') as f:
    syms = json.load(f)['symbols']
syms = syms[:50]

parts = []
for s in syms:
    parts.append("SELECT '"+s+"' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \""+s+"\" WHERE Date BETWEEN '2015-01-01' AND '2015-12-31'")
q = " UNION ALL ".join(parts)
print('__RESULT__:')
print(json.dumps({'len': len(q), 'preview': q[:300]}))"""

env_args = {'var_call_VGVpI3kO5XpwoFYTl8XTVeJE': 'file_storage/call_VGVpI3kO5XpwoFYTl8XTVeJE.json', 'var_call_JIIwmBkuzTk3s1YN9hLJvjTA': 'file_storage/call_JIIwmBkuzTk3s1YN9hLJvjTA.json', 'var_call_V8MhUQLNeBGUkhoLUHUtY1KW': {'n': 1435}, 'var_call_RwtnADUHw7UHekN3VQmAj6qL': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_tMvtkwNUD4qPnebzX6FZXcPl': 'file_storage/call_tMvtkwNUD4qPnebzX6FZXcPl.json', 'var_call_SHDdrZidyTVCLBbYlkxeT7Vz': 'file_storage/call_SHDdrZidyTVCLBbYlkxeT7Vz.json', 'var_call_Kf4HV43niPB26ReZBA5MpBcz': {'ok': True, 'x': 1}, 'var_call_u9MiIY3VUbNHTJe067dzeivO': [], 'var_call_Gv30R8ddPYnNpC8RXodyRh7w': [{'max_adj_close': '193.5270538330078'}], 'var_call_e63LRGc3ZRfhnrY67xTxEWey': [{'max_adj_close': '193.3121490478516'}], 'var_call_2ADN27QAJ1R7u2nOBCtER1ap': {'query_len': 3502, 'n_syms': 400, 'query_preview': "WITH sym(symbol) AS (VALUES ('AAAU'),('AADR'),('ABEQ'),('ACSG'),('ACWF'),('AFK'),('AFLG'),('AFMC'),('AFSM'),('AFTY'),('AGG'),('AGGP'),('AGGY'),('AGQ'),('AGZ'),('AIEQ'),('AIIQ'),('AMLP'),('AMOM'),('AMZ"}}

exec(code, env_args)
