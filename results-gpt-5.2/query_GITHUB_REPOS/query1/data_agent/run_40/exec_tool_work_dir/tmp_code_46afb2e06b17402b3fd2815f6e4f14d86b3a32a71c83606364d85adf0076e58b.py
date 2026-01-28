code = """import json, pandas as pd

# load non-python repos
non_py = var_call_rRs3IFLlIIMYXgyy2kyYmgN2
if isinstance(non_py, str):
    with open(non_py, 'r') as f:
        non_py = json.load(f)
non_py_set = set(r['repo_name'] for r in non_py if r.get('repo_name') is not None)

def has_copyright(text: str) -> bool:
    if text is None:
        return False
    t = text.lower()
    # common copyright markers
    if 'copyright' in t:
        return True
    if '(c)' in t or '©' in t:
        return True
    return False

readmes = var_call_mBtp2MHhGAMkXjwFBV4IdmyU
# compute
repos_with_readme = set(r['repo_name'] for r in readmes if r.get('repo_name') is not None)
non_py_with_readme = non_py_set.intersection(repos_with_readme)

# count repos whose README includes copyright marker
repo_to_flag = {}
for r in readmes:
    repo = r.get('repo_name')
    if repo not in non_py_with_readme:
        continue
    repo_to_flag.setdefault(repo, False)
    if has_copyright(r.get('content')):
        repo_to_flag[repo] = True

numerator = sum(1 for v in repo_to_flag.values() if v)
denominator = len(non_py_with_readme)
proportion = (numerator / denominator) if denominator else None

out = {
    'non_python_repos_with_readme_md': int(denominator),
    'with_copyright_in_readme_md': int(numerator),
    'proportion': proportion
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_rRs3IFLlIIMYXgyy2kyYmgN2': 'file_storage/call_rRs3IFLlIIMYXgyy2kyYmgN2.json', 'var_call_mBtp2MHhGAMkXjwFBV4IdmyU': []}

exec(code, env_args)
