code = """import json, pandas as pd, re

# load repos without python
v = var_call_IGX24xuPhnS4xBc7jW5qTAtS
if isinstance(v, str):
    with open(v, 'r', encoding='utf-8') as f:
        v = json.load(f)
no_py = set(r['repo_name'] for r in v)

# load readmes
r = var_call_ZS0khV9pDzMOkqg8xReLHGfT
if isinstance(r, str):
    with open(r, 'r', encoding='utf-8') as f:
        r = json.load(f)

# heuristic: copyright info
pat = re.compile(r"(?is)(\bcopyright\b|\b\(c\)\b|\b©\b|all rights reserved)")

seen_repo = set()
has_copyright = set()
for rec in r:
    repo = rec.get('repo_name')
    if repo not in no_py:
        continue
    if repo in seen_repo:
        # multiple readme.md blobs possible; treat as positive if any contains copyright
        pass
    seen_repo.add(repo)
    content = rec.get('content') or ''
    if pat.search(content):
        has_copyright.add(repo)

numer = len(has_copyright)
denom = len(seen_repo)
prop = (numer/denom) if denom else None
out = {
    'non_python_repos_with_readme_md_count': denom,
    'with_copyright_count': numer,
    'proportion': prop
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_IGX24xuPhnS4xBc7jW5qTAtS': 'file_storage/call_IGX24xuPhnS4xBc7jW5qTAtS.json', 'var_call_ZS0khV9pDzMOkqg8xReLHGfT': 'file_storage/call_ZS0khV9pDzMOkqg8xReLHGfT.json'}

exec(code, env_args)
