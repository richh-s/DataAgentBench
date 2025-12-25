code = """import json
with open(locals()['var_function-call-4354025683768215761'], 'r') as f:
    ids = json.load(f)
print("__RESULT__:")
print(json.dumps({"min": min(ids), "max": max(ids), "count": len(ids)}))"""

env_args = {'var_function-call-3168952214730479894': 'file_storage/function-call-3168952214730479894.json', 'var_function-call-4354025683768215761': 'file_storage/function-call-4354025683768215761.json', 'var_function-call-15545576569609142318': 'file_storage/function-call-15545576569609142318.json', 'var_function-call-4981172069167279422': 6696}

exec(code, env_args)
