code = """import json
syms = ['AAAU','AADR']
chunks = [syms]
queries = []
for ch in chunks:
    parts = []
    for s in ch:
        parts.append("SELECT '" + s + "' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"" + s + "\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")
    queries.append(' UNION ALL '.join(parts))
print('__RESULT__:')
print(json.dumps({'q': queries[0]}))"""

env_args = {'var_call_SobbbbZXILGybWnUoxXTVWWx': 'file_storage/call_SobbbbZXILGybWnUoxXTVWWx.json', 'var_call_QhxtRLpkISLHodfoZTe1ZO6J': 'file_storage/call_QhxtRLpkISLHodfoZTe1ZO6J.json', 'var_call_bCxE0YzOOU4Jp5szkT8hBUtj': {'x': 1}, 'var_call_B75OzIt1OZFzYxN2Hnlm9WQZ': {'n_etf_syms': 1435, 'n_trade_tables': 2753, 'n_syms_intersection': 1435, 'first10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}}

exec(code, env_args)
