code = """import json
with open(var_call_nELGdyvPXxMt9K3rUNiloF4h, 'r') as f:
    info = json.load(f)
with open(var_call_OxR5V4zYOQmYrDGwhBhWPqi7, 'r') as f:
    tables = json.load(f)

symbols_from_info = [rec['Symbol'] for rec in info]
tables_set = set(tables)
symbols = [s for s in symbols_from_info if s in tables_set]

select_parts = []
for s in symbols:
    part = "SELECT '{}' AS symbol, SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) AS down_days FROM \"{}\" WHERE \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31'".format(s, s)
    select_parts.append(part)

sql = " UNION ALL ".join(select_parts) + " ORDER BY up_days DESC;"

print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_nELGdyvPXxMt9K3rUNiloF4h': 'file_storage/call_nELGdyvPXxMt9K3rUNiloF4h.json', 'var_call_OxR5V4zYOQmYrDGwhBhWPqi7': 'file_storage/call_OxR5V4zYOQmYrDGwhBhWPqi7.json'}

exec(code, env_args)
