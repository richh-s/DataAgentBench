code = """import json

file_path = locals()['var_function-call-344482854029373658']
with open(file_path, 'r') as f:
    ids = json.load(f)

print("__RESULT__:")
print(json.dumps({"min": min(ids), "max": max(ids)}))"""

env_args = {'var_function-call-5463793062581898541': 'file_storage/function-call-5463793062581898541.json', 'var_function-call-344482854029373658': 'file_storage/function-call-344482854029373658.json', 'var_function-call-8270661288261401404': 14860, 'var_function-call-15074060882240908165': [{'COUNT(*)': '127600'}]}

exec(code, env_args)
