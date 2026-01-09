code = """import json, re, pandas as pd

# load non-python repos
nonpy = var_call_0H4ZlPO2gg5lPYoIQsfBsYMM
if isinstance(nonpy, str):
    with open(nonpy, 'r', encoding='utf-8') as f:
        nonpy = json.load(f)
nonpy_set = set(r['repo_name'] for r in nonpy)

# load readmes
readmes = var_call_4g51fXAFUiFF35ELehqNY1lS
if isinstance(readmes, str):
    with open(readmes, 'r', encoding='utf-8') as f:
        readmes = json.load(f)

# keep only readmes for non-python repos
filtered = [r for r in readmes if r.get('repo_name') in nonpy_set]

# heuristic: copyright info
pat = re.compile(r"(?is)(copyright\s*(?:\(c\)|©)?\s*\d{0,4}|\b©\s*\d{0,4}|all\s+rights\s+reserved)")

repos_with_readme = set()
repos_with_copyright = set()
for r in filtered:
    repo = r.get('repo_name')
    content = r.get('content') or ''
    repos_with_readme.add(repo)
    if pat.search(content):
        repos_with_copyright.add(repo)

den = len(repos_with_readme)
num = len(repos_with_copyright)
prop = (num/den) if den else None

out = {
    'non_python_repos_with_readme_md': den,
    'non_python_repos_readme_with_copyright': num,
    'proportion': prop
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0H4ZlPO2gg5lPYoIQsfBsYMM': 'file_storage/call_0H4ZlPO2gg5lPYoIQsfBsYMM.json', 'var_call_4g51fXAFUiFF35ELehqNY1lS': 'file_storage/call_4g51fXAFUiFF35ELehqNY1lS.json'}

exec(code, env_args)
