code = """import json, re
# Load the non-Python repo list (stored as a JSON file path)
with open(var_call_bhXJaeUmxiyN0n2C68PDm526, 'r') as f:
    non_python_records = json.load(f)

non_python_repos = set()
for r in non_python_records:
    # normalize repo names
    name = r.get('repo_name')
    if name:
        non_python_repos.add(name)

# Load the README contents
with open(var_call_KYSX19bAo36npovkiGjTgfb6, 'r') as f:
    readme_records = json.load(f)

# Map repo -> list of readme contents
from collections import defaultdict
readmes_by_repo = defaultdict(list)
for rec in readme_records:
    repo = rec.get('sample_repo_name')
    content = rec.get('content')
    if repo and content is not None:
        readmes_by_repo[repo].append(content)

# Consider only non-Python repos
non_python_with_readme = set(readmes_by_repo.keys()) & non_python_repos

# Define regex for copyright detection
pattern = re.compile(r"copyright|\u00A9|\u00a9|all rights reserved|copyright\s*\(c\)", re.IGNORECASE)

num_with_copyright = 0
for repo in non_python_with_readme:
    contents = readmes_by_repo.get(repo, [])
    found = False
    for c in contents:
        if pattern.search(c):
            found = True
            break
    if found:
        num_with_copyright += 1

 denom = len(non_python_with_readme)

proportion = None
if denom > 0:
    proportion = num_with_copyright / denom

result = {
    'non_python_repos_with_readme': denom,
    'readmes_with_copyright': num_with_copyright,
    'proportion': proportion
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_bhXJaeUmxiyN0n2C68PDm526': 'file_storage/call_bhXJaeUmxiyN0n2C68PDm526.json', 'var_call_KYSX19bAo36npovkiGjTgfb6': 'file_storage/call_KYSX19bAo36npovkiGjTgfb6.json'}

exec(code, env_args)
