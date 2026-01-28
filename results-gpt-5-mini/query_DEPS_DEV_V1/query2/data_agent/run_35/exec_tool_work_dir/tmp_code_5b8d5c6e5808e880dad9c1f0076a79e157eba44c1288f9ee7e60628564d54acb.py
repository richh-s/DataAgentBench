code = """import json
path = var_call_xsej0CgJXF5DxxGblASF1tv3
with open(path, 'r', encoding='utf-8') as f:
    ppv = json.load(f)
# Build mapping from (Name, Version) to ProjectName (prefer first encountered)
mapping = {}
for r in ppv:
    key = (r.get('Name'), r.get('Version'))
    if key not in mapping:
        mapping[key] = r.get('ProjectName')
# Save mapping
print('__RESULT__:')
print(json.dumps(mapping))"""

env_args = {'var_call_yLsAhTA5bdHMTrzlstkcUKhF': 'file_storage/call_yLsAhTA5bdHMTrzlstkcUKhF.json', 'var_call_ZAWEUlm0qlUdHYqISvwFHbVI': 'file_storage/call_ZAWEUlm0qlUdHYqISvwFHbVI.json', 'var_call_hW65jdsv3GmpdCSlUQsl6fxo': 'file_storage/call_hW65jdsv3GmpdCSlUQsl6fxo.json', 'var_call_ca4KRB3OW4oXuOi0zdpapENt': 'file_storage/call_ca4KRB3OW4oXuOi0zdpapENt.json', 'var_call_xsej0CgJXF5DxxGblASF1tv3': 'file_storage/call_xsej0CgJXF5DxxGblASF1tv3.json'}

exec(code, env_args)
