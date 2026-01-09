code = """import json

src = var_call_tBV3GJDNoaydc95nVxMZLmQP
if isinstance(src, str):
    with open(src, 'r') as f:
        data = json.load(f)
else:
    data = src
symbols = data['symbols']

parts = []
for s in symbols:
    part = 'SELECT \'{sym}\' AS symbol, ' \
           'SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, ' \
           'SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days ' \
           'FROM "{sym}" ' \
           "WHERE Date >= '2017-01-01' AND Date < '2018-01-01'".format(sym=s)
    parts.append(part)

sql = '\nUNION ALL\n'.join(parts)
print('__RESULT__:')
print(json.dumps({'sql': sql}))"""

env_args = {'var_call_Ccu3gVLBYmt6aODTNoRLYShv': 'file_storage/call_Ccu3gVLBYmt6aODTNoRLYShv.json', 'var_call_Vuu3fiiPc3q8j0Wv61fKeY8b': 'file_storage/call_Vuu3fiiPc3q8j0Wv61fKeY8b.json', 'var_call_tBV3GJDNoaydc95nVxMZLmQP': 'file_storage/call_tBV3GJDNoaydc95nVxMZLmQP.json'}

exec(code, env_args)
