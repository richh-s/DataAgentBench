code = """import json

p1 = locals()['var_function-call-1835962571305796969']
p2 = locals()['var_function-call-1835962571305799198']

with open(p1) as f: i = json.load(f)
with open(p2) as f: t = json.load(f)

v = sorted(list({x['Symbol'] for x in i} & set(t))) # Sort to be deterministic

# Split
mid = len(v) // 2
batch1 = v[:mid]

qs = []
sq = chr(39)
dq = chr(34)

for s in batch1:
    q = "SELECT " + sq + s + sq + " as Symbol, COUNT(*) as cnt FROM " + dq + s + dq + " WHERE SUBSTR(Date, 1, 4) = " + sq + "2019" + sq + " AND (High - Low) > (0.2 * Low)"
    qs.append(q)

query = " UNION ALL ".join(qs)

print("__RESULT__:")
print(json.dumps({"query": query}))"""

env_args = {'var_function-call-1835962571305796969': 'file_storage/function-call-1835962571305796969.json', 'var_function-call-1835962571305799198': 'file_storage/function-call-1835962571305799198.json', 'var_function-call-3665247125593027312': 'file_storage/function-call-3665247125593027312.json', 'var_function-call-13104781202796968482': 'file_storage/function-call-13104781202796968482.json', 'var_function-call-14492313189319632336': 'file_storage/function-call-14492313189319632336.json'}

exec(code, env_args)
