code = """import json
v = var_call_sioTGPnUUGRodKxjXTHYUi8A
if isinstance(v, str):
    with open(v, 'r') as f:
        data = json.load(f)
else:
    data = v
symbols = data.get('symbols', [])
parts = []
for sym in symbols:
    parts.append("SELECT " + repr(sym) + " AS symbol FROM " + '"' + sym + '"' + " WHERE " + '"Date"' + " >= " + repr('2015-01-01') + " AND " + '"Date"' + " <= " + repr('2015-12-31') + " AND " + '"Adj Close"' + " > 200 LIMIT 1")
sql = "\nUNION ALL\n".join(parts) if parts else "SELECT NULL WHERE FALSE;"
print('__RESULT__:')
print(json.dumps({"sql": sql}))"""

env_args = {'var_call_OhZ4rWYNl61yYyzGFPplZ5WS': 'file_storage/call_OhZ4rWYNl61yYyzGFPplZ5WS.json', 'var_call_KVY7N3JVPncrE5cHywJzTNjV': 'file_storage/call_KVY7N3JVPncrE5cHywJzTNjV.json', 'var_call_sioTGPnUUGRodKxjXTHYUi8A': 'file_storage/call_sioTGPnUUGRodKxjXTHYUi8A.json'}

exec(code, env_args)
