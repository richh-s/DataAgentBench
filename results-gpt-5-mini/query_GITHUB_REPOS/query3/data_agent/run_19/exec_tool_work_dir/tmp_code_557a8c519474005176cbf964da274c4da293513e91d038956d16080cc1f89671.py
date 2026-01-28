code = """import json
# Load the metadata repo list and commits list from the files whose paths are provided
with open(var_call_nYkOB7RwqDl9hvfZ22HF8VYy, 'r') as f:
    metadata_list = json.load(f)
with open(var_call_LJuumEH30wXIS25dNWLb0NWk, 'r') as f:
    commits_list = json.load(f)

# Build set of repo names from metadata (repositories that use Shell and have Apache-2.0)
repo_set = set()
for item in metadata_list:
    rn = item.get('repo_name')
    if rn:
        repo_set.add(rn)

# Count commits whose repo_name is in repo_set and have a message (commits_list already filtered)
count = 0
for c in commits_list:
    if c.get('repo_name') in repo_set and c.get('message') is not None:
        count += 1

import json as _json
print("__RESULT__:")
print(_json.dumps(count))"""

env_args = {'var_call_nYkOB7RwqDl9hvfZ22HF8VYy': 'file_storage/call_nYkOB7RwqDl9hvfZ22HF8VYy.json', 'var_call_LJuumEH30wXIS25dNWLb0NWk': 'file_storage/call_LJuumEH30wXIS25dNWLb0NWk.json'}

exec(code, env_args)
