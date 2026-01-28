code = """import json

# Load metadata repo list
v1 = var_call_X6gq46gfmNqTpA50tyG3TVTO
if isinstance(v1, str):
    with open(v1, 'r', encoding='utf-8') as f:
        metadata = json.load(f)
else:
    metadata = v1

# Load commits filtered by message constraints
v2 = var_call_NtJhBdOJkmJp8f2zB6Um8H8r
if isinstance(v2, str):
    with open(v2, 'r', encoding='utf-8') as f:
        commits = json.load(f)
else:
    commits = v2

# Build set of repo names from metadata
repo_set = set()
for item in metadata:
    rn = item.get('repo_name')
    if rn:
        repo_set.add(rn)

# Count commits whose repo_name is in repo_set
count = 0
for c in commits:
    rn = c.get('repo_name')
    if rn in repo_set:
        # message already satisfies non-null, length<1000 and not starting with merge/update/test
        count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_call_X6gq46gfmNqTpA50tyG3TVTO': 'file_storage/call_X6gq46gfmNqTpA50tyG3TVTO.json', 'var_call_jluADJdlTOOlitaeWMueVrZ6': 'file_storage/call_jluADJdlTOOlitaeWMueVrZ6.json', 'var_call_NtJhBdOJkmJp8f2zB6Um8H8r': 'file_storage/call_NtJhBdOJkmJp8f2zB6Um8H8r.json'}

exec(code, env_args)
