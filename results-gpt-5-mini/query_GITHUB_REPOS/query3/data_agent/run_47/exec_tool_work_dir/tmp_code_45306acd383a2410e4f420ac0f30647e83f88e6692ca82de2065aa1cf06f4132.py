code = """import json
from pathlib import Path

# Load the repo list (metadata query result)
path_repos = Path(var_call_yGFPfSHi8WTncYMr9k1oadra)
with open(path_repos, 'r', encoding='utf-8') as f:
    repos_data = json.load(f)

# Extract repo names into a set
repos_set = set()
for row in repos_data:
    # row expected to have 'repo_name'
    rn = row.get('repo_name')
    if rn:
        repos_set.add(rn)

# Load commits data
path_commits = Path(var_call_kc73EMaf8PLEcAzdK6nmVZ3C)
with open(path_commits, 'r', encoding='utf-8') as f:
    commits_data = json.load(f)

# Filter commits
count = 0
excluded_prefixes = ('merge', 'update', 'test')
for c in commits_data:
    repo = c.get('repo_name')
    if not repo or repo not in repos_set:
        continue
    msg = c.get('message')
    if not msg:
        continue
    # ensure it's a string
    if not isinstance(msg, str):
        try:
            msg = str(msg)
        except Exception:
            continue
    # Check length
    if len(msg) >= 1000:
        continue
    # Trim leading whitespace and lowercase for prefix check
    s = msg.lstrip().lower()
    if any(s.startswith(p) for p in excluded_prefixes):
        continue
    # Passed all filters
    count += 1

import json as _json
print("__RESULT__:")
print(_json.dumps(count))"""

env_args = {'var_call_2a82yUQfH1CbgpfZLMsT8c4y': ['languages', 'repos', 'licenses'], 'var_call_2Wg547eiR2HvP7ugV5mjups4': ['commits', 'contents', 'files'], 'var_call_yGFPfSHi8WTncYMr9k1oadra': 'file_storage/call_yGFPfSHi8WTncYMr9k1oadra.json', 'var_call_kc73EMaf8PLEcAzdK6nmVZ3C': 'file_storage/call_kc73EMaf8PLEcAzdK6nmVZ3C.json'}

exec(code, env_args)
