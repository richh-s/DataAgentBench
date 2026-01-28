code = """import json

res_path = var_call_LjDjToKzxMRjHcG573Em5PnB
with open(res_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

keywords = ['fema', 'outdoor warning', 'sirens', 'emergency']

filtered = []
for r in data:
    name_low = r.get('Project_Name','').lower()
    if any(k in name_low for k in keywords):
        filtered.append(r)

lines = []
lines.append('Project Name | Funding Source | Amount | Status')
for r in filtered:
    name = r.get('Project_Name','')
    src = r.get('Funding_Source','')
    amt = r.get('Amount', 0)
    status = r.get('Status','') or 'unknown'
    lines.append(f"{name} | {src} | ${amt:,} | {status}")

answer = "\n".join(lines)

print("__RESULT__:")
print(json.dumps(answer))"""

env_args = {'var_call_8vBnfmWWXT7qozNkwSfsNVHc': 'file_storage/call_8vBnfmWWXT7qozNkwSfsNVHc.json', 'var_call_U60WqxOGdjsbcqS6PF9PWbjF': 'file_storage/call_U60WqxOGdjsbcqS6PF9PWbjF.json', 'var_call_LjDjToKzxMRjHcG573Em5PnB': 'file_storage/call_LjDjToKzxMRjHcG573Em5PnB.json'}

exec(code, env_args)
