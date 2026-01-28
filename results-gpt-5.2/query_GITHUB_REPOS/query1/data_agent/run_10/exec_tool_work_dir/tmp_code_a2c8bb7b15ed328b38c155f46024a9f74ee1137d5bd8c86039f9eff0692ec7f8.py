code = """import json, re, pandas as pd

# load repo list (non-python)
non_py = var_call_i9ExtFkapGPijElhntm1uXj2
if isinstance(non_py, str):
    with open(non_py, 'r', encoding='utf-8') as f:
        non_py = json.load(f)
non_py_set = set(r['repo_name'] for r in non_py)

# load readmes
readmes = var_call_VGCEyCN5VwqZSuzI9CRsSWe6
if isinstance(readmes, str):
    with open(readmes, 'r', encoding='utf-8') as f:
        readmes = json.load(f)

# keep first README per repo (any ref) 
readme_by_repo = {}
for r in readmes:
    rn = r.get('repo_name')
    if rn in non_py_set and rn not in readme_by_repo:
        readme_by_repo[rn] = r.get('content') or ''

# heuristic for copyright info
pat = re.compile(r'(?:copyright\s*(?:\(c\))?\s*\d{2,4}|©\s*\d{2,4}|\bcopyright\b)', re.IGNORECASE)

numerator = 0
for rn, txt in readme_by_repo.items():
    if pat.search(txt or ''):
        numerator += 1

denominator = len(readme_by_repo)  # repos w/ README.md among non-python repos
prop = (numerator / denominator) if denominator else None

out = {
    "non_python_repos_with_readme_md": denominator,
    "readmes_with_copyright": numerator,
    "proportion": prop
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_i9ExtFkapGPijElhntm1uXj2': 'file_storage/call_i9ExtFkapGPijElhntm1uXj2.json', 'var_call_VGCEyCN5VwqZSuzI9CRsSWe6': 'file_storage/call_VGCEyCN5VwqZSuzI9CRsSWe6.json'}

exec(code, env_args)
