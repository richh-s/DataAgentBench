code = """import json
with open(var_call_YAmGc7SHT2zMzksFygYdnQRl, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_cDQEaKskDLs8TaPk1lEF91pz, 'r') as f:
    trade_tables = json.load(f)
trade_set = set(trade_tables)
symbols = []
mapping = {}
for rec in stockinfo:
    sym = rec.get('Symbol')
    if sym in trade_set:
        symbols.append(sym)
        mapping[sym] = rec.get('Company Description')
# Build union queries safely using format with single-quoted Python strings
union_queries = []
for s in symbols:
    q = 'SELECT "{sym}" AS symbol, SUM(CASE WHEN "Close">"Open" THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN "Close"<"Open" THEN 1 ELSE 0 END) AS down_days FROM "{sym}" WHERE "Date" LIKE "2017-%"'.format(sym=s)
    union_queries.append(q)
full_sql = 'WITH counts AS (\n' + '\nUNION ALL\n'.join(union_queries) + '\n)\nSELECT symbol, up_days, down_days FROM counts WHERE up_days > down_days ORDER BY up_days DESC LIMIT 5;'
result = {'sql': full_sql, 'mapping_sample_count': len(mapping)}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YAmGc7SHT2zMzksFygYdnQRl': 'file_storage/call_YAmGc7SHT2zMzksFygYdnQRl.json', 'var_call_cDQEaKskDLs8TaPk1lEF91pz': 'file_storage/call_cDQEaKskDLs8TaPk1lEF91pz.json'}

exec(code, env_args)
