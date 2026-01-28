code = """import json
path = var_call_ZAWEUlm0qlUdHYqISvwFHbVI
with open(path, 'r', encoding='utf-8') as f:
    pairs = json.load(f)
names = sorted({p['Name'] for p in pairs if p.get('Name')})
print('__RESULT__:')
print(json.dumps(names))"""

env_args = {'var_call_yLsAhTA5bdHMTrzlstkcUKhF': 'file_storage/call_yLsAhTA5bdHMTrzlstkcUKhF.json', 'var_call_ZAWEUlm0qlUdHYqISvwFHbVI': 'file_storage/call_ZAWEUlm0qlUdHYqISvwFHbVI.json'}

exec(code, env_args)
