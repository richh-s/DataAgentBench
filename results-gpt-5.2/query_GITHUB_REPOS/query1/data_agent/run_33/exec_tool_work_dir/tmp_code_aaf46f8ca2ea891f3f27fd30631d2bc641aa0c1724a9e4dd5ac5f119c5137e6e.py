code = """import json, re
import pandas as pd

# load inputs (may be file paths)
langs = var_call_UrZ5XpV6QmmmeKhX5r3IQi6s
readmes = var_call_ILLCviBBmMjywWJU1Imctl7T

def load_maybe_path(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

langs = load_maybe_path(langs)
readmes = load_maybe_path(readmes)

non_python_repos = set(r['repo_name'] for r in langs if r.get('repo_name'))

# filter readmes to those repos
rows = [r for r in readmes if r.get('repo_name') in non_python_repos]

# detect copyright info
pattern = re.compile(r'(?im)(^|\b)(copyright\s*(\(c\)|©)?\s*\d{2,4}|\b©\b\s*\d{2,4}|\ball rights reserved\b)')

def has_copyright(text):
    if not isinstance(text, str):
        return False
    return bool(pattern.search(text))

# If multiple README.md per repo (different refs), treat repo as having copyright if any README does.
repo_any = {}
for r in rows:
    rn = r['repo_name']
    c = has_copyright(r.get('content'))
    repo_any[rn] = repo_any.get(rn, False) or c

n_with_readme = len(repo_any)
n_with_copyright = sum(1 for v in repo_any.values() if v)
prop = (n_with_copyright / n_with_readme) if n_with_readme else None

out = {
    "non_python_repos_with_readme_md": n_with_readme,
    "with_copyright": n_with_copyright,
    "proportion": prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_UrZ5XpV6QmmmeKhX5r3IQi6s': 'file_storage/call_UrZ5XpV6QmmmeKhX5r3IQi6s.json', 'var_call_ILLCviBBmMjywWJU1Imctl7T': 'file_storage/call_ILLCviBBmMjywWJU1Imctl7T.json'}

exec(code, env_args)
