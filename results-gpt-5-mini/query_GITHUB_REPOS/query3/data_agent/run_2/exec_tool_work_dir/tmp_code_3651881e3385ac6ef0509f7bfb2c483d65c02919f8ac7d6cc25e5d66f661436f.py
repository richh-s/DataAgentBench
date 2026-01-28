code = """import json
# Load metadata repo list (Shell + Apache-2.0)
meta_path = var_call_fNDvHPSqxhTTLn5V45C4wwjs
with open(meta_path, 'r') as f:
    meta = json.load(f)
shell_repos = set()
for r in meta:
    rn = r.get('repo_name')
    if rn:
        shell_repos.add(rn)
# Load commits result (already filtered by message conditions)
commits_path = var_call_fWMTTXKSyQYmQk3gHgrO9qa4
with open(commits_path, 'r') as f:
    commits = json.load(f)
# Count messages where repo_name is in shell_repos and re-apply filters to be safe
total = 0
from collections import defaultdict
repo_counts = defaultdict(int)
for c in commits:
    rn = c.get('repo_name')
    msg = c.get('message')
    if not rn or msg is None:
        continue
    if rn not in shell_repos:
        continue
    m = msg.lstrip()
    if m == '':
        continue
    if len(m) >= 1000:
        continue
    low = m.lower()
    if low.startswith(('merge','update','test')):
        continue
    total += 1
    repo_counts[rn] += 1
# Prepare top repos list (top 50)
top_repos = sorted(repo_counts.items(), key=lambda x: x[1], reverse=True)[:50]
result = {
    'total_commit_messages': total,
    'matching_repos_count': len(repo_counts),
    'top_repos_sample': top_repos
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_fNDvHPSqxhTTLn5V45C4wwjs': 'file_storage/call_fNDvHPSqxhTTLn5V45C4wwjs.json', 'var_call_jmqELJpiXJqDN2kbXqABdEVi': 'file_storage/call_jmqELJpiXJqDN2kbXqABdEVi.json', 'var_call_fWMTTXKSyQYmQk3gHgrO9qa4': 'file_storage/call_fWMTTXKSyQYmQk3gHgrO9qa4.json', 'var_call_tMrpsjXLUaU7I7dNMRXVXkhG': [{'repo_name': 'torvalds/linux', 'count': 13413}, {'repo_name': 'twbs/bootstrap', 'count': 251}, {'repo_name': 'Microsoft/vscode', 'count': 171}, {'repo_name': 'apple/swift', 'count': 963}, {'repo_name': 'facebook/react', 'count': 104}, {'repo_name': 'tensorflow/tensorflow', 'count': 114}]}

exec(code, env_args)
