code = """import json, re, pandas as pd

# load non-python repos
non_py = var_call_7VEG3pYy8g9IDj64f9wYKw31
if isinstance(non_py, str):
    with open(non_py, 'r', encoding='utf-8') as f:
        non_py = json.load(f)
non_py_set = set(r['repo_name'] for r in non_py)

# load readmes
readmes = var_call_mTz7x3SPmBK0BJADfdHsQgJx
if isinstance(readmes, str):
    with open(readmes, 'r', encoding='utf-8') as f:
        readmes = json.load(f)

# for repos, there can be multiple refs; count repo once if any README has copyright
# heuristic: look for 'copyright' word or © symbol
pat = re.compile(r'(copyright|\u00a9|©)', re.IGNORECASE)

repo_has = {}
for r in readmes:
    repo = r.get('repo_name')
    if repo not in non_py_set:
        continue
    content = r.get('content') or ''
    if repo not in repo_has:
        repo_has[repo] = False
    if (not repo_has[repo]) and pat.search(content):
        repo_has[repo] = True

# denominator: non-python repos that have a README.md captured
n_with_readme = len(repo_has)
n_with_copyright = sum(1 for v in repo_has.values() if v)
prop = (n_with_copyright / n_with_readme) if n_with_readme else None

out = {
    'non_python_repos_with_readme': n_with_readme,
    'with_copyright_in_readme': n_with_copyright,
    'proportion': prop
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_7VEG3pYy8g9IDj64f9wYKw31': 'file_storage/call_7VEG3pYy8g9IDj64f9wYKw31.json', 'var_call_mTz7x3SPmBK0BJADfdHsQgJx': 'file_storage/call_mTz7x3SPmBK0BJADfdHsQgJx.json'}

exec(code, env_args)
