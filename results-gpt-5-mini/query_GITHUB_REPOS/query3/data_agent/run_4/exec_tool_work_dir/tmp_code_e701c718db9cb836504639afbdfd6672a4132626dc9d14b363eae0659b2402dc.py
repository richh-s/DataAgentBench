code = """import json
# Load metadata repos (file path stored in var_call_nDatpTdGQL5akoYvA6iJHGRT)
with open(var_call_nDatpTdGQL5akoYvA6iJHGRT, 'r') as f:
    md = json.load(f)
# Load commits (file path stored in var_call_sWXjgBmBdRVQPeSbJhNqKTRA)
with open(var_call_sWXjgBmBdRVQPeSbJhNqKTRA, 'r') as f:
    commits = json.load(f)

# Build set of repo_names from metadata
md_repos = {rec['repo_name'] for rec in md if 'repo_name' in rec}

# Count commits whose repo_name is in md_repos
count = 0
for c in commits:
    rn = c.get('repo_name')
    if rn in md_repos:
        # message should already satisfy filters from the previous query, but double-check
        msg = c.get('message')
        if msg and len(msg) < 1000:
            lm = msg.lstrip().lower()
            if not (lm.startswith('merge') or lm.startswith('update') or lm.startswith('test')):
                count += 1

# Print result in required format
print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_nDatpTdGQL5akoYvA6iJHGRT': 'file_storage/call_nDatpTdGQL5akoYvA6iJHGRT.json', 'var_call_sB3ZhG5aLTNkfRTpNHrh55gu': 'file_storage/call_sB3ZhG5aLTNkfRTpNHrh55gu.json', 'var_call_sWXjgBmBdRVQPeSbJhNqKTRA': 'file_storage/call_sWXjgBmBdRVQPeSbJhNqKTRA.json'}

exec(code, env_args)
