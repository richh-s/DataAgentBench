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

queries = []
for s in valid:
    # Use triple single quotes for the string to avoid escaping issues
    # But inside SQL we need single quotes for dates and literals.
    # SQL: SELECT 'SYM' ...
    # Python: q = '''SELECT '{0}' ...'''
    q = '''SELECT '{0}' as Symbol FROM "{0}" WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' AND "Adj Close" > 200 LIMIT 1'''.format(s)
    queries.append(q)

fq = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps({"count": len(valid), "query": fq}))"""

env_args = {'var_function-call-11805765579617057108': 'file_storage/function-call-11805765579617057108.json', 'var_function-call-18208316545680584426': 'file_storage/function-call-18208316545680584426.json'}

exec(code, env_args)
