code = """import json, re
from pathlib import Path

path = Path(var_call_JaHxz8loYuj2ls3BK7KYa7HD)
rows = json.loads(path.read_text())

max_copies = -1
best = None
pattern = re.compile(r"(appearing|duplicated|copied|seen|repeated) (\d+) times")

for r in rows:
    desc = r.get('repo_data_description') or ''
    if 'non-binary' not in desc:
        continue
    m = pattern.search(desc)
    if not m:
        continue
    copies = int(m.group(2))
    if copies > max_copies:
        max_copies = copies
        best = {'id': r['id'], 'sample_repo_name': r['sample_repo_name'], 'copies': copies}

result = best

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_JaHxz8loYuj2ls3BK7KYa7HD': 'file_storage/call_JaHxz8loYuj2ls3BK7KYa7HD.json'}

exec(code, env_args)
