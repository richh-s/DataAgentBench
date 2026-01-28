code = """import json

path = var_call_f39xK48tgXiUg6Y69VTnBuVj
with open(path, 'r') as f:
    data = json.load(f)

filtered = []
for r in data:
    pname = (r.get('Project_Name') or '').lower()
    fsrc = (r.get('Funding_Source') or '').lower()
    if 'fema' in pname or 'emergency' in pname or 'fema' in fsrc or 'emergency' in fsrc:
        filtered.append({'Project_Name': r.get('Project_Name'), 'Funding_Source': r.get('Funding_Source'), 'Amount': r.get('Amount'), 'Status': r.get('Status')})

# Remove duplicates (if any)
seen = set()
out = []
for rec in filtered:
    key = (rec['Project_Name'], rec['Funding_Source'], rec['Amount'])
    if key not in seen:
        seen.add(key)
        out.append(rec)

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_4mLAARyPY98ipz6fdcJufYyy': 'file_storage/call_4mLAARyPY98ipz6fdcJufYyy.json', 'var_call_5ZTqNs3HVZYVKoxQ2862Me1r': 'file_storage/call_5ZTqNs3HVZYVKoxQ2862Me1r.json', 'var_call_f39xK48tgXiUg6Y69VTnBuVj': 'file_storage/call_f39xK48tgXiUg6Y69VTnBuVj.json'}

exec(code, env_args)
