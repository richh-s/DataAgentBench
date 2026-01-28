code = """import json, re
import pandas as pd

# Load languages (may be file path)
langs_src = var_call_um0qbhX8ZsqezDP1rpO0bRhT
if isinstance(langs_src, str):
    with open(langs_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = langs_src

readmes_src = var_call_FDPEwBZNWI9khg3sE5BX1zch
if isinstance(readmes_src, str):
    with open(readmes_src, 'r', encoding='utf-8') as f:
        readmes = json.load(f)
else:
    readmes = readmes_src

# Determine repos that do NOT use Python (any mention of Python in language_description)
py_re = re.compile(r'\bpython\b', re.IGNORECASE)
non_python_repos = set()
for r in langs:
    desc = r.get('language_description') or ''
    if not py_re.search(desc):
        non_python_repos.add(r['repo_name'])

# Among those repos with README.md content, check for copyright info
# Define copyright heuristic: presence of 'copyright' or '(c)' or '©'
cr_re = re.compile(r'(copyright|\(c\)|©)', re.IGNORECASE)

total = 0
with_cr = 0
for r in readmes:
    repo = r.get('repo_name')
    if repo in non_python_repos:
        total += 1
        content = r.get('content') or ''
        if cr_re.search(content):
            with_cr += 1

prop = None
if total > 0:
    prop = with_cr / total

out = {
    "non_python_repos_with_readme_md": total,
    "readme_md_with_copyright": with_cr,
    "proportion": prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_um0qbhX8ZsqezDP1rpO0bRhT': 'file_storage/call_um0qbhX8ZsqezDP1rpO0bRhT.json', 'var_call_FDPEwBZNWI9khg3sE5BX1zch': 'file_storage/call_FDPEwBZNWI9khg3sE5BX1zch.json'}

exec(code, env_args)
