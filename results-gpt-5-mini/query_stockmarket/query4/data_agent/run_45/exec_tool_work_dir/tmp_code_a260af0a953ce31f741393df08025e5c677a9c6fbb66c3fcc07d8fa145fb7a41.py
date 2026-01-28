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
    part = ("SELECT '" + s + "' as symbol, SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) as up_count, "
            "SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) as down_count FROM \"" + s + "\" "
            "WHERE \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31'")
    parts.append(part)
sql = ''
if parts:
    sql = ' UNION ALL '.join(parts) + ' ORDER BY up_count DESC'
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_F7ARdSLa3CfMEqYQoQGvzIcb': 'file_storage/call_F7ARdSLa3CfMEqYQoQGvzIcb.json', 'var_call_nRCOIQTKtx4ukCguggXBETaj': 'file_storage/call_nRCOIQTKtx4ukCguggXBETaj.json'}

exec(code, env_args)
