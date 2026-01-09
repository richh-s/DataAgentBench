code = """import json, re
import pandas as pd

# Load repo list (non-python) from file if needed
nonpy = var_call_Xgtg1NeuROO3jgK3dxXMDShn
if isinstance(nonpy, str):
    with open(nonpy, 'r', encoding='utf-8') as f:
        nonpy = json.load(f)
nonpy_set = set(r['repo_name'] for r in nonpy)

readmes = var_call_939gDnmG3cL93WONIPAhj3KR
if isinstance(readmes, str):
    with open(readmes, 'r', encoding='utf-8') as f:
        readmes = json.load(f)

def has_copyright(text: str) -> bool:
    if text is None:
        return False
    t = text.lower()
    # Common forms: "copyright", "(c)", "©", "all rights reserved"
    if 'copyright' in t:
        return True
    if 'all rights reserved' in t:
        return True
    if '©' in text or '(c)' in t:
        return True
    return False

# Only consider repos that are non-python AND have a README.md content row
eligible = 0
with_c = 0
seen = set()
for r in readmes:
    repo = r.get('repo_name')
    if repo not in nonpy_set:
        continue
    # If multiple readme.md rows per repo, treat as repo-level: any contains copyright
    if repo not in seen:
        seen.add(repo)
        eligible += 1
    if has_copyright(r.get('content','')):
        # mark as with copyright
        # ensure we count once
        # use a separate set
        pass

# second pass with set
with_set = set()
for r in readmes:
    repo = r.get('repo_name')
    if repo not in nonpy_set:
        continue
    if repo in with_set:
        continue
    if has_copyright(r.get('content','')):
        with_set.add(repo)

with_c = len(with_set)
prop = (with_c / eligible) if eligible else None

out = {
    "non_python_repos_with_readme_md": eligible,
    "with_copyright": with_c,
    "proportion": prop
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Xgtg1NeuROO3jgK3dxXMDShn': 'file_storage/call_Xgtg1NeuROO3jgK3dxXMDShn.json', 'var_call_939gDnmG3cL93WONIPAhj3KR': 'file_storage/call_939gDnmG3cL93WONIPAhj3KR.json'}

exec(code, env_args)
