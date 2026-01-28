code = """import json
with open(var_call_tItXDldGr2benyc4Ud9wMyCQ, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_3GqfoyPVmTjGEwRIfI1A6U1V, 'r') as f:
    tables = json.load(f)

s_symbols = [entry['Symbol'] for entry in stockinfo]
tables_set = set(tables)
symbols = [s for s in s_symbols if s in tables_set]

selects = []
for s in symbols:
    t = s.replace('"', '""')
    sel = "SELECT '%s' AS symbol, SUM(CASE WHEN \"High\" > 1.2 * \"Low\" AND \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31' THEN 1 ELSE 0 END) AS cnt FROM \"%s\"" % (s, t)
    selects.append(sel)

if selects:
    sql = " UNION ALL ".join(selects) + " ORDER BY cnt DESC LIMIT 5;"
else:
    sql = ""

print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_tItXDldGr2benyc4Ud9wMyCQ': 'file_storage/call_tItXDldGr2benyc4Ud9wMyCQ.json', 'var_call_3GqfoyPVmTjGEwRIfI1A6U1V': 'file_storage/call_3GqfoyPVmTjGEwRIfI1A6U1V.json'}

exec(code, env_args)
