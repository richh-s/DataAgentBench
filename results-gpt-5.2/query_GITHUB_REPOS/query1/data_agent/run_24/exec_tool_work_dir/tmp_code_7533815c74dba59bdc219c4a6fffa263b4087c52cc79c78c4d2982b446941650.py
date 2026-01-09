code = """import json, re
import pandas as pd

# Load non-python repos
non_py = var_call_y86PDA03EJSB4yDMMZG6jwxB
if isinstance(non_py, str):
    with open(non_py, 'r', encoding='utf-8') as f:
        non_py = json.load(f)
non_py_repos = set(r['repo_name'] for r in non_py)

# Load readmes
readmes = var_call_OSqIcj9S6L7H0r7ayla0SwYz
if isinstance(readmes, str):
    with open(readmes, 'r', encoding='utf-8') as f:
        readmes = json.load(f)

# Keep one README per repo (if multiple refs/paths collapsed already)
# Determine copyright presence
pat = re.compile(r'(?:copyright\s*\(c\)|copyright\s*©|copyright\s+\d{4}|©\s*\d{4}|\bcopy(?:right)?\b\s*\d{4})', re.IGNORECASE)

def has_copyright(text):
    if text is None:
        return False
    return bool(pat.search(text))

# For each non-python repo, check if it has README and whether any README has copyright
repo_to_flag = {}
for r in readmes:
    repo = r.get('repo_name')
    if repo not in non_py_repos:
        continue
    flag = has_copyright(r.get('content',''))
    repo_to_flag[repo] = repo_to_flag.get(repo, False) or flag

n_non_py = len(non_py_repos)
repos_with_readme = set(repo_to_flag.keys())
# proportion among non-python repos that have README.md and include copyright
n_with_copyright = sum(1 for repo in non_py_repos if repo_to_flag.get(repo, False))
prop = (n_with_copyright / n_non_py) if n_non_py else None

out = {
    'non_python_repo_count': n_non_py,
    'non_python_repos_with_readme_md_count': len(repos_with_readme),
    'non_python_repos_with_readme_md_and_copyright_count': n_with_copyright,
    'proportion': prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_y86PDA03EJSB4yDMMZG6jwxB': 'file_storage/call_y86PDA03EJSB4yDMMZG6jwxB.json', 'var_call_OSqIcj9S6L7H0r7ayla0SwYz': 'file_storage/call_OSqIcj9S6L7H0r7ayla0SwYz.json'}

exec(code, env_args)
