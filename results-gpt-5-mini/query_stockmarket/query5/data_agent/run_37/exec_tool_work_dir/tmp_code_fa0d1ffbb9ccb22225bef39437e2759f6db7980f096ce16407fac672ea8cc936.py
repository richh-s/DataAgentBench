code = """import json
with open(var_call_VqxF3xG5XGRmxZHnEI5CHGMJ, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_sOBRWuxkOyvJlDzcPXen5MsU, 'r') as f:
    trade_tables = json.load(f)

symbol_to_company = {rec['Symbol'].upper(): rec.get('Company Description','') for rec in stockinfo}
trade_set = set([t.upper() for t in trade_tables])
symbols = sorted([s for s in symbol_to_company.keys() if s in trade_set])

parts = []
for s in symbols:
    part = "SELECT '" + s + "' AS Symbol, COUNT(*) AS cnt FROM " + chr(34) + s + chr(34) + " WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND ((High - Low) > 0.2 * Low)"
    parts.append(part)

if parts:
    union_all = ' UNION ALL '.join(parts)
    full_sql = 'SELECT Symbol, cnt FROM (' + union_all + ') ORDER BY cnt DESC LIMIT 5;'
else:
    full_sql = ''

result = {'sql': full_sql, 'num_symbols': len(symbols)}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_VqxF3xG5XGRmxZHnEI5CHGMJ': 'file_storage/call_VqxF3xG5XGRmxZHnEI5CHGMJ.json', 'var_call_sOBRWuxkOyvJlDzcPXen5MsU': 'file_storage/call_sOBRWuxkOyvJlDzcPXen5MsU.json'}

exec(code, env_args)
