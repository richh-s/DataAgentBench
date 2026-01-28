code = """import json, re
import pandas as pd

# Load non-python repos
non_py = var_call_9DOiziIio300zVisxZolWwS8
if isinstance(non_py, str):
    with open(non_py, 'r', encoding='utf-8') as f:
        non_py = json.load(f)
non_py_set = set(r['repo_name'] for r in non_py)

# Load readmes
readmes = var_call_avhLSQJtOkjzLWTJNyFrxRBY
if isinstance(readmes, str):
    with open(readmes, 'r', encoding='utf-8') as f:
        readmes = json.load(f)

# For each repo, consider README.md exists if we have at least one record
# If multiple README.md contents per repo, mark as containing copyright if any does.

copyright_re = re.compile(r"(?is)\b(copyright|©|\(c\))\b")

has_readme = set()
has_copyright = set()

for r in readmes:
    repo = r.get('repo_name')
    if repo is None:
        continue
    if repo not in non_py_set:
        continue
    has_readme.add(repo)
    content = r.get('content') or ''
    if copyright_re.search(content):
        has_copyright.add(repo)

n_non_py = len(non_py_set)
# Proportion among non-python repos with a README.md sampled in contents
n_with_readme = len(has_readme)
prop = (len(has_copyright) / n_with_readme) if n_with_readme else None

out = {
    "non_python_repos_total": n_non_py,
    "non_python_repos_with_readme_md": n_with_readme,
    "non_python_repos_with_readme_md_and_copyright": len(has_copyright),
    "proportion": prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_9DOiziIio300zVisxZolWwS8': 'file_storage/call_9DOiziIio300zVisxZolWwS8.json', 'var_call_avhLSQJtOkjzLWTJNyFrxRBY': 'file_storage/call_avhLSQJtOkjzLWTJNyFrxRBY.json'}

exec(code, env_args)
