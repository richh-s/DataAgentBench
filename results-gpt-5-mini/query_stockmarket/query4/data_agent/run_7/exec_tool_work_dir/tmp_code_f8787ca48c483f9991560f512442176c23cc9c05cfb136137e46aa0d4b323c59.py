code = """import json
p = var_call_qO5UOjJhgUd3ljUq9Cpo6Q7e
with open(p, 'r') as f:
    data = json.load(f)
symbols = [rec['Symbol'] for rec in data]
parts = []
for s in symbols:
    # escape double quotes in table name by wrapping in double quotes
    part = ("SELECT '{}' as symbol, SUM(CASE WHEN \"Close\">\"Open\" AND \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31' THEN 1 ELSE 0 END) as up_days, "
            "SUM(CASE WHEN \"Close\"<\"Open\" AND \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31' THEN 1 ELSE 0 END) as down_days FROM \"{}\"").format(s, s)
    parts.append(part)
sql = ' UNION ALL '.join(parts)
# print result JSON string
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_NOrOeolxry3KNh5kwmiCZwYH': 'file_storage/call_NOrOeolxry3KNh5kwmiCZwYH.json', 'var_call_mt89zRyxGP2HAtEkz4Dmna3z': 'file_storage/call_mt89zRyxGP2HAtEkz4Dmna3z.json', 'var_call_qO5UOjJhgUd3ljUq9Cpo6Q7e': 'file_storage/call_qO5UOjJhgUd3ljUq9Cpo6Q7e.json', 'var_call_pzgIXutuSg5PSbl8pUosa5yX': {'count': 234, 'first10': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}}

exec(code, env_args)
