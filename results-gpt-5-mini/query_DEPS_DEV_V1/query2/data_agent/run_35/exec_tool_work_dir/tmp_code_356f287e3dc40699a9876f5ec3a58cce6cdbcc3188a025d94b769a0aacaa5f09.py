code = """import json
path = var_call_xsej0CgJXF5DxxGblASF1tv3
with open(path, 'r', encoding='utf-8') as f:
    ppv = json.load(f)
# Build list of records
records = []
for r in ppv:
    records.append({'Name': r.get('Name'), 'Version': r.get('Version'), 'ProjectName': r.get('ProjectName')})
print('__RESULT__:')
print(json.dumps(records))"""

env_args = {'var_call_yLsAhTA5bdHMTrzlstkcUKhF': 'file_storage/call_yLsAhTA5bdHMTrzlstkcUKhF.json', 'var_call_ZAWEUlm0qlUdHYqISvwFHbVI': 'file_storage/call_ZAWEUlm0qlUdHYqISvwFHbVI.json', 'var_call_hW65jdsv3GmpdCSlUQsl6fxo': 'file_storage/call_hW65jdsv3GmpdCSlUQsl6fxo.json', 'var_call_ca4KRB3OW4oXuOi0zdpapENt': 'file_storage/call_ca4KRB3OW4oXuOi0zdpapENt.json', 'var_call_xsej0CgJXF5DxxGblASF1tv3': 'file_storage/call_xsej0CgJXF5DxxGblASF1tv3.json'}

exec(code, env_args)
