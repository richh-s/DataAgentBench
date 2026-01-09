code = """import json, re
import pandas as pd

# Load non-python repos
npr = var_call_dIrge5tho92RCXj1UnsPdQmt
if isinstance(npr, str):
    with open(npr, 'r', encoding='utf-8') as f:
        npr = json.load(f)
non_python_repos = set(r['repo_name'] for r in npr)

# Load readme contents
rc = var_call_rnpbYFAwSaxvcwcTPqaQNtCR
if isinstance(rc, str):
    with open(rc, 'r', encoding='utf-8') as f:
        rc = json.load(f)

# For each repo, pick any README.md content (if multiple refs/duplicates exist)
readme_by_repo = {}
for r in rc:
    repo = r.get('repo_name')
    if repo is None:
        continue
    if repo in readme_by_repo:
        continue
    readme_by_repo[repo] = r.get('content')

# Intersect repos that are non-python and have README.md
repos_with_readme = non_python_repos.intersection(readme_by_repo.keys())

# Detect copyright info
pat = re.compile(r"(?i)(copyright\s*(?:\(c\)|©)?\s*(?:\d{4}(?:\s*[-–]\s*\d{2,4})?)?)|\b©\b")

def has_copyright(txt):
    if txt is None:
        return False
    return bool(pat.search(txt))

num_total = len(repos_with_readme)
num_with_c = sum(1 for repo in repos_with_readme if has_copyright(readme_by_repo.get(repo)))
prop = (num_with_c / num_total) if num_total else None

out = {
    'non_python_repos_with_readme_md': num_total,
    'readme_md_with_copyright': num_with_c,
    'proportion': prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_dIrge5tho92RCXj1UnsPdQmt': 'file_storage/call_dIrge5tho92RCXj1UnsPdQmt.json', 'var_call_rnpbYFAwSaxvcwcTPqaQNtCR': 'file_storage/call_rnpbYFAwSaxvcwcTPqaQNtCR.json'}

exec(code, env_args)
