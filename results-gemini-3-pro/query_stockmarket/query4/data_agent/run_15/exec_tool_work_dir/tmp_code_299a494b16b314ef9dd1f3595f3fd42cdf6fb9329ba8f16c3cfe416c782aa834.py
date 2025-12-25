code = """import json

# Reconstruct batches as before
with open(locals()['var_function-call-7354891248035902988'], 'r') as f:
    batches = json.load(f)

all_queries = []
for b in batches:
    all_queries.extend(b.split(" UNION ALL "))

batch_size = 25
new_batches = []
for i in range(0, len(all_queries), batch_size):
    b_q = " UNION ALL ".join(all_queries[i:i+batch_size])
    new_batches.append(b_q)

print("__RESULT__:")
print(json.dumps(new_batches[:5]))"""

env_args = {'var_function-call-8629880559091051052': 'file_storage/function-call-8629880559091051052.json', 'var_function-call-8629880559091050687': 'file_storage/function-call-8629880559091050687.json', 'var_function-call-1791396151003041946': 'file_storage/function-call-1791396151003041946.json', 'var_function-call-2330781380349541887': 'file_storage/function-call-2330781380349541887.json', 'var_function-call-13901570492172126839': 'file_storage/function-call-13901570492172126839.json', 'var_function-call-7354891248035902988': 'file_storage/function-call-7354891248035902988.json', 'var_function-call-9427095669927247292': 'file_storage/function-call-9427095669927247292.json', 'var_function-call-1633943863650871760': [10615, 10595, 10599, 10613, 7203], 'var_function-call-17251104012735503225': {'count': 10, 'lengths': [5303, 5301, 5295, 5289, 5295, 5293, 5303, 5299, 5297, 1895]}}

exec(code, env_args)
