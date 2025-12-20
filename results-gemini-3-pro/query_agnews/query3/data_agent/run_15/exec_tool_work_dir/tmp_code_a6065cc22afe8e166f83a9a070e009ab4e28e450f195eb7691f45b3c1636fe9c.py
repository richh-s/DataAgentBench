code = """import json

file_path = locals()['var_function-call-13397356953059300154']
with open(file_path, 'r') as f:
    ids = json.load(f)

print("__RESULT__:")
print(json.dumps({"min": min(ids), "max": max(ids)}))"""

env_args = {'var_function-call-2680107260476408076': 'file_storage/function-call-2680107260476408076.json', 'var_function-call-13397356953059300154': 'file_storage/function-call-13397356953059300154.json', 'var_function-call-1670274316384238860': 14860}

exec(code, env_args)
