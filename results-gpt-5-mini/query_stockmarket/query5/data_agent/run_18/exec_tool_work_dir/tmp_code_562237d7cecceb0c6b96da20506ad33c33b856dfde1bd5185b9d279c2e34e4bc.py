code = """import json
with open(var_call_p3wehT7WbD92Ab0NJaPpAfGD, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_Brv828NQIaemUxAB6OfCNpOc, 'r') as f:
    trade_tables = json.load(f)
mapping = {item['Symbol']: item.get('Company Description','') for item in stockinfo}
symbols = [s for s in mapping.keys() if s in trade_tables]
parts = []
for sym in symbols:
    part = "SELECT '{}' AS symbol, COUNT(*) AS cnt FROM \"{}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (\"High\" - \"Low\") > 0.2 * \"Low\"".format(sym, sym)
    parts.append(part)
if parts:
    sql = ' UNION ALL '.join(parts) + ' ORDER BY cnt DESC LIMIT 5;'
else:
    sql = ''
output = {'sql': sql, 'symbols_count': len(symbols)}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_p3wehT7WbD92Ab0NJaPpAfGD': 'file_storage/call_p3wehT7WbD92Ab0NJaPpAfGD.json', 'var_call_Brv828NQIaemUxAB6OfCNpOc': 'file_storage/call_Brv828NQIaemUxAB6OfCNpOc.json'}

exec(code, env_args)
