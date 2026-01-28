code = """import json
with open(var_call_E5c2YY2Csym0kXhekfXRBlVX, 'r') as f:
    data = json.load(f)
symbols = [rec['Symbol'] for rec in data]
parts = []
for s in symbols:
    table = chr(34) + s + chr(34)
    # build condition without escaping quotes by using single quotes for SQL literals
    part = "SELECT '" + s + "' AS symbol, COUNT(*) AS cnt FROM " + table + " WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (\"High\" - \"Low\") > 0.2 * \"Low\""
    parts.append(part)
if parts:
    unions = ' UNION ALL '.join(parts)
    sql = 'SELECT symbol, cnt FROM ( ' + unions + ' ) AS t ORDER BY cnt DESC LIMIT 1000;'
else:
    sql = "SELECT NULL as symbol, 0 as cnt WHERE 1=0;"
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_wEEkxu0dysYgfB649IqQvJ1V': 'file_storage/call_wEEkxu0dysYgfB649IqQvJ1V.json', 'var_call_fNX066P2IyOjKzz9kLNIrdpe': 'file_storage/call_fNX066P2IyOjKzz9kLNIrdpe.json', 'var_call_E5c2YY2Csym0kXhekfXRBlVX': 'file_storage/call_E5c2YY2Csym0kXhekfXRBlVX.json'}

exec(code, env_args)
