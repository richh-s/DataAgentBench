code = """import json

# Load the repo list (may be a file path)
path_langs = var_call_BcBHpB5HKV2i1XslcUBlO2AR
with open(path_langs, 'r') as f:
    langs = json.load(f)

path_commits = var_call_pPVXc33jLps527RL1ljZFaeP
with open(path_commits, 'r') as f:
    commits = json.load(f)

# Build set of target repo names (lowercased for safe matching)
repo_set = set(r['repo_name'].lower() for r in langs if 'repo_name' in r)

# Count commits whose repo_name is in the repo_set
count = 0
for c in commits:
    rn = c.get('repo_name', '')
    if rn and rn.lower() in repo_set:
        count += 1

import json as _json
print("__RESULT__:")
print(_json.dumps(count))"""

env_args = {'var_call_BcBHpB5HKV2i1XslcUBlO2AR': 'file_storage/call_BcBHpB5HKV2i1XslcUBlO2AR.json', 'var_call_pPVXc33jLps527RL1ljZFaeP': 'file_storage/call_pPVXc33jLps527RL1ljZFaeP.json'}

exec(code, env_args)
