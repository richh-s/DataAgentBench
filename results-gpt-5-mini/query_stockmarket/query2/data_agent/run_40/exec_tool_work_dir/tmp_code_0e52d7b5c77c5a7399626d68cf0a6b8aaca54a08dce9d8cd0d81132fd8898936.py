code = """import json
with open(var_call_vOvpTPTh22GcZEIT2EmmuKDH, 'r') as f:
    data = json.load(f)
symbols = data.get('symbols_in_trade_db', [])
selects = []
for s in symbols:
    sel = 'SELECT "{sym}" AS Symbol FROM "{sym}" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' AND "Adj Close" > 200 LIMIT 1'.format(sym=s)
    selects.append(sel)
if selects:
    sql = '\nUNION ALL\n'.join(selects)
    sql = 'SELECT DISTINCT Symbol FROM (\n' + sql + '\n) as t;'
else:
    sql = 'SELECT DISTINCT NULL AS Symbol WHERE false;'

output = {'sql': sql, 'symbols_checked': len(symbols)}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_Xbn6LlMeaJI4TuDuO6U1lrKA': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_call_uujsuC1CCLMoXiLygvLHw84R': 'file_storage/call_uujsuC1CCLMoXiLygvLHw84R.json', 'var_call_NMGGKIDoDKAikS77E1C3am3R': 'file_storage/call_NMGGKIDoDKAikS77E1C3am3R.json', 'var_call_vOvpTPTh22GcZEIT2EmmuKDH': 'file_storage/call_vOvpTPTh22GcZEIT2EmmuKDH.json', 'var_call_uliy6p2kjUKT69HBvTrOr4xu': {'sql': None}}

exec(code, env_args)
