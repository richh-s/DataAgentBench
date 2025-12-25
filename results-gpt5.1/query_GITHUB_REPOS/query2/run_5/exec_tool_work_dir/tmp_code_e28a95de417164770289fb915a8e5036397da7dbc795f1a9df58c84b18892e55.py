code = """import json, re
from pathlib import Path

path = var_call_gzBVjol06rCo0y7dcYw29x89
with open(path) as f:
    data = json.load(f)

max_copies = -1
best = None
pattern = re.compile(r"(copied|duplicated|appearing|seen|repeated) (\d+) times")

for row in data:
    desc = row.get('repo_data_description') or ''
    m = pattern.search(desc)
    if not m:
        continue
    copies = int(m.group(2))
    if copies > max_copies:
        max_copies = copies
        best = row

result = {'max_copies': max_copies, 'id': best.get('id') if best else None, 'sample_repo_name': best.get('sample_repo_name') if best else None}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gzBVjol06rCo0y7dcYw29x89': 'file_storage/call_gzBVjol06rCo0y7dcYw29x89.json'}

exec(code, env_args)
