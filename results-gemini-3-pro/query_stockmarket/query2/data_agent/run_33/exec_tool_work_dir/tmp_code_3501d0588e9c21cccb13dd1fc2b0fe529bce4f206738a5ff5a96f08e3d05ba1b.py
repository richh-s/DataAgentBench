code = """import json
path = locals()['var_function-call-13327904948754133498']
with open(path) as f:
    data = json.load(f)
syms = data['symbols']

batches = [syms[i:i+300] for i in range(0, len(syms), 300)]
qs = []
for b in batches:
    sqs = []
    for s in b:
        q = "SELECT '" + s + "' as Symbol FROM \"" + s + "\" WHERE \"Date\" LIKE '2015-%' AND \"Adj Close\" > 200 LIMIT 1"
        sqs.append(q)
    qs.append(" UNION ALL ".join(sqs))

print("__RESULT__:")
print(json.dumps(qs))"""

env_args = {'var_function-call-689800581831186980': 'file_storage/function-call-689800581831186980.json', 'var_function-call-10272020244024100123': 'file_storage/function-call-10272020244024100123.json', 'var_function-call-13327904948754133498': 'file_storage/function-call-13327904948754133498.json'}

exec(code, env_args)
