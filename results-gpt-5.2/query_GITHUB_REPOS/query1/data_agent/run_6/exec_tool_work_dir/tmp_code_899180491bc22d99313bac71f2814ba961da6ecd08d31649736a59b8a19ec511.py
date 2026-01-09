code = """import json, re

non_py = var_call_kYJWwVWfchPHpiGkaatjMR5f
if isinstance(non_py, str) and non_py.endswith('.json'):
    with open(non_py, 'r', encoding='utf-8') as f:
        non_py = json.load(f)
non_py_set = set(r['repo_name'].lower() for r in non_py)

readmes = var_call_AgsaU8G9sBtV0hPyzrDjh7F5
if isinstance(readmes, str) and readmes.endswith('.json'):
    with open(readmes, 'r', encoding='utf-8') as f:
        readmes = json.load(f)

filtered = [r for r in readmes if (r.get('repo_name') or '').lower() in non_py_set]

def has_copyright(text: str) -> bool:
    if not text:
        return False
    t = text.lower()
    if 'copyright' in t:
        return True
    if '©' in text:
        return True
    if re.search(r"\(c\)\s*\d{4}", t):
        return True
    return False

repo_to_has = {}
for r in filtered:
    rn = r['repo_name'].lower()
    repo_to_has[rn] = repo_to_has.get(rn, False) or has_copyright(r.get('content') or '')

n_readme = len(repo_to_has)
n_with = sum(1 for v in repo_to_has.values() if v)
prop = (n_with / n_readme) if n_readme else None

out = {
    "non_python_repos_with_readme_md": n_readme,
    "repos_with_copyright_in_readme_md": n_with,
    "proportion": prop
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_kYJWwVWfchPHpiGkaatjMR5f': 'file_storage/call_kYJWwVWfchPHpiGkaatjMR5f.json', 'var_call_AgsaU8G9sBtV0hPyzrDjh7F5': 'file_storage/call_AgsaU8G9sBtV0hPyzrDjh7F5.json'}

exec(code, env_args)
