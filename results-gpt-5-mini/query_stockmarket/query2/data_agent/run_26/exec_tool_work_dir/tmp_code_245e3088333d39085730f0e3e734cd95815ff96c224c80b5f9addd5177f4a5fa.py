code = """import json
p = var_call_4cWA3639OvPpZZVOsHr7ctXT
with open(p,'r') as f:
    candidates = json.load(f)
qs = []
for s in candidates:
    qs.append(f"SELECT '{s}' as Symbol FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1")
sql = "\nUNION ALL\n".join(qs) + ";" if qs else ""
out = {"num_candidates": len(candidates), "sql": sql}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_EeBDIfF6nIPvT4Tn05bSTLUt': 'file_storage/call_EeBDIfF6nIPvT4Tn05bSTLUt.json', 'var_call_BhqADYroukDRFFl1xBNUru7t': 'file_storage/call_BhqADYroukDRFFl1xBNUru7t.json', 'var_call_4cWA3639OvPpZZVOsHr7ctXT': 'file_storage/call_4cWA3639OvPpZZVOsHr7ctXT.json'}

exec(code, env_args)
