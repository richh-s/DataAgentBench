code = """import json, re, pandas as pd

# load non-python repos
non_py = var_call_kYJWwVWfchPHpiGkaatjMR5f
non_py_set = set(r['repo_name'].lower() for r in non_py)

# load readmes from file if needed
readmes_obj = var_call_AgsaU8G9sBtV0hPyzrDjh7F5
if isinstance(readmes_obj, str) and readmes_obj.endswith('.json'):
    with open(readmes_obj, 'r', encoding='utf-8') as f:
        readmes = json.load(f)
else:
    readmes = readmes_obj

# filter readmes to non-python repos
filtered = [r for r in readmes if (r.get('repo_name') or '').lower() in non_py_set]

def has_copyright(text: str) -> bool:
    if not text:
        return False
    t = text.lower()
    # common patterns
    if 'copyright' in t:
        return True
    if '©' in text:
        return True
    # (c) 2019, (c)2019
    if re.search(r"\(c\)\s*\d{4}", t):
        return True
    return False

n_readme = len({r['repo_name'].lower() for r in filtered})
# if multiple readmes per repo, count repo as having copyright if any readme does
repo_to_has = {}
for r in filtered:
    rn = r['repo_name'].lower()
    repo_to_has[rn] = repo_to_has.get(rn, False) or has_copyright(r.get('content') or '')

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
