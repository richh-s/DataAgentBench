code = """import json

file_path = locals()['var_function-call-8411561626965281580']
with open(file_path, 'r') as f:
    papers = json.load(f)

print("__RESULT__:")
debug_info = []
for p in papers[:5]:
    debug_info.append({
        "filename": p['filename'],
        "snippet": p['text'][:300]
    })
print(json.dumps(debug_info))"""

env_args = {'var_function-call-14900117783735274401': 'file_storage/function-call-14900117783735274401.json', 'var_function-call-8411561626965281580': 'file_storage/function-call-8411561626965281580.json', 'var_function-call-7310412388729179495': []}

exec(code, env_args)
