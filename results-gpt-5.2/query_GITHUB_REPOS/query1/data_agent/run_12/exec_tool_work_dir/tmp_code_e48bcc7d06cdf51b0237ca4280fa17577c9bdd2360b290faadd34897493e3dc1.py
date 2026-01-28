code = """import json, re

nonpy = var_call_FNNaZsoDC890Os26cTGEvonr
readmes = var_call_tHGgIROYuhoDLro8saMn0eZI

# if stored as file paths, load
if isinstance(nonpy, str) and nonpy.endswith('.json'):
    with open(nonpy, 'r', encoding='utf-8') as f:
        nonpy = json.load(f)
if isinstance(readmes, str) and readmes.endswith('.json'):
    with open(readmes, 'r', encoding='utf-8') as f:
        readmes = json.load(f)

nonpy_set = set(r['repo_name'] for r in nonpy)
filtered = [r for r in readmes if r.get('repo_name') in nonpy_set]

pat = re.compile(r"\bcopyright\b|©", re.IGNORECASE)

total = len(filtered)
with_c = 0
for r in filtered:
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
