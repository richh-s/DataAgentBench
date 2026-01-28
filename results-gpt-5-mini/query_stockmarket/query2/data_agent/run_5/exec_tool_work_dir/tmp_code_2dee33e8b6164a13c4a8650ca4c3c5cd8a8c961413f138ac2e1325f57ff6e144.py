code = """import json
with open(var_call_svQsBvucK6HUwI89ycJ6EqMt, 'r') as f:
    symbols = json.load(f)
symbols = sorted(list(dict.fromkeys(symbols)))
batch_size = 200
queries = []
for i in range(0, len(symbols), batch_size):
    batch = symbols[i:i+batch_size]
    parts = []
    for s in batch:
        tbl = chr(34) + s + chr(34)
        col = chr(34) + 'Adj Close' + chr(34)
        part = "SELECT '{sym}' AS Symbol, MAX({col}) AS max_adj FROM {tbl} WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(sym=s, col=col, tbl=tbl)
        parts.append(part)
    query = ' \nUNION ALL\n '.join(parts) + ';'
    queries.append(query)
print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_call_sivacHuiSgcyyLES4JY2Pmbh': 'file_storage/call_sivacHuiSgcyyLES4JY2Pmbh.json', 'var_call_8wxgRA4ankapzlMw4DhePGJj': 'file_storage/call_8wxgRA4ankapzlMw4DhePGJj.json', 'var_call_GM4b9XWbZdjPKEghYXIfgFyD': {'has_SPY': True, 'total_etfs': 1435}, 'var_call_svQsBvucK6HUwI89ycJ6EqMt': 'file_storage/call_svQsBvucK6HUwI89ycJ6EqMt.json', 'var_call_2oMOmlZNivM6PlBm9Di2B1Cz': [], 'var_call_vnuNeODHxnkNI6xdxOSx0DKI': [{'max_adj': '193.3121490478516'}]}

exec(code, env_args)
