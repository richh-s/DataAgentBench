code = """import json
path_tables = var_call_9EqcyJTTNqzbni5nT5m8eM89
path_stockinfo = var_call_w0BWMEldosjQXfLC7QjaVZWn

with open(path_tables, 'r') as f:
    tables = json.load(f)
with open(path_stockinfo, 'r') as f:
    stockinfo = json.load(f)

symbols_info = [rec['Symbol'] for rec in stockinfo]
available = set(tables)
# Filter symbols that are present in stocktrade database
symbols = [s for s in symbols_info if s in available]

parts = []
for s in symbols:
    part = ('''SELECT '{sym}' AS symbol, COALESCE(SUM(CASE WHEN "Close">"Open" THEN 1 ELSE 0 END),0) AS up, COALESCE(SUM(CASE WHEN "Close"<"Open" THEN 1 ELSE 0 END),0) AS down FROM "{sym}" WHERE "Date">='2017-01-01' AND "Date"<='2017-12-31' ''').format(sym=s)
    parts.append(part)

if parts:
    union_sql = '\nUNION ALL\n'.join(parts)
    sql = 'SELECT symbol, up, down FROM (\n' + union_sql + '\n) AS t WHERE up>down ORDER BY up DESC LIMIT 5;'
else:
    sql = ''

print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_ILvcekgasuDAplGbc9NsdFXR': ['stockinfo'], 'var_call_9EqcyJTTNqzbni5nT5m8eM89': 'file_storage/call_9EqcyJTTNqzbni5nT5m8eM89.json', 'var_call_w0BWMEldosjQXfLC7QjaVZWn': 'file_storage/call_w0BWMEldosjQXfLC7QjaVZWn.json'}

exec(code, env_args)
