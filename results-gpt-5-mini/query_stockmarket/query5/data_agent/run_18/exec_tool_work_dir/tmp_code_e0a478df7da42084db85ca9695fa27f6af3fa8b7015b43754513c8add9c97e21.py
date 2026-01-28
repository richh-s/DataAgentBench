code = """import json
# load previous query results using provided variable names
with open(var_call_p3wehT7WbD92Ab0NJaPpAfGD, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_Brv828NQIaemUxAB6OfCNpOc, 'r') as f:
    trade_tables = json.load(f)
# build mapping for Market Category S and non-ETF
mapping = {item['Symbol']: item.get('Company Description','') for item in stockinfo if item.get('Market Category')=='S' and (item.get('ETF') is None or item.get('ETF')!='Y')}
# filter symbols present in trade_tables
symbols = sorted([s for s in mapping.keys() if s in trade_tables])
parts = []
for sym in symbols:
    parts.append("SELECT '{}' AS symbol, COUNT(*) AS cnt FROM \"{}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.2 * Low".format(sym, sym))
if parts:
    sql = ' UNION ALL '.join(parts) + ' ORDER BY cnt DESC LIMIT 5;'
else:
    sql = ''
print('__RESULT__:')
print(json.dumps({'sql': sql, 'symbols_count': len(symbols)}))"""

env_args = {'var_call_p3wehT7WbD92Ab0NJaPpAfGD': 'file_storage/call_p3wehT7WbD92Ab0NJaPpAfGD.json', 'var_call_Brv828NQIaemUxAB6OfCNpOc': 'file_storage/call_Brv828NQIaemUxAB6OfCNpOc.json', 'var_call_vXJROydgUZN5l3qOIPDotLEG': ['file_storage/call_p3wehT7WbD92Ab0NJaPpAfGD.json', 'file_storage/call_Brv828NQIaemUxAB6OfCNpOc.json'], 'var_call_4pFubIUX5q0Q89bAK3ZRLwOH': {'symbols_sample': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX'], 'symbols_count': 86}}

exec(code, env_args)
