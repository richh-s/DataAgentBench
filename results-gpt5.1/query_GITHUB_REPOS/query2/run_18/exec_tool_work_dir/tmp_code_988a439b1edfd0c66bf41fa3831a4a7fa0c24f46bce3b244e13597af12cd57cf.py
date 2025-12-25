code = """import json, re
path = var_call_qyJYN2E9nzWlq9PdLvJSqH7T
with open(path) as f:
    data = json.load(f)
max_copies = -1
best = None
for row in data:
    desc = row['repo_data_description'] or ''
    m = re.search(r'(?i)copied (\d+) times|appearing (\d+) times|seen (\d+) times|duplicated (\d+) times|repeated (\d+) times', desc)
    if not m:
        continue
    copies = max(int(g) for g in m.groups() if g)
    if copies > max_copies:
        max_copies = copies
        best = {'id': row['id'], 'sample_repo_name': row['sample_repo_name'], 'copies': copies}
result = best
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qyJYN2E9nzWlq9PdLvJSqH7T': 'file_storage/call_qyJYN2E9nzWlq9PdLvJSqH7T.json'}

exec(code, env_args)
