code = """import json
k1 = 'var_function-call-13379061347181110174'
k2 = 'var_function-call-6559325847238713717'

p1 = locals()[k1]
p2 = locals()[k2]

with open(p1, 'r') as f:
    d1 = json.load(f)
with open(p2, 'r') as f:
    d2 = json.load(f)

s1 = set(x['Symbol'] for x in d1)
s2 = set(d2)
valid = sorted(list(s1.intersection(s2)))

s = valid[0]
q = "SELECT '{}' as Symbol FROM \"{}\" WHERE \"Adj Close\" > 200 AND Date LIKE '2015%' LIMIT 1".format(s, s)

print("__RESULT__:")
print(json.dumps({"query": q}))"""

env_args = {'var_function-call-13379061347181110174': 'file_storage/function-call-13379061347181110174.json', 'var_function-call-6559325847238713717': 'file_storage/function-call-6559325847238713717.json', 'var_function-call-14816739761886936635': ['var_function-call-13379061347181110174', 'var_function-call-6559325847238713717', '__builtins__', 'json'], 'var_function-call-11850539345965912126': {'count': 1435}, 'var_function-call-2281720184919499494': {'status': 'OK', 'len': 1435}}

exec(code, env_args)
