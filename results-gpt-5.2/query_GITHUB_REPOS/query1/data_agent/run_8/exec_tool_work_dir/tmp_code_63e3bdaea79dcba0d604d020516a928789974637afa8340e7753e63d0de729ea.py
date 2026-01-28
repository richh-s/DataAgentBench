code = """import json, re
import pandas as pd

# Load repo list (non-Python)
repos_src = var_call_KlN7CFfvqsVyXZRLZLY9AyaV
if isinstance(repos_src, str) and repos_src.endswith('.json'):
    with open(repos_src, 'r', encoding='utf-8') as f:
        repos_records = json.load(f)
else:
    repos_records = repos_src
non_py_repos = set(r['repo_name'] for r in repos_records if r.get('repo_name') is not None)

# Load README.md contents
readmes_src = var_call_8aSHRIutmZoi8ZvPMshVWEQS
if isinstance(readmes_src, str) and readmes_src.endswith('.json'):
    with open(readmes_src, 'r', encoding='utf-8') as f:
        readme_records = json.load(f)
else:
    readme_records = readmes_src

# Keep only readmes from non-python repos
readme_by_repo = {}
for r in readme_records:
    repo = r.get('repo_name')
    if repo in non_py_repos and repo not in readme_by_repo:
        # if multiple, keep first
        readme_by_repo[repo] = r.get('content')

# Heuristic for copyright info
pattern = re.compile(r'(?:\bcopyright\b|\b©\b|\ball rights reserved\b)', re.IGNORECASE)

total = len(readme_by_repo)
with_copyright = sum(1 for c in readme_by_repo.values() if isinstance(c, str) and pattern.search(c or ''))

prop = (with_copyright / total) if total else None

out = {
    'non_python_repos_with_readme_md_count': total,
    'readme_md_with_copyright_count': with_copyright,
    'proportion': prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_KlN7CFfvqsVyXZRLZLY9AyaV': 'file_storage/call_KlN7CFfvqsVyXZRLZLY9AyaV.json', 'var_call_8aSHRIutmZoi8ZvPMshVWEQS': 'file_storage/call_8aSHRIutmZoi8ZvPMshVWEQS.json'}

exec(code, env_args)
