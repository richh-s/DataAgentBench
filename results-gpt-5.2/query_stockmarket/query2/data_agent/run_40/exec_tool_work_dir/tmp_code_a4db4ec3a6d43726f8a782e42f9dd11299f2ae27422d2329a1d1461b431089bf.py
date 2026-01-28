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

parts = []
for s in syms:
    s2 = s.replace('"','""')
    parts.append("SELECT '" + s.replace("'","''") + "' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"" + s2 + "\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")

query = " UNION ALL ".join(parts) if parts else "SELECT NULL AS symbol, NULL AS max_adj_close WHERE FALSE"

print('__RESULT__:')
print(json.dumps({'symbols': syms, 'union_query': query}))"""

env_args = {'var_call_kfHBO7fB9JYYhZvzLMNf8cEY': 'file_storage/call_kfHBO7fB9JYYhZvzLMNf8cEY.json', 'var_call_pYXepvhMgzA5lKnYX96wSRqh': 'file_storage/call_pYXepvhMgzA5lKnYX96wSRqh.json'}

exec(code, env_args)
