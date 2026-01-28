code = """import json
# Read symbols mapping from previous step
with open(var_call_CS6mbDQaTBWaHXltXPXrtA1x, 'r') as f:
    data = json.load(f)
symbols = data.get('symbols', [])
# Create batch SQLs
batch_size = 100
sqls = []
for i in range(0, len(symbols), batch_size):
    batch = symbols[i:i+batch_size]
    parts = []
    for s in batch:
        parts.append("SELECT '{}' AS symbol, SUM(CASE WHEN \"Close\" > \"Open\" THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN \"Close\" < \"Open\" THEN 1 ELSE 0 END) AS down_days FROM \"{}\" WHERE \"Date\" >= '2017-01-01' AND \"Date\" <= '2017-12-31'".format(s, s))
    union = "\nUNION ALL\n".join(parts)
    sql = "SELECT symbol, up_days, down_days FROM (\n" + union + "\n) as t;"
    sqls.append(sql)
# Output list
print('__RESULT__:')
print(json.dumps({'sqls': sqls}))"""

env_args = {'var_call_bYQyMqrBbLBPnHo5oOIwzCIP': ['stockinfo'], 'var_call_Js61eKeKPd8pJkBCv55jt5nu': 'file_storage/call_Js61eKeKPd8pJkBCv55jt5nu.json', 'var_call_LbZzmGVobT3Mgm9lwFj5SNHc': 'file_storage/call_LbZzmGVobT3Mgm9lwFj5SNHc.json', 'var_call_CS6mbDQaTBWaHXltXPXrtA1x': 'file_storage/call_CS6mbDQaTBWaHXltXPXrtA1x.json'}

exec(code, env_args)
