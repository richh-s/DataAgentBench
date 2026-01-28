code = """import json
import os

# Access variables from previous tool calls
meta_var = var_call_zYb6fXoqtBkzDc1PAh5wwL9Q
commits_var = var_call_cpGJIth0ZsF8cTy1xos3Dk9H

def load_storage(var):
    # If var is a string path to a .json file, open and load it
    if isinstance(var, str) and os.path.exists(var):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    # Otherwise assume it's already a list-like object
    return var

meta_records = load_storage(meta_var)
commit_records = load_storage(commits_var)

# Extract repo names from metadata
meta_repos = set()
for r in meta_records:
    # Each record expected to be a dict with 'repo_name'
    if isinstance(r, dict) and 'repo_name' in r:
        meta_repos.add(r['repo_name'])

# Count commits whose repo_name is in meta_repos
count = 0
for c in commit_records:
    if isinstance(c, dict) and 'repo_name' in c:
        if c['repo_name'] in meta_repos:
            count += 1

import json
print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_zYb6fXoqtBkzDc1PAh5wwL9Q': 'file_storage/call_zYb6fXoqtBkzDc1PAh5wwL9Q.json', 'var_call_cpGJIth0ZsF8cTy1xos3Dk9H': 'file_storage/call_cpGJIth0ZsF8cTy1xos3Dk9H.json'}

exec(code, env_args)
