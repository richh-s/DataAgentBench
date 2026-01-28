code = """import json
# load filtered stockinfo rows file path
path = var_call_oYATr3lACqKv3d9bwO11EIgq
with open(path, 'r') as f:
    rows = json.load(f)
symbols = [r['Symbol'] for r in rows]
# build union parts
parts = []
for s in symbols:
    part = "SELECT '{sym}' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down FROM \"{sym}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'".format(sym=s)
    parts.append(part)
if not parts:
    sql = ''
else:
    sql = 'SELECT symbol, up, down FROM (' + ' UNION ALL '.join(parts) + ') WHERE up > down ORDER BY (up - down) DESC LIMIT 5;'
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_mf8p8wR7qUDwPcMyViiKZp7a': 'file_storage/call_mf8p8wR7qUDwPcMyViiKZp7a.json', 'var_call_wsVInw8eEyMzIoSnAVX55pOn': 'file_storage/call_wsVInw8eEyMzIoSnAVX55pOn.json', 'var_call_atY7Z5oy1ePQMP8fS8SVojO2': {'a': 'ok'}, 'var_call_oYATr3lACqKv3d9bwO11EIgq': 'file_storage/call_oYATr3lACqKv3d9bwO11EIgq.json'}

exec(code, env_args)
