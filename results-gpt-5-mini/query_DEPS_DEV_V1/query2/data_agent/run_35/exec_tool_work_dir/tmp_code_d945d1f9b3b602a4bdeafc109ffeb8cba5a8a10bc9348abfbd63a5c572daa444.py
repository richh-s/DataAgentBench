code = """import json
# load package pairs (Name,Version) from earlier var_call_ZAWEUlm0qlUdHYqISvwFHbVI
pairs_path = var_call_ZAWEUlm0qlUdHYqISvwFHbVI
with open(pairs_path, 'r', encoding='utf-8') as f:
    pairs = json.load(f)
# load project_packageversion records from var_call_D1crF1iMb1rYajTXGSwUo2mg
ppv_path = var_call_D1crF1iMb1rYajTXGSwUo2mg
with open(ppv_path, 'r', encoding='utf-8') as f:
    ppv = json.load(f)
# Build mapping from (Name,Version) to ProjectName using ppv
mapping = {}
for r in ppv:
    key = (r.get('Name'), r.get('Version'))
    if key not in mapping and r.get('ProjectName'):
        mapping[key] = r.get('ProjectName')
# For each pair, find ProjectName
results = []
for p in pairs:
    key = (p.get('Name'), p.get('Version'))
    proj = mapping.get(key)
    if proj:
        results.append({'Name': p.get('Name'), 'Version': p.get('Version'), 'ProjectName': proj})
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_yLsAhTA5bdHMTrzlstkcUKhF': 'file_storage/call_yLsAhTA5bdHMTrzlstkcUKhF.json', 'var_call_ZAWEUlm0qlUdHYqISvwFHbVI': 'file_storage/call_ZAWEUlm0qlUdHYqISvwFHbVI.json', 'var_call_hW65jdsv3GmpdCSlUQsl6fxo': 'file_storage/call_hW65jdsv3GmpdCSlUQsl6fxo.json', 'var_call_ca4KRB3OW4oXuOi0zdpapENt': 'file_storage/call_ca4KRB3OW4oXuOi0zdpapENt.json', 'var_call_xsej0CgJXF5DxxGblASF1tv3': 'file_storage/call_xsej0CgJXF5DxxGblASF1tv3.json', 'var_call_D1crF1iMb1rYajTXGSwUo2mg': 'file_storage/call_D1crF1iMb1rYajTXGSwUo2mg.json'}

exec(code, env_args)
