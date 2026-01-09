code = """import json

si = var_call_kfHBO7fB9JYYhZvzLMNf8cEY
if isinstance(si, str):
    with open(si, 'r') as f:
        si = json.load(f)
si_syms = [r['symbol'] for r in si]

tb = var_call_pYXepvhMgzA5lKnYX96wSRqh
if isinstance(tb, str):
    with open(tb, 'r') as f:
        tb = json.load(f)
trade_tables = set(tb)

syms = sorted(set(si_syms).intersection(trade_tables))

parts = []
for s in syms:
    parts.append("SELECT '{sym}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{sym}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(sym=s.replace("'","''")))

query = " UNION ALL ".join(parts) if parts else "SELECT NULL AS symbol, NULL AS max_adj_close WHERE FALSE"

out = json.dumps({"symbols": syms, "union_query": query})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_kfHBO7fB9JYYhZvzLMNf8cEY': 'file_storage/call_kfHBO7fB9JYYhZvzLMNf8cEY.json', 'var_call_pYXepvhMgzA5lKnYX96wSRqh': 'file_storage/call_pYXepvhMgzA5lKnYX96wSRqh.json'}

exec(code, env_args)
