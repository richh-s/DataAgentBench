code = """import json

file_path = locals()['var_function-call-3327544021322435934']
with open(file_path, 'r') as f:
    ids = json.load(f)

print("__RESULT__:")
print(json.dumps({"min": min(ids), "max": max(ids), "count": len(ids)}))"""

env_args = {'var_function-call-12987280970809318212': 'file_storage/function-call-12987280970809318212.json', 'var_function-call-3327544021322435934': 'file_storage/function-call-3327544021322435934.json'}

exec(code, env_args)
