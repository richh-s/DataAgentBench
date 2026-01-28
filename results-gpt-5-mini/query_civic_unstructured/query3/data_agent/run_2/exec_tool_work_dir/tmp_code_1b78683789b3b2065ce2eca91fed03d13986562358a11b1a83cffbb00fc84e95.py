code = """import json, re
# Load previous results
path = var_call_hk49l5eo8lkkMkuZHkrQqmC8
if isinstance(path, str):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
else:
    data = path

pat = re.compile(r'fema|emergency', re.I)
filtered = []
for r in data:
    pname = r.get('Project_Name','') or ''
    fsrc = r.get('Funding_Source','') or ''
    if pat.search(pname) or pat.search(fsrc):
        filtered.append({
            'Project_Name': pname,
            'Funding_Source': fsrc,
            'Amount': r.get('Amount'),
            'Status': r.get('Status')
        })

# Sort by Project_Name
filtered = sorted(filtered, key=lambda x: x['Project_Name'].lower())

print('__RESULT__:')
print(json.dumps(filtered))"""

env_args = {'var_call_gWIVvlDnNeNO28YeN24U8bSs': 'file_storage/call_gWIVvlDnNeNO28YeN24U8bSs.json', 'var_call_51uSuFk7C0eKQtq87NGdSzGT': 'file_storage/call_51uSuFk7C0eKQtq87NGdSzGT.json', 'var_call_hk49l5eo8lkkMkuZHkrQqmC8': 'file_storage/call_hk49l5eo8lkkMkuZHkrQqmC8.json'}

exec(code, env_args)
