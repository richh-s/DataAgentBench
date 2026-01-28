code = """import json
p = var_call_yu2THRxExb7QIgtsCuXUShDA
with open(p) as f:
    data = json.load(f)
symbols = data['symbols']
parts = []
# template uses double quotes for column names and table quoting
template = '''SELECT '{sym}' AS symbol, SUM(CASE WHEN ("High" - "Low") > 0.2 * "Low" THEN 1 ELSE 0 END) AS cnt FROM "{sym}" WHERE "Date" >= '2019-01-01' AND "Date" <= '2019-12-31' '''
for s in symbols:
    parts.append(template.format(sym=s))
sql = "\nUNION ALL\n".join(parts)
sql = "SELECT symbol, cnt FROM (\n" + sql + "\n) ORDER BY cnt DESC LIMIT 5;"
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_h4lURv0gsFsNbbGeJpA93oUb': 'file_storage/call_h4lURv0gsFsNbbGeJpA93oUb.json', 'var_call_wrrVFEISzbCFFa5DhbWeDDsL': 'file_storage/call_wrrVFEISzbCFFa5DhbWeDDsL.json', 'var_call_yu2THRxExb7QIgtsCuXUShDA': 'file_storage/call_yu2THRxExb7QIgtsCuXUShDA.json'}

exec(code, env_args)
