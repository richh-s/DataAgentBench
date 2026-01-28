code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

langs = load_records(var_call_i7b5dg6Qvzpip28OZqUHckcD)
readmes = load_records(var_call_C6UPJnvs9s6Zk1lq9DZM2ARl)

non_python_repos = {r['repo_name'] for r in langs if r.get('repo_name')}

# One README.md per repo: if multiple, mark as having copyright if any does.
# Detect typical copyright markers.
pat = re.compile(r"(?is)\bcopyright\b|\(c\)\s*\d{2,4}|©\s*\d{2,4}|\ball rights reserved\b")

repo_has_readme = {}
repo_has_copyright = {}

for r in readmes:
    repo = r.get('repo_name')
    if not repo or repo not in non_python_repos:
        continue
    repo_has_readme[repo] = True
    content = r.get('content') or ''
    if pat.search(content):
        repo_has_copyright[repo] = True

n_with_readme = len(repo_has_readme)
n_with_copyright = sum(1 for repo in repo_has_readme if repo_has_copyright.get(repo, False))
prop = (n_with_copyright / n_with_readme) if n_with_readme else None

out = {
    "non_python_repos_with_README_md": n_with_readme,
    "with_copyright_in_README_md": n_with_copyright,
    "proportion": prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_i7b5dg6Qvzpip28OZqUHckcD': 'file_storage/call_i7b5dg6Qvzpip28OZqUHckcD.json', 'var_call_C6UPJnvs9s6Zk1lq9DZM2ARl': 'file_storage/call_C6UPJnvs9s6Zk1lq9DZM2ARl.json'}

exec(code, env_args)
