code = """import json, re, pandas as pd

# Load repo list (non-python)
nonpython = var_call_PPqjA3N6CSJWQ8obkU1KUOLx
if isinstance(nonpython, str):
    with open(nonpython, 'r', encoding='utf-8') as f:
        nonpython = json.load(f)
nonpython_set = {r['repo_name'] for r in nonpython if r.get('repo_name') is not None}

# Load readmes
readmes = var_call_4Q3aFjQ3HBBZqtA7Cd8ubbQG
if isinstance(readmes, str):
    with open(readmes, 'r', encoding='utf-8') as f:
        readmes = json.load(f)

# Filter to nonpython repos and de-duplicate by repo (if multiple readmes, treat as any contains)
# Define copyright detection
pat = re.compile(r"(?i)(?:copyright\s*(?:\(c\)|©)?\s*\d{0,4}|\b©\b)")

repo_has_readme = {}
repo_has_copyright = {}

for r in readmes:
    repo = r.get('repo_name')
    if repo not in nonpython_set:
        continue
    content = r.get('content') or ''
    repo_has_readme[repo] = True
    if pat.search(content):
        repo_has_copyright[repo] = True

n_readme = len(repo_has_readme)
n_copyright = sum(1 for repo in repo_has_readme if repo_has_copyright.get(repo, False))
prop = (n_copyright / n_readme) if n_readme else None

out = {
    "nonpython_repos_with_readme_md": n_readme,
    "with_copyright_in_readme_md": n_copyright,
    "proportion": prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_PPqjA3N6CSJWQ8obkU1KUOLx': 'file_storage/call_PPqjA3N6CSJWQ8obkU1KUOLx.json', 'var_call_4Q3aFjQ3HBBZqtA7Cd8ubbQG': 'file_storage/call_4Q3aFjQ3HBBZqtA7Cd8ubbQG.json'}

exec(code, env_args)
