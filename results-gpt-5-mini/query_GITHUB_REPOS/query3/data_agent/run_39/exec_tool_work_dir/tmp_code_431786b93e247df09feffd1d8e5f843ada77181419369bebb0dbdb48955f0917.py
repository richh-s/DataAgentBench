code = """import json

# Load the large results from previous tool calls (file paths)
with open(var_call_qo0gHezLmYnhKJNSVN5HPIMw, 'r') as f:
    metadata_repos = json.load(f)
with open(var_call_PmuVrQaoK3V6hpYZcOywGNS6, 'r') as f:
    commits = json.load(f)

# Build set of repo_names from metadata query
metadata_repo_set = set()
for r in metadata_repos:
    # guard for dicts with repo_name
    name = r.get('repo_name') if isinstance(r, dict) else None
    if name:
        metadata_repo_set.add(name)

# Count commits whose repo_name is in the metadata set
count = 0
for c in commits:
    rn = c.get('repo_name') if isinstance(c, dict) else None
    if rn and rn in metadata_repo_set:
        count += 1

import json
print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_qo0gHezLmYnhKJNSVN5HPIMw': 'file_storage/call_qo0gHezLmYnhKJNSVN5HPIMw.json', 'var_call_PmuVrQaoK3V6hpYZcOywGNS6': 'file_storage/call_PmuVrQaoK3V6hpYZcOywGNS6.json'}

exec(code, env_args)
