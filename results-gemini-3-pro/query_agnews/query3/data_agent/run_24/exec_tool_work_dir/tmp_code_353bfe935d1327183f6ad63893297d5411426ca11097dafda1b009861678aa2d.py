code = """import json
with open(locals()['var_function-call-12368714050560337210'], 'r') as f:
    ids = json.load(f)
print(f"Count of IDs: {len(ids)}")
print("__RESULT__:")
print(len(ids))"""

env_args = {'var_function-call-3160904242471063353': 'file_storage/function-call-3160904242471063353.json', 'var_function-call-12368714050560337210': 'file_storage/function-call-12368714050560337210.json'}

exec(code, env_args)
