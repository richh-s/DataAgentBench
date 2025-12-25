code = """import json
path = locals()['var_function-call-13327904948754133498']
with open(path) as f:
    data = json.load(f)
syms = data['symbols']

batch_size = 50
batches = [syms[i:i+batch_size] for i in range(0, len(syms), batch_size)]
qs = []
dq = chr(34) # double quote
sq = chr(39) # single quote
for b in batches:
    sqs = []
    for s in b:
        # SELECT 'SYM' as Symbol FROM "SYM" WHERE "Date" LIKE '2015-%' AND "Adj Close" > 200 LIMIT 1
        q = "SELECT " + sq + s + sq + " as Symbol FROM " + dq + s + dq + " WHERE " + dq + "Date" + dq + " LIKE " + sq + "2015-%" + sq + " AND " + dq + "Adj Close" + dq + " > 200 LIMIT 1"
        sqs.append(q)
    qs.append(" UNION ALL ".join(sqs))

print("__RESULT__:")
print(json.dumps(qs))"""

env_args = {'var_function-call-689800581831186980': 'file_storage/function-call-689800581831186980.json', 'var_function-call-10272020244024100123': 'file_storage/function-call-10272020244024100123.json', 'var_function-call-13327904948754133498': 'file_storage/function-call-13327904948754133498.json', 'var_function-call-2221161902044302506': 'file_storage/function-call-2221161902044302506.json', 'var_function-call-6046526480813939881': 'file_storage/function-call-6046526480813939881.json'}

exec(code, env_args)
