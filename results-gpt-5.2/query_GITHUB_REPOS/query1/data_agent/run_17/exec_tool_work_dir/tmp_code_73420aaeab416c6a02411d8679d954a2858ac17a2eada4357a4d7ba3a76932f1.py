code = """import json, re
import pandas as pd

# Load languages (non-python) result
langs = var_call_0jcWJAs66eYPQlD0894haqXH
if isinstance(langs, str):
    with open(langs, 'r', encoding='utf-8') as f:
        langs = json.load(f)

readmes = var_call_wgm1lsXzMAZhiiExxnpMUBwS
if isinstance(readmes, str):
    with open(readmes, 'r', encoding='utf-8') as f:
        readmes = json.load(f)

non_python_repos = {r['repo_name'] for r in langs if r.get('repo_name')}

# Among those repos, check README.md content includes copyright info
# Heuristic: presence of 'copyright' or '(c)' or '©'
pat = re.compile(r"copyright|\(c\)|©", re.IGNORECASE)

repos_with_readme = set()
repos_with_copyright = set()

for r in readmes:
    repo = r.get('repo_name')
    if repo in non_python_repos:
        repos_with_readme.add(repo)
        content = r.get('content') or ''
        if pat.search(content):
            repos_with_copyright.add(repo)

num = len(repos_with_copyright)
den = len(repos_with_readme)
prop = (num / den) if den else None

out = {
    "non_python_repos_with_readme": den,
    "non_python_repos_with_readme_and_copyright": num,
    "proportion": prop
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_0jcWJAs66eYPQlD0894haqXH': 'file_storage/call_0jcWJAs66eYPQlD0894haqXH.json', 'var_call_wgm1lsXzMAZhiiExxnpMUBwS': 'file_storage/call_wgm1lsXzMAZhiiExxnpMUBwS.json'}

exec(code, env_args)
