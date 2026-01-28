code = """import json

# Load the repository list (from the metadata query result file)
with open(var_call_Zkt3pHtdGV2iQFb74zKh6oPi, 'r') as f:
    repo_rows = json.load(f)

# Build set of repo names
repo_set = set()
for r in repo_rows:
    rn = r.get('repo_name')
    if rn:
        repo_set.add(rn)

# Load commits
with open(var_call_yO3LpqBhKcfoj9m5QF6i7VCD, 'r') as f:
    commits = json.load(f)

# Filter commits according to conditions
count = 0
for c in commits:
    rn = c.get('repo_name')
    if rn not in repo_set:
        continue
    msg = c.get('message')
    if not msg:
        continue
    if not isinstance(msg, str):
        continue
    ms = msg.strip()
    if ms == '':
        continue
    if len(ms) >= 1000:
        continue
    low = ms.lower()
    if low.startswith('merge') or low.startswith('update') or low.startswith('test'):
        continue
    count += 1

import json as _json
print("__RESULT__:")
print(_json.dumps(count))"""

env_args = {'var_call_Zkt3pHtdGV2iQFb74zKh6oPi': 'file_storage/call_Zkt3pHtdGV2iQFb74zKh6oPi.json', 'var_call_yO3LpqBhKcfoj9m5QF6i7VCD': 'file_storage/call_yO3LpqBhKcfoj9m5QF6i7VCD.json'}

exec(code, env_args)
