code = """import json, pandas as pd, re

# Load non-python repos
non_py_path = var_call_OXpkTiM8pNFo8i8lNPOrizft
with open(non_py_path, 'r', encoding='utf-8') as f:
    non_py = json.load(f)
non_py_set = set(r['repo_name'] for r in non_py)

# Load readmes
readme_path = var_call_CP72vEdKQ1wdi6KPCbj5ht0M
with open(readme_path, 'r', encoding='utf-8') as f:
    readmes = json.load(f)

# Filter readmes to non-python repos
filtered = [r for r in readmes if r.get('repo_name') in non_py_set]

def has_copyright(text: str) -> bool:
    if text is None:
        return False
    t = text.lower()
    # common markers
    if 'copyright' in t or '(c)' in t or '©' in t:
        return True
    # common license footer like "Copyright 2018" even without word? usually includes it.
    return False

n_total = len(filtered)
n_with = sum(1 for r in filtered if has_copyright(r.get('content')))
prop = (n_with / n_total) if n_total else None

out = {
    'non_python_repos_with_readme_md': n_total,
    'readme_md_with_copyright': n_with,
    'proportion': prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_OXpkTiM8pNFo8i8lNPOrizft': 'file_storage/call_OXpkTiM8pNFo8i8lNPOrizft.json', 'var_call_CP72vEdKQ1wdi6KPCbj5ht0M': 'file_storage/call_CP72vEdKQ1wdi6KPCbj5ht0M.json'}

exec(code, env_args)
