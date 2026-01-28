code = """import json
p = var_call_yu2THRxExb7QIgtsCuXUShDA
with open(p, 'r') as f:
    data = json.load(f)
symbols = data['symbols']

dq = chr(34)
parts = []
for s in symbols:
    part = (
        "SELECT '" + s + "' AS symbol, SUM(CASE WHEN (" + dq + "High" + dq + " - " + dq + "Low" + dq + ") > 0.2 * " + dq + "Low" + dq + " THEN 1 ELSE 0 END) AS cnt "
        "FROM " + dq + s + dq + " WHERE " + dq + "Date" + dq + " >= '2019-01-01' AND " + dq + "Date" + dq + " <= '2019-12-31'"
    )
    parts.append(part)
sql = "\nUNION ALL\n".join(parts)
sql = "SELECT symbol, cnt FROM (\n" + sql + "\n) ORDER BY cnt DESC LIMIT 5;"
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_h4lURv0gsFsNbbGeJpA93oUb': 'file_storage/call_h4lURv0gsFsNbbGeJpA93oUb.json', 'var_call_wrrVFEISzbCFFa5DhbWeDDsL': 'file_storage/call_wrrVFEISzbCFFa5DhbWeDDsL.json', 'var_call_yu2THRxExb7QIgtsCuXUShDA': 'file_storage/call_yu2THRxExb7QIgtsCuXUShDA.json'}

exec(code, env_args)
