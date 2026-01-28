code = """import json, re
with open(var_call_4EPghs9YfMy0CszRHq9wZrCU, 'r', encoding='utf-8') as f:
    data = json.load(f)
# Filter for projects related to FEMA, emergency, or warning
filtered = []
for r in data:
    name = r.get('Project_Name','')
    if re.search(r'FEMA', name, re.I) or re.search(r'emergency', name, re.I) or re.search(r'warning', name, re.I):
        filtered.append({'Project_Name': name, 'Funding_Source': r.get('Funding_Source'), 'Amount': r.get('Amount'), 'Status': r.get('Status')})
# Sort by Project_Name
filtered = sorted(filtered, key=lambda x: x['Project_Name'].lower())
print('__RESULT__:')
print(json.dumps(filtered))"""

env_args = {'var_call_Ag1Nv9ECG7ZO4PrsZpGxuiUV': 'file_storage/call_Ag1Nv9ECG7ZO4PrsZpGxuiUV.json', 'var_call_pSrNmu38G145Fy0MAdlanHwu': 'file_storage/call_pSrNmu38G145Fy0MAdlanHwu.json', 'var_call_4EPghs9YfMy0CszRHq9wZrCU': 'file_storage/call_4EPghs9YfMy0CszRHq9wZrCU.json'}

exec(code, env_args)
