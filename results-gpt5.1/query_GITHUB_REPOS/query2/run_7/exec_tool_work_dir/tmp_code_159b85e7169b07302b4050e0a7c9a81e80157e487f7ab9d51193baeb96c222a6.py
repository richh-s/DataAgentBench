code = """import json, re
path = var_call_2HBPOfy4rXaxalHX8EKzvj4I
with open(path) as f:
    data = json.load(f)
max_copies = -1
best = None
for row in data:
    desc = row['repo_data_description'] or ''
    m = re.search(r'(?:duplicated|appearing|appears|repeated|seen) (\d+) times', desc)
    if not m:
        continue
    copies = int(m.group(1))
    if copies > max_copies:
        max_copies = copies
        best = row
result = {'repo_name': best['sample_repo_name'] if best else None, 'file_id': best['id'] if best else None, 'copies': max_copies}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2HBPOfy4rXaxalHX8EKzvj4I': 'file_storage/call_2HBPOfy4rXaxalHX8EKzvj4I.json'}

exec(code, env_args)
