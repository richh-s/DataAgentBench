code = """import json

file_path = locals()['var_function-call-17144050128473710327']
with open(file_path, 'r') as f:
    data = json.load(f)

ids = [int(i) for i in data['ids']]
min_id = min(ids)
max_id = max(ids)
count = len(ids)

print("__RESULT__:")
print(json.dumps({"min": min_id, "max": max_id, "count": count}))"""

env_args = {'var_function-call-4731593455298835981': 'file_storage/function-call-4731593455298835981.json', 'var_function-call-17144050128473710327': 'file_storage/function-call-17144050128473710327.json'}

exec(code, env_args)
