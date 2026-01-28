code = """import json, pandas as pd, re

# load repo list (non-python)
repo_list = var_call_ORC5FBSqwzpTO2x8DJl8pX51
if isinstance(repo_list, str):
    with open(repo_list, 'r', encoding='utf-8') as f:
        repo_list = json.load(f)
non_python_repos = set(r['repo_name'] for r in repo_list)

# load readmes
readmes = var_call_c0j5FWlPOjlGsjAbcUN4Dcyz
if isinstance(readmes, str):
    with open(readmes, 'r', encoding='utf-8') as f:
        readmes = json.load(f)

# filter readmes to non-python repos
readmes_np = [r for r in readmes if r.get('repo_name') in non_python_repos]

# detect copyright info
pat = re.compile(r'(?im)(^|\b)(copyright|\(c\)|©)\b')

repos_with_readme = set()
repos_with_copyright = set()
for r in readmes_np:
    repo = r.get('repo_name')
    if not repo:
        continue
    repos_with_readme.add(repo)
    content = r.get('content') or ''
    if pat.search(content):
        repos_with_copyright.add(repo)

num_with_readme = len(repos_with_readme)
num_with_copyright = len(repos_with_copyright)
prop = (num_with_copyright / num_with_readme) if num_with_readme else None

out = {
    "non_python_repos_with_readme": num_with_readme,
    "non_python_repos_with_readme_and_copyright": num_with_copyright,
    "proportion": prop
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ORC5FBSqwzpTO2x8DJl8pX51': 'file_storage/call_ORC5FBSqwzpTO2x8DJl8pX51.json', 'var_call_c0j5FWlPOjlGsjAbcUN4Dcyz': 'file_storage/call_c0j5FWlPOjlGsjAbcUN4Dcyz.json'}

exec(code, env_args)
