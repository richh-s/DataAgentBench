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

print('__RESULT__:')
print(json.dumps({'n_syms': len(syms), 'symbols_preview': syms[:20]}))"""

env_args = {'var_call_kfHBO7fB9JYYhZvzLMNf8cEY': 'file_storage/call_kfHBO7fB9JYYhZvzLMNf8cEY.json', 'var_call_pYXepvhMgzA5lKnYX96wSRqh': 'file_storage/call_pYXepvhMgzA5lKnYX96wSRqh.json', 'var_call_GwP5dDV6zuuPNMcKHakMiYuN': 'ok', 'var_call_bStrsD1YHhdlyKCYeeVmWK68': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}]}

exec(code, env_args)
