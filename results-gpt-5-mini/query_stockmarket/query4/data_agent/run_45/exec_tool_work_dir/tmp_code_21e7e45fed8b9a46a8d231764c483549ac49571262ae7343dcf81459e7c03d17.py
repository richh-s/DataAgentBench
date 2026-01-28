code = """import json
p1 = var_call_F7ARdSLa3CfMEqYQoQGvzIcb
p2 = var_call_nRCOIQTKtx4ukCguggXBETaj
with open(p1,'r') as f:
    data1 = json.load(f)
with open(p2,'r') as f:
    tables = json.load(f)
symbols = [rec['Symbol'] for rec in data1]
present = [s for s in symbols if s in tables]
parts = []
for s in present:
    part = (
        "SELECT '" + s + "' as symbol, SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) as up_count, "
        "SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) as down_count FROM \"" + s + "\" "
        "WHERE \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31'")
    parts.append(part)
if not parts:
    union_sql = ''
else:
    union_sql = ' UNION ALL '.join(parts)
final_sql = 'SELECT symbol, up_count, down_count FROM (' + union_sql + ') as t WHERE up_count>down_count ORDER BY up_count DESC LIMIT 5;'
print('__RESULT__:')
print(json.dumps(final_sql))"""

env_args = {'var_call_F7ARdSLa3CfMEqYQoQGvzIcb': 'file_storage/call_F7ARdSLa3CfMEqYQoQGvzIcb.json', 'var_call_nRCOIQTKtx4ukCguggXBETaj': 'file_storage/call_nRCOIQTKtx4ukCguggXBETaj.json', 'var_call_iiVxyEpARj5wqd3glSsWLWmq': {'symbols_in_stockinfo': 234, 'tables_in_stocktrade': 2753}, 'var_call_cV4zh4nKX1ldk88sDJmyrQHs': {'symbols_present_count': 234, 'sample_present': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}}

exec(code, env_args)
