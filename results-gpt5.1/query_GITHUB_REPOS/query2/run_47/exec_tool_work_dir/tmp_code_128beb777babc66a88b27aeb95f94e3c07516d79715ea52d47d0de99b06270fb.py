code = """import json, re
path = var_call_UqsrZ8AcyfQ3yebn7rrAd5qG
with open(path) as f:
    data = json.load(f)
max_copies = -1
best = None
for row in data:
    desc = row['repo_data_description'] or ''
    m = re.search(r'(?:duplicated|appearing|repeated|seen|copied) (\d+) times', desc)
    if not m:
        continue
    copies = int(m.group(1))
    if copies > max_copies:
        max_copies = copies
        best = {'id': row['id'], 'sample_repo_name': row['sample_repo_name'], 'copies': copies}
result = best
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_UqsrZ8AcyfQ3yebn7rrAd5qG': 'file_storage/call_UqsrZ8AcyfQ3yebn7rrAd5qG.json'}

exec(code, env_args)
