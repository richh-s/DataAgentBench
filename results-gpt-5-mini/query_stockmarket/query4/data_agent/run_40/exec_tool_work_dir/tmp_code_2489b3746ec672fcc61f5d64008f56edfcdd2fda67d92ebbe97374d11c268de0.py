code = """import json, os
p = var_call_Z1LS9TfnT11V5aMqhG55TyCL
if isinstance(p, str) and os.path.exists(p):
    data = json.load(open(p, 'r'))
else:
    data = p
symbols = [r['Symbol'] for r in data]
selects = []
for s in symbols:
    s_esc = s.replace('"', '""')
    sel = ("SELECT '" + s_esc + "' AS symbol, "
           "SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) AS up, "
           "SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) AS down "
           "FROM \"" + s_esc + "\" "
           "WHERE Date>='2017-01-01' AND Date<='2017-12-31'")
    selects.append(sel)
sql = "SELECT symbol, up, down, (up-down) AS diff FROM (\n" + "\nUNION ALL\n".join(selects) + "\n) AS t ORDER BY up DESC;"
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_Z1LS9TfnT11V5aMqhG55TyCL': 'file_storage/call_Z1LS9TfnT11V5aMqhG55TyCL.json'}

exec(code, env_args)
