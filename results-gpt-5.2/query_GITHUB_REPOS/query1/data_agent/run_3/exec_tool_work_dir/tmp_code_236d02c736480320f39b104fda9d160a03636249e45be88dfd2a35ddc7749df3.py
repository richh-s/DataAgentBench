code = """import json, re, pandas as pd

# Load non-python repos
nonpy = var_call_FCoRWWFOMGBR74qVN2G9YD1y
if isinstance(nonpy, str):
    with open(nonpy, 'r', encoding='utf-8') as f:
        nonpy = json.load(f)
nonpy_set = set(r['repo_name'] for r in nonpy)

# Load readmes
readmes = var_call_TkRARNsQErNh9m4ZB9aWi68P
if isinstance(readmes, str):
    with open(readmes, 'r', encoding='utf-8') as f:
        readmes = json.load(f)

# Deduplicate by repo: pick first README.md content (any ref) deterministically
repo_to_content = {}
for r in readmes:
    rn = r.get('repo_name')
    if rn is None:
        continue
    if rn in repo_to_content:
        continue
    repo_to_content[rn] = r.get('content')

# Filter to repos that are non-python and have README.md
repos_with_readme = [rn for rn in repo_to_content.keys() if rn in nonpy_set]

def has_copyright(text):
    if text is None:
        return False
    t = str(text)
    # common patterns: "Copyright", "©", "(c)" optionally with year
    return bool(re.search(r"(?i)copyright|\u00a9|\(c\)", t))

n_total = len(repos_with_readme)
n_with = sum(1 for rn in repos_with_readme if has_copyright(repo_to_content[rn]))
prop = (n_with / n_total) if n_total else None

result = {
    "non_python_repos_with_readme_md": n_total,
    "with_copyright": n_with,
    "proportion": prop
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_FCoRWWFOMGBR74qVN2G9YD1y': 'file_storage/call_FCoRWWFOMGBR74qVN2G9YD1y.json', 'var_call_TkRARNsQErNh9m4ZB9aWi68P': 'file_storage/call_TkRARNsQErNh9m4ZB9aWi68P.json'}

exec(code, env_args)
