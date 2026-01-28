code = """import json
with open(var_call_K7vCPdj9qX458HBv3QMuzxu1, 'r') as f:
    data = json.load(f)
symbols = data['symbols']
selects = []
for s in symbols:
    stmt = "SELECT '{}' AS symbol, COUNT(*) AS cnt FROM \"{}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (\"High\" - \"Low\") > 0.2 * \"Low\"".format(s, s)
    selects.append(stmt)
union_sql = " UNION ALL ".join(selects)
final_sql = "SELECT symbol, cnt FROM ( {} ) t ORDER BY cnt DESC LIMIT 5;".format(union_sql)
output = {'sql': final_sql}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_PVAfm8uVITZvm5Qg3urNUhRO': 'file_storage/call_PVAfm8uVITZvm5Qg3urNUhRO.json', 'var_call_wtLJ5gytvW712GxaYrXyCriN': 'file_storage/call_wtLJ5gytvW712GxaYrXyCriN.json', 'var_call_K7vCPdj9qX458HBv3QMuzxu1': 'file_storage/call_K7vCPdj9qX458HBv3QMuzxu1.json'}

exec(code, env_args)
