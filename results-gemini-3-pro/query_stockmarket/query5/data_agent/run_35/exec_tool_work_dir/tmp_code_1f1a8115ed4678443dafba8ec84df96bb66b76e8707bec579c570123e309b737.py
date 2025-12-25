code = """import json

p1 = locals()['var_function-call-1835962571305796969']
p2 = locals()['var_function-call-1835962571305799198']

with open(p1) as f: i = json.load(f)
with open(p2) as f: t = json.load(f)

v = list({x['Symbol'] for x in i} & set(t))

qs = []
for s in v:
    q = "SELECT '" + s + "' as Symbol, COUNT(*) as cnt FROM \"" + s + "\" WHERE SUBSTR(Date, 1, 4) = '2019' AND (High - Low) > (0.2 * Low)"
    qs.append(q)

full_q = " UNION ALL ".join(qs) + " ORDER BY cnt DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps({"query": full_q}))"""

env_args = {'var_function-call-1835962571305796969': 'file_storage/function-call-1835962571305796969.json', 'var_function-call-1835962571305799198': 'file_storage/function-call-1835962571305799198.json', 'var_function-call-3665247125593027312': 'file_storage/function-call-3665247125593027312.json'}

exec(code, env_args)
