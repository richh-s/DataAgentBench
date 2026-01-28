code = """import json
with open(var_call_YAmGc7SHT2zMzksFygYdnQRl, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_cDQEaKskDLs8TaPk1lEF91pz, 'r') as f:
    trade_tables = json.load(f)
trade_set = set(trade_tables)
symbols = [rec['Symbol'] for rec in stockinfo if rec['Symbol'] in trade_set]
mapping = {rec['Symbol']: rec['Company Description'] for rec in stockinfo if rec['Symbol'] in trade_set}
parts = []
for s in symbols:
    part = '''SELECT '{}' AS symbol, SUM(CASE WHEN "Close">"Open" THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN "Close"<"Open" THEN 1 ELSE 0 END) AS down_days FROM "{}" WHERE "Date" LIKE '2017-%' '''.format(s, s)
    parts.append(part)
full_sql = 'WITH counts AS (\n' + '\nUNION ALL\n'.join(parts) + '\n)\nSELECT symbol, up_days, down_days FROM counts WHERE up_days > down_days ORDER BY up_days DESC LIMIT 5;'
print('__RESULT__:')
print(json.dumps({'sql': full_sql, 'mapping_count': len(mapping)}))"""

env_args = {'var_call_YAmGc7SHT2zMzksFygYdnQRl': 'file_storage/call_YAmGc7SHT2zMzksFygYdnQRl.json', 'var_call_cDQEaKskDLs8TaPk1lEF91pz': 'file_storage/call_cDQEaKskDLs8TaPk1lEF91pz.json', 'var_call_rv7AwKhcaSbLUleltodP8ssN': {'stockinfo_count': 234, 'trade_tables_count': 2753}}

exec(code, env_args)
