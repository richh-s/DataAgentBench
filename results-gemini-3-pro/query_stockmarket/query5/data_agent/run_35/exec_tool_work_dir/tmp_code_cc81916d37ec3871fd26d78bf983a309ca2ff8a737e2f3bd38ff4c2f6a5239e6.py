code = """import json

k1 = 'var_function-call-1835962571305796969'
k2 = 'var_function-call-1835962571305799198'
path1 = locals()[k1]
path2 = locals()[k2]

with open(path1, 'r') as f:
    info = json.load(f)
with open(path2, 'r') as f:
    tables = json.load(f)

syms = {i['Symbol'] for i in info}
tabs = set(tables)
valid = list(syms.intersection(tabs))

q_parts = []
# Use .format() to avoid quote confusion
template = "SELECT '{0}' as Symbol, COUNT(*) as cnt FROM \"{0}\" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)"

for s in valid:
    q_parts.append(template.format(s))

if not q_parts:
    query = ""
else:
    query = " UNION ALL ".join(q_parts)
    query += " ORDER BY cnt DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps({"query": query}))"""

env_args = {'var_function-call-1835962571305796969': 'file_storage/function-call-1835962571305796969.json', 'var_function-call-1835962571305799198': 'file_storage/function-call-1835962571305799198.json', 'var_function-call-3665247125593027312': 'file_storage/function-call-3665247125593027312.json'}

exec(code, env_args)
