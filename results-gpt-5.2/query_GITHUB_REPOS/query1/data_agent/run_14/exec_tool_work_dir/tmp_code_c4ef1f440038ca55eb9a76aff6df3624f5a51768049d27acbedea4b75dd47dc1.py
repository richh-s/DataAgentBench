code = """import json, re
import pandas as pd

# Load no-python repos
no_py = var_call_hCKdiNRHY8m91Szb5nlpFR1y
if isinstance(no_py, str) and no_py.endswith('.json'):
    with open(no_py, 'r', encoding='utf-8') as f:
        no_py = json.load(f)
no_py_set = set(r['repo_name'] for r in no_py)

# Load README.md contents
readmes = var_call_gnouq2gFMeouiPVUVi0q9cRI
if isinstance(readmes, str) and readmes.endswith('.json'):
    with open(readmes, 'r', encoding='utf-8') as f:
        readmes = json.load(f)

# Filter to repos that do not use Python
rows = [r for r in readmes if r.get('repo_name') in no_py_set]

# Deduplicate multiple README.md rows per repo by taking first non-null content
repo_to_content = {}
for r in rows:
    repo = r.get('repo_name')
    content = r.get('content')
    if repo not in repo_to_content:
        repo_to_content[repo] = content
    else:
        # prefer non-empty content
        if (repo_to_content[repo] is None or repo_to_content[repo] == '') and content:
            repo_to_content[repo] = content

# Heuristic for copyright info
pat = re.compile(r'\bcopyright\b|\b©\b|\ball rights reserved\b', re.IGNORECASE)

total = len(repo_to_content)
with_c = 0
for repo, content in repo_to_content.items():
    if isinstance(content, str) and pat.search(content):
        with_c += 1

prop = (with_c / total) if total else None
result = {
    "non_python_repos_with_readme_md_count": total,
    "readme_with_copyright_count": with_c,
    "proportion": prop
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hCKdiNRHY8m91Szb5nlpFR1y': 'file_storage/call_hCKdiNRHY8m91Szb5nlpFR1y.json', 'var_call_gnouq2gFMeouiPVUVi0q9cRI': 'file_storage/call_gnouq2gFMeouiPVUVi0q9cRI.json'}

exec(code, env_args)
