code = """import json

path1 = locals()['var_function-call-15016460926965200659']
path2 = locals()['var_function-call-570738584850609366']

with open(path1, 'r') as f:
    d1 = json.load(f)
    
s_set = set()
for x in d1:
    s_set.add(x['Symbol'])

with open(path2, 'r') as f:
    d2 = json.load(f)

valid = []
for s in d2:
    if s in s_set:
        valid.append(s)

sqls = []
for s in valid:
    q = "SELECT '" + s + "' as Symbol, COUNT(*) as cnt FROM \"" + s + "\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.2 * Low"
    sqls.append(q)

final_q = ""
if len(sqls) > 0:
    final_q = " UNION ALL ".join(sqls)
    final_q = final_q + " ORDER BY cnt DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps({"query": final_q, "count": len(valid)}))"""

env_args = {'var_function-call-15016460926965200659': 'file_storage/function-call-15016460926965200659.json', 'var_function-call-570738584850609366': 'file_storage/function-call-570738584850609366.json'}

exec(code, env_args)
