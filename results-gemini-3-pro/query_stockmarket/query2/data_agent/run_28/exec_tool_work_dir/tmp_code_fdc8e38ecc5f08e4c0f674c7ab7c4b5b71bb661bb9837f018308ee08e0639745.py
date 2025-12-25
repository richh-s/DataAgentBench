code = """import json

p1 = locals()['var_function-call-11805765579617057108']
p2 = locals()['var_function-call-18208316545680584426']

with open(p1, 'r') as f:
    d1 = json.load(f)
with open(p2, 'r') as f:
    d2 = json.load(f)

s1 = set(i['Symbol'] for i in d1)
s2 = set(d2)
valid = list(s1.intersection(s2))
valid.sort()

batch = valid[0:50]
queries = []
for s in batch:
    # Construct query using chr to avoid quote issues in source
    # SELECT 'SYM' as Symbol FROM "SYM" WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' AND "Adj Close" > 200 LIMIT 1
    q = "SELECT " + chr(39) + s + chr(39) + " as Symbol FROM " + chr(34) + s + chr(34) + " WHERE Date BETWEEN " + chr(39) + "2015-01-01" + chr(39) + " AND " + chr(39) + "2015-12-31" + chr(39) + " AND " + chr(34) + "Adj Close" + chr(34) + " > 200 LIMIT 1"
    queries.append(q)

final_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-11805765579617057108': 'file_storage/function-call-11805765579617057108.json', 'var_function-call-18208316545680584426': 'file_storage/function-call-18208316545680584426.json', 'var_function-call-4450274117295212615': 'file_storage/function-call-4450274117295212615.json', 'var_function-call-14797498511390155982': 'file_storage/function-call-14797498511390155982.json'}

exec(code, env_args)
