code = """import json, re
import pandas as pd

# load languages (non-python) list
langs_src = var_call_gFYzb8kbDSntl3IHIgZXwDVv
if isinstance(langs_src, str):
    with open(langs_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = langs_src

# load readmes
readmes_src = var_call_STUiDSodwZH1IxMQcXP8mRon
if isinstance(readmes_src, str):
    with open(readmes_src, 'r', encoding='utf-8') as f:
        readmes = json.load(f)
else:
    readmes = readmes_src

non_py_repos = set(r['repo_name'] for r in langs)

# copyright detection regex
# match: copyright, (c), ©, or 'all rights reserved'
pat = re.compile(r"(?is)(copyright\b|\(c\)|©|all\s+rights\s+reserved)")

total = 0
with_copyright = 0

for r in readmes:
    repo = r.get('repo_name')
    if repo in non_py_repos:
        total += 1
        content = r.get('content') or ''
        if pat.search(content):
            with_copyright += 1

prop = (with_copyright / total) if total else None

out = {
    "non_python_repos_with_readme_md": total,
    "readme_md_with_copyright": with_copyright,
    "proportion": prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_gFYzb8kbDSntl3IHIgZXwDVv': 'file_storage/call_gFYzb8kbDSntl3IHIgZXwDVv.json', 'var_call_STUiDSodwZH1IxMQcXP8mRon': 'file_storage/call_STUiDSodwZH1IxMQcXP8mRon.json'}

exec(code, env_args)
