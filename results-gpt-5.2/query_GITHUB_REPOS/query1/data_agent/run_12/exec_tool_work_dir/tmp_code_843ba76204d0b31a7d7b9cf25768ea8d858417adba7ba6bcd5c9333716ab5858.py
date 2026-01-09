code = """import json, pandas as pd, re

# Load non-python repos
nonpy = var_call_FNNaZsoDC890Os26cTGEvonr
nonpy_set = set(r['repo_name'] for r in nonpy)

# Load readmes
readmes = var_call_tHGgIROYuhoDLro8saMn0eZI

# Filter to repos that are non-python and have a README.md entry
filtered = []
for r in readmes:
    rn = r.get('repo_name')
    if rn in nonpy_set:
        filtered.append(r)

# Define copyright detection
pat = re.compile(r"\bcopyright\b|\b©\b", re.IGNORECASE)

total = 0
with_c = 0
for r in filtered:
    total += 1
    content = r.get('content') or ''
    if pat.search(content):
        with_c += 1

prop = (with_c / total) if total else None
out = {
    "non_python_repos_with_readme_md": total,
    "readmes_with_copyright": with_c,
    "proportion": prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FNNaZsoDC890Os26cTGEvonr': 'file_storage/call_FNNaZsoDC890Os26cTGEvonr.json', 'var_call_tHGgIROYuhoDLro8saMn0eZI': 'file_storage/call_tHGgIROYuhoDLro8saMn0eZI.json'}

exec(code, env_args)
