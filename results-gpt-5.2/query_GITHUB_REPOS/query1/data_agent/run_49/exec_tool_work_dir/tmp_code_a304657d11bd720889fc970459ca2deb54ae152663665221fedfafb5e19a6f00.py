code = """import json, pandas as pd, re

# Load repo list (non-Python)
repo_path = var_call_o9C1SfQpNNrdfH1OpYM5TaYh
with open(repo_path, 'r', encoding='utf-8') as f:
    non_py = json.load(f)
non_py_set = set(r['repo_name'] for r in non_py if r.get('repo_name'))

# Load readmes
readme_path = var_call_mbtI1DDv5HqSMyVT7RYtFD4Z
with open(readme_path, 'r', encoding='utf-8') as f:
    readmes = json.load(f)

def has_copyright(txt: str) -> bool:
    if txt is None:
        return False
    t = txt.lower()
    # common patterns: 'copyright', '(c)', '©'
    if 'copyright' in t:
        return True
    if '©' in txt:
        return True
    if re.search(r'\(c\)\s*\d{2,4}', t):
        return True
    if re.search(r'\bcopyright\s*\(c\)', t):
        return True
    return False

# For each repo among non-py, check if it has a README.md row and whether any README contains copyright
repo_to_has = {}
repo_to_any = {}
for r in readmes:
    repo = r.get('repo_name')
    if repo not in non_py_set:
        continue
    repo_to_any[repo] = True
    if has_copyright(r.get('content') or ''):
        repo_to_has[repo] = True

n_with_readme = len(repo_to_any)
n_with_copyright = sum(1 for repo in repo_to_any if repo_to_has.get(repo, False))
prop = (n_with_copyright / n_with_readme) if n_with_readme else None

result = {
    'non_python_repos_with_readme_md': n_with_readme,
    'non_python_repos_with_copyright_in_readme_md': n_with_copyright,
    'proportion': prop
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_o9C1SfQpNNrdfH1OpYM5TaYh': 'file_storage/call_o9C1SfQpNNrdfH1OpYM5TaYh.json', 'var_call_mbtI1DDv5HqSMyVT7RYtFD4Z': 'file_storage/call_mbtI1DDv5HqSMyVT7RYtFD4Z.json'}

exec(code, env_args)
