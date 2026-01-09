code = """import json, re
import pandas as pd

# Load non-python repos
p = var_call_nPBbGsCg0YBubAdkiHYtTCDh
if isinstance(p, str):
    with open(p, 'r', encoding='utf-8') as f:
        non_py = json.load(f)
else:
    non_py = p
non_py_set = set(r['repo_name'] for r in non_py if r.get('repo_name') is not None)

# Load readme contents
q = var_call_XwwweRUgbYGMk40tZBHZ56wQ
if isinstance(q, str):
    with open(q, 'r', encoding='utf-8') as f:
        readmes = json.load(f)
else:
    readmes = q

def has_copyright(text: str) -> bool:
    if text is None:
        return False
    t = text.lower()
    # common copyright markers
    if 'copyright' in t or 'copr.' in t or '©' in text:
        return True
    # (c) and similar
    if re.search(r'\(\s*c\s*\)', t):
        return True
    return False

# Restrict to non-python repos that have a README.md row
n_total = 0
n_with = 0
for r in readmes:
    repo = r.get('repo_name')
    if repo in non_py_set:
        n_total += 1
        if has_copyright(r.get('content')):
            n_with += 1

prop = (n_with / n_total) if n_total else None
out = {
    "non_python_repos_with_readme_md": n_total,
    "with_copyright_in_readme_md": n_with,
    "proportion": prop,
    "proportion_percent": (prop * 100.0) if prop is not None else None
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_nPBbGsCg0YBubAdkiHYtTCDh': 'file_storage/call_nPBbGsCg0YBubAdkiHYtTCDh.json', 'var_call_XwwweRUgbYGMk40tZBHZ56wQ': 'file_storage/call_XwwweRUgbYGMk40tZBHZ56wQ.json'}

exec(code, env_args)
