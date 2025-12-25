code = """import json

k1 = "var_function-call-13379061347181110174"
k2 = "var_function-call-6559325847238713717"

with open(locals()[k1], "r") as f:
    d1 = json.load(f)
with open(locals()[k2], "r") as f:
    d2 = json.load(f)

s1 = set(x["Symbol"] for x in d1)
s2 = set(d2)

valid = sorted(list(s1.intersection(s2)))

qs = []
chunk = []
for s in valid:
    q = "SELECT '" + s + "' as Symbol FROM \"" + s + "\" WHERE \"Adj Close\" > 200 AND Date >= '2015-01-01' AND Date <= '2015-12-31' LIMIT 1"
    chunk.append(q)
    if len(chunk) >= 100:
        qs.append(" UNION ALL ".join(chunk))
        chunk = []

if chunk:
    qs.append(" UNION ALL ".join(chunk))

print("__RESULT__:")
print(json.dumps({"count": len(valid), "queries": qs}))"""

env_args = {'var_function-call-13379061347181110174': 'file_storage/function-call-13379061347181110174.json', 'var_function-call-6559325847238713717': 'file_storage/function-call-6559325847238713717.json', 'var_function-call-14816739761886936635': ['var_function-call-13379061347181110174', 'var_function-call-6559325847238713717', '__builtins__', 'json']}

exec(code, env_args)
