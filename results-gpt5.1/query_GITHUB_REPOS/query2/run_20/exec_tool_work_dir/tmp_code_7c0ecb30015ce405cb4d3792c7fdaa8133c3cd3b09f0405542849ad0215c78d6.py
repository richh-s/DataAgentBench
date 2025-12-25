code = """import json, re
from collections import defaultdict

path = var_call_bzorlpnj723iHQRPz0uJklNq
with open(path) as f:
    data = json.load(f)

max_copies = -1
best = None
pattern = re.compile(r"(copied|appearing|repeated|duplicated|seen) (\d+) times")

for row in data:
    desc = row.get('repo_data_description') or ''
    m = pattern.search(desc)
    if not m:
        continue
    copies = int(m.group(2))
    if copies > max_copies:
        max_copies = copies
        best = {'id': row['id'], 'sample_repo_name': row['sample_repo_name'], 'copies': copies}

result = best

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_bzorlpnj723iHQRPz0uJklNq': 'file_storage/call_bzorlpnj723iHQRPz0uJklNq.json'}

exec(code, env_args)
