code = """import json, re
import pandas as pd

# Load languages not including Python
lang_src = var_call_qApXCTP4CX9NUKzQlsIX8sFX
if isinstance(lang_src, str):
    with open(lang_src, 'r', encoding='utf-8') as f:
        lang_rows = json.load(f)
else:
    lang_rows = lang_src

readme_src = var_call_4quZKypKfuZ1GwpjuNDq6fmv
if isinstance(readme_src, str):
    with open(readme_src, 'r', encoding='utf-8') as f:
        readme_rows = json.load(f)
else:
    readme_rows = readme_src

non_python_repos = set(r['repo_name'] for r in lang_rows if r.get('repo_name') is not None)

# dedupe README per repo: if multiple, consider includes copyright if any includes
# copyright detection: case-insensitive 'copyright' or '(c)' or '©'
pat = re.compile(r'(copyright|\(c\)|©)', re.IGNORECASE)

repo_has_readme = set()
repo_has_copyright = set()

for r in readme_rows:
    repo = r.get('repo_name')
    if repo in non_python_repos:
        repo_has_readme.add(repo)
        content = r.get('content') or ''
        if pat.search(content):
            repo_has_copyright.add(repo)

num_with_readme = len(repo_has_readme)
num_with_copyright = len(repo_has_copyright)
prop = (num_with_copyright / num_with_readme) if num_with_readme else None

out = {
    "non_python_repos_with_readme_md": num_with_readme,
    "with_copyright_in_readme_md": num_with_copyright,
    "proportion": prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_qApXCTP4CX9NUKzQlsIX8sFX': 'file_storage/call_qApXCTP4CX9NUKzQlsIX8sFX.json', 'var_call_4quZKypKfuZ1GwpjuNDq6fmv': 'file_storage/call_4quZKypKfuZ1GwpjuNDq6fmv.json'}

exec(code, env_args)
