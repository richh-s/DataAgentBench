code = """import json, re

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pi = load_maybe_path(var_call_FhD4S8krAStrLmiGyy7r2oUI)

samples = []
for rec in pi[:2000]:
    t = rec.get('Project_Information')
    if isinstance(t, str) and (' forks' in t or 'forks' in t) and 'project' in t:
        samples.append(t)
    if len(samples) >= 5:
        break

print('__RESULT__:')
print(json.dumps(samples))"""

env_args = {'var_call_ZE9KN9DOlI7j7zVOCa3r3FqT': 'file_storage/call_ZE9KN9DOlI7j7zVOCa3r3FqT.json', 'var_call_ww7i2MXMtA5uvgeQwPLi9f81': 'file_storage/call_ww7i2MXMtA5uvgeQwPLi9f81.json', 'var_call_FhD4S8krAStrLmiGyy7r2oUI': 'file_storage/call_FhD4S8krAStrLmiGyy7r2oUI.json', 'var_call_VhucjoAshOLRzdU24ovCtJHi': [], 'var_call_t1kUjKcXcmnAzEy8sgbAN9kG': []}

exec(code, env_args)
