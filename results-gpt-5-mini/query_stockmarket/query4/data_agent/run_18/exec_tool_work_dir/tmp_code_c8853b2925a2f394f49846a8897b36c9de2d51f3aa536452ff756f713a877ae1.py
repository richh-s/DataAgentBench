code = """import json
pt = var_call_9EqcyJTTNqzbni5nT5m8eM89
pinfo = var_call_w0BWMEldosjQXfLC7QjaVZWn
with open(pt) as f:
    tables = json.load(f)
with open(pinfo) as f:
    stockinfo = json.load(f)

symbols = [rec['Symbol'] for rec in stockinfo if rec['Symbol'] in tables]
parts = []
for s in symbols:
    part = (
        "SELECT '{s}' AS symbol, COALESCE(SUM(CASE WHEN "
        + '"Close"' + ">" + '"Open"' + " THEN 1 ELSE 0 END),0) AS up, "
        + "COALESCE(SUM(CASE WHEN " + '"Close"' + "<" + '"Open"' + " THEN 1 ELSE 0 END),0) AS down "
        + "FROM " + '"' + s + '"' + " WHERE " + '"Date"' + ">='2017-01-01' AND " + '"Date"' + "<='2017-12-31'"
    ).format(s=s)
    parts.append(part)
if parts:
    sql = "SELECT symbol, up, down FROM (\n" + "\nUNION ALL\n".join(parts) + "\n) AS t WHERE up>down ORDER BY up DESC LIMIT 5;"
else:
    sql = ""
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_ILvcekgasuDAplGbc9NsdFXR': ['stockinfo'], 'var_call_9EqcyJTTNqzbni5nT5m8eM89': 'file_storage/call_9EqcyJTTNqzbni5nT5m8eM89.json', 'var_call_w0BWMEldosjQXfLC7QjaVZWn': 'file_storage/call_w0BWMEldosjQXfLC7QjaVZWn.json'}

exec(code, env_args)
