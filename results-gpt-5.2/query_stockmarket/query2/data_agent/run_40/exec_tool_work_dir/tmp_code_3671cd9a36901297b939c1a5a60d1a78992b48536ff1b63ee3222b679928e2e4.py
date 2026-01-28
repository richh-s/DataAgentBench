code = """import json
si = var_call_kfHBO7fB9JYYhZvzLMNf8cEY
if isinstance(si, str):
    si = json.load(open(si,'r'))
si_syms = [r['symbol'] for r in si]

tb = var_call_pYXepvhMgzA5lKnYX96wSRqh
if isinstance(tb, str):
    tb = json.load(open(tb,'r'))
trade_tables = set(tb)

syms = sorted(set(si_syms).intersection(trade_tables))

# chunk symbols to keep query size manageable
chunks = [syms[i:i+150] for i in range(0, len(syms), 150)]

queries = []
for ch in chunks:
    parts = []
    for s in ch:
        s_tbl = s.replace('"','""')
        s_lit = s.replace("'","''")
        parts.append("SELECT '" + s_lit + "' AS symbol, MAX(\"Adj Close\")::DOUBLE AS max_adj_close FROM \"" + s_tbl + "\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")
    queries.append(" UNION ALL ".join(parts))

print('__RESULT__:')
print(json.dumps({'n_chunks': len(queries), 'first_query_len': len(queries[0]), 'first_query_preview': queries[0][:500]}))"""

env_args = {'var_call_kfHBO7fB9JYYhZvzLMNf8cEY': 'file_storage/call_kfHBO7fB9JYYhZvzLMNf8cEY.json', 'var_call_pYXepvhMgzA5lKnYX96wSRqh': 'file_storage/call_pYXepvhMgzA5lKnYX96wSRqh.json', 'var_call_GwP5dDV6zuuPNMcKHakMiYuN': 'ok', 'var_call_bStrsD1YHhdlyKCYeeVmWK68': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_HRcGJ6Bu1w2ayj6dLUTrDyfU': {'n_syms': 1435, 'symbols_preview': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_call_R7p3arVKg6E2CIlc3Fsag4KJ': [{'symbol': 'SPY', 'max_adj_close': '193.3121490478516'}]}

exec(code, env_args)
