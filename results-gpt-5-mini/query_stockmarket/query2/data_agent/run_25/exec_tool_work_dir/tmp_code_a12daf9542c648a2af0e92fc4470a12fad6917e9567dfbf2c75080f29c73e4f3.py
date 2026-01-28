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
    # build SQL part: select symbol if any row in 2015 has Adj Close > 200
    part = f"SELECT '{sym}' AS symbol FROM \"{sym}\" WHERE \"Date\">='2015-01-01' AND \"Date\"<='2015-12-31' AND \"Adj Close\">200 LIMIT 1"
    parts.append(part)

sql = '\nUNION ALL\n'.join(parts) if parts else 'SELECT NULL WHERE FALSE;'

print('__RESULT__:')
print(json.dumps({'sql': sql}))"""

env_args = {'var_call_OhZ4rWYNl61yYyzGFPplZ5WS': 'file_storage/call_OhZ4rWYNl61yYyzGFPplZ5WS.json', 'var_call_KVY7N3JVPncrE5cHywJzTNjV': 'file_storage/call_KVY7N3JVPncrE5cHywJzTNjV.json', 'var_call_sioTGPnUUGRodKxjXTHYUi8A': 'file_storage/call_sioTGPnUUGRodKxjXTHYUi8A.json', 'var_call_ZEl6sq96uXMfGSAk5zHXhNa7': {'found': ['SPY', 'IVV', 'VOO', 'PRF', 'IWM', 'DIA', 'VTI', 'VOO', 'SPYG', 'GDX', 'GLD', 'XLK']}}

exec(code, env_args)
