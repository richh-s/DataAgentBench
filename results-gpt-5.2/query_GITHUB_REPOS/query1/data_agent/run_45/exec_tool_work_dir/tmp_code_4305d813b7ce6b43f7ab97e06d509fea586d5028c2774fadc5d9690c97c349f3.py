code = """import json, pandas as pd, re

# Load repo lists
import os

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path

non_python = load_records(var_call_xsX470ZYT503Y621XudYjPiT)
readmes = load_records(var_call_A0tSZNKNsy0diq65ixhgotKv)

non_python_set = {r['repo_name'] for r in non_python}

# Filter to non-python repos that have a README.md content record
readmes_np = [r for r in readmes if r.get('repo_name') in non_python_set and isinstance(r.get('content'), str)]

def has_copyright(text: str) -> bool:
    t = text.lower()
    # common patterns: copyright, (c), ©, all rights reserved
    return (
        'copyright' in t
        or 'all rights reserved' in t
        or '(c)' in t
        or '©' in text
    )

n_total = len(readmes_np)
n_with = sum(1 for r in readmes_np if has_copyright(r['content']))

prop = (n_with / n_total) if n_total else None

out = {
    'non_python_repos_with_readme_md': n_total,
    'readme_md_with_copyright': n_with,
    'proportion': prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_xsX470ZYT503Y621XudYjPiT': 'file_storage/call_xsX470ZYT503Y621XudYjPiT.json', 'var_call_A0tSZNKNsy0diq65ixhgotKv': 'file_storage/call_A0tSZNKNsy0diq65ixhgotKv.json'}

exec(code, env_args)
