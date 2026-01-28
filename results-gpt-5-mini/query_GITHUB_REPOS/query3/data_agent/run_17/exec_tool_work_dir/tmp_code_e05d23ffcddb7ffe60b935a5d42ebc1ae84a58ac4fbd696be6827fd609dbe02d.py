code = """import json
import os

# Load the list of repo_names from the metadata query result
path_repos = var_call_Hxz9VVU2JJkkudHDDGLOwHpY
if isinstance(path_repos, str) and os.path.exists(path_repos):
    with open(path_repos, 'r', encoding='utf-8') as f:
        repos_data = json.load(f)
else:
    repos_data = path_repos

repo_set = set()
for r in repos_data:
    # Each record has repo_name
    rn = r.get('repo_name')
    if rn:
        repo_set.add(rn)

# Load commits data
path_commits = var_call_qkMfrkUU09adommNHHC8O3Zm
if isinstance(path_commits, str) and os.path.exists(path_commits):
    with open(path_commits, 'r', encoding='utf-8') as f:
        commits = json.load(f)
else:
    commits = path_commits

# Filter commits: repo in repo_set, message exists, len<1000, and does not begin with merge/update/test
count = 0
for c in commits:
    rn = c.get('repo_name')
    if rn not in repo_set:
        continue
    msg = c.get('message')
    if not msg:
        continue
    # Ensure length < 1000
    try:
        if len(msg) >= 1000:
            continue
    except Exception:
        # if message is not a string, skip
        continue
    # Check start
    stripped = msg.lstrip()
    low = stripped.lower()
    if low.startswith('merge') or low.startswith('update') or low.startswith('test'):
        continue
    count += 1

import json as _json
print('__RESULT__:')
print(_json.dumps(count))"""

env_args = {'var_call_Hxz9VVU2JJkkudHDDGLOwHpY': 'file_storage/call_Hxz9VVU2JJkkudHDDGLOwHpY.json', 'var_call_qkMfrkUU09adommNHHC8O3Zm': 'file_storage/call_qkMfrkUU09adommNHHC8O3Zm.json'}

exec(code, env_args)
