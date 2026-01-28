code = """import json
with open(var_call_CS6mbDQaTBWaHXltXPXrtA1x, 'r') as f:
    data = json.load(f)
symbols = data.get('symbols', [])
parts = []
for s in symbols:
    parts.append('SELECT "{}" AS symbol, "Open", "Close" FROM "{}" WHERE "Date" >= \'2017-01-01\' AND "Date" <= \'2017-12-31\''.format(s, s))
union = '\nUNION ALL\n'.join(parts)
sql = (
    'SELECT symbol, SUM(CASE WHEN "Close" > "Open" THEN 1 ELSE 0 END) AS up_days, '
    'SUM(CASE WHEN "Close" < "Open" THEN 1 ELSE 0 END) AS down_days '
    'FROM (\n' + union + '\n) AS all_data '
    'GROUP BY symbol '
    'HAVING SUM(CASE WHEN "Close" > "Open" THEN 1 ELSE 0 END) > SUM(CASE WHEN "Close" < "Open" THEN 1 ELSE 0 END) '
    'ORDER BY up_days DESC '
    'LIMIT 5;'
)
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_bYQyMqrBbLBPnHo5oOIwzCIP': ['stockinfo'], 'var_call_Js61eKeKPd8pJkBCv55jt5nu': 'file_storage/call_Js61eKeKPd8pJkBCv55jt5nu.json', 'var_call_LbZzmGVobT3Mgm9lwFj5SNHc': 'file_storage/call_LbZzmGVobT3Mgm9lwFj5SNHc.json', 'var_call_CS6mbDQaTBWaHXltXPXrtA1x': 'file_storage/call_CS6mbDQaTBWaHXltXPXrtA1x.json'}

exec(code, env_args)
