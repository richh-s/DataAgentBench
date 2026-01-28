code = """import json

res_path = var_call_dloGuUYONRqxgiFxJkj2ybgZ
with open(res_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

keywords = ['fema', 'emergency', 'outdoor warning', 'sirens']
filtered = []
for r in data:
    pname = r.get('Project_Name', '')
    if not isinstance(pname, str):
        continue
    low = pname.lower()
    for k in keywords:
        if k in low:
            filtered.append({
                'Project_Name': pname,
                'Funding_Source': r.get('Funding_Source', ''),
                'Amount': r.get('Amount', 0),
                'Status': r.get('Status', 'unknown')
            })
            break

print('__RESULT__:')
print(json.dumps(filtered))"""

env_args = {'var_call_8vBnfmWWXT7qozNkwSfsNVHc': 'file_storage/call_8vBnfmWWXT7qozNkwSfsNVHc.json', 'var_call_U60WqxOGdjsbcqS6PF9PWbjF': 'file_storage/call_U60WqxOGdjsbcqS6PF9PWbjF.json', 'var_call_LjDjToKzxMRjHcG573Em5PnB': 'file_storage/call_LjDjToKzxMRjHcG573Em5PnB.json', 'var_call_dloGuUYONRqxgiFxJkj2ybgZ': 'file_storage/call_dloGuUYONRqxgiFxJkj2ybgZ.json'}

exec(code, env_args)
