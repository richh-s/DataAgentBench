code = """import json, re
import pandas as pd

# Load non-python repos
nonpy = var_call_za6iqrx5LaBNA8e4Tlb1fHDE
if isinstance(nonpy, str):
    with open(nonpy, 'r', encoding='utf-8') as f:
        nonpy = json.load(f)
nonpy_set = set(r['repo_name'] for r in nonpy)

# Load readmes
readmes = var_call_OUryV8lKLY3OPVYkrMpfE67i
if isinstance(readmes, str):
    with open(readmes, 'r', encoding='utf-8') as f:
        readmes = json.load(f)

# For each repo, only consider if it's in non-python set and has a README.md content record
# If multiple README.md rows per repo, consider it includes copyright if any row matches.

pat = re.compile(r"(?i)(?:\bcopyright\b|\(c\)|©)")

repo_has_readme = {}
repo_has_copyright = {}
for r in readmes:
    repo = r.get('repo_name')
    if repo not in nonpy_set:
        continue
    repo_has_readme[repo] = True
    content = r.get('content') or ''
    if pat.search(content):
        repo_has_copyright[repo] = True

n_with_readme = len(repo_has_readme)
# proportion among repos (non-python) that have README.md available in artifacts
n_with_c = sum(1 for repo in repo_has_readme if repo_has_copyright.get(repo, False))
prop = (n_with_c / n_with_readme) if n_with_readme else None

out = {
    "non_python_repos_with_readme_md": n_with_readme,
    "with_copyright": n_with_c,
    "proportion": prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_za6iqrx5LaBNA8e4Tlb1fHDE': 'file_storage/call_za6iqrx5LaBNA8e4Tlb1fHDE.json', 'var_call_OUryV8lKLY3OPVYkrMpfE67i': 'file_storage/call_OUryV8lKLY3OPVYkrMpfE67i.json'}

exec(code, env_args)
