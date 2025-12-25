code = """import json
with open(locals()['var_function-call-4354025683768215761'], 'r') as f:
    ids = json.load(f)

chunk = ids[0:1000]
print("__RESULT__:")
print(json.dumps(chunk))"""

env_args = {'var_function-call-3168952214730479894': 'file_storage/function-call-3168952214730479894.json', 'var_function-call-4354025683768215761': 'file_storage/function-call-4354025683768215761.json', 'var_function-call-15545576569609142318': 'file_storage/function-call-15545576569609142318.json', 'var_function-call-4981172069167279422': 6696, 'var_function-call-12969213931199910920': {'min': 13, 'max': 127570, 'count': 6696}}

exec(code, env_args)
