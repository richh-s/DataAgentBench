code = """import json, re
import pandas as pd

# Load non-python repos
non_python = var_call_Hgic7iwBX1MfCSvobe1hkAPc
if isinstance(non_python, str):
    with open(non_python, 'r', encoding='utf-8') as f:
        non_python = json.load(f)
non_python_set = set(r['repo_name'] for r in non_python)

# Load readmes
readmes = var_call_Att0Sq2cZRoRK2B96OxE3djp
if isinstance(readmes, str):
    with open(readmes, 'r', encoding='utf-8') as f:
        readmes = json.load(f)

# Filter to repos not using Python and having README.md content
rows = []
for r in readmes:
    rn = r.get('repo_name')
    if rn in non_python_set:
        rows.append(r)

# Deduplicate by repo_name; keep first
seen = set()
unique = []
for r in rows:
    rn = r['repo_name']
    if rn not in seen:
        seen.add(rn)
        unique.append(r)

# Heuristic for copyright info
pat = re.compile(r'(?:\(c\)|\bcopyright\b|©)', re.IGNORECASE)

total = len(unique)
with_copy = 0
for r in unique:
    content = r.get('content') or ''
    if pat.search(content):
        with_copy += 1

prop = (with_copy / total) if total else None

out = {
    'non_python_repos_with_readme_md': total,
    'readme_md_with_copyright': with_copy,
    'proportion': prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Hgic7iwBX1MfCSvobe1hkAPc': 'file_storage/call_Hgic7iwBX1MfCSvobe1hkAPc.json', 'var_call_Att0Sq2cZRoRK2B96OxE3djp': 'file_storage/call_Att0Sq2cZRoRK2B96OxE3djp.json'}

exec(code, env_args)
