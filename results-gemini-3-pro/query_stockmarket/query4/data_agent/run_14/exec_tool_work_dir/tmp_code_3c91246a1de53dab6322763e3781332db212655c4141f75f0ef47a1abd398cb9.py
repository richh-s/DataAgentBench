code = """import json
k1 = 'var_function-call-2664401347096856404'
k2 = 'var_function-call-14718190706972975468'
p1 = locals().get(k1)
p2 = locals().get(k2)

# Load data to check if we can
with open(p1, 'r') as f:
    d1 = json.load(f)
with open(p2, 'r') as f:
    d2 = json.load(f)

print('__RESULT__:')
print(json.dumps({'count1': len(d1), 'count2': len(d2)}))"""

env_args = {'var_function-call-2664401347096856404': 'file_storage/function-call-2664401347096856404.json', 'var_function-call-14718190706972975468': 'file_storage/function-call-14718190706972975468.json'}

exec(code, env_args)
