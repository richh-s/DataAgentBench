code = """import json
import re

# Load first tool result (list of non-Python repo records)
data1 = var_call_qnxdQu7CwYKYQxPkISDRyVZd
if isinstance(data1, str):
    with open(data1, 'r', encoding='utf-8') as f:
        non_python_records = json.load(f)
else:
    non_python_records = data1

# Extract repo names into a set for fast lookup
non_python_repos = set()
for r in non_python_records:
    # each record expected to have 'repo_name'
    name = r.get('repo_name') if isinstance(r, dict) else None
    if name:
        non_python_repos.add(name)

# Load second tool result (contents with 'readme' in path)
data2 = var_call_6CxOy12JsPpVKLsN4d3A8Gwr
if isinstance(data2, str):
    with open(data2, 'r', encoding='utf-8') as f:
        contents = json.load(f)
else:
    contents = data2

# Filter to README.md files (case-insensitive) located in non-Python repos
readme_md_entries = []
for rec in contents:
    repo = rec.get('sample_repo_name')
    path = rec.get('sample_path') or ''
    if not repo or repo not in non_python_repos:
        continue
    path_l = path.lower()
    # consider files whose path ends with 'readme.md' (case-insensitive)
    if path_l.endswith('readme.md'):
        readme_md_entries.append(rec)

# Now detect copyright indicators in the content
def has_copyright(text):
    if text is None:
        return False
    # sometimes content is the string 'None'
    if isinstance(text, str) and text.strip().lower() == 'none':
        return False
    txt = str(text).lower()
    # search for typical copyright indicators
    patterns = ['copyright', '\u00a9', '(c)', 'all rights reserved']
    for p in patterns:
        if p in txt:
            return True
    return False

n_total = len(readme_md_entries)

n_copyright = 0
for rec in readme_md_entries:
    content = rec.get('content')
    if has_copyright(content):
        n_copyright += 1

proportion = None
percentage = None
if n_total > 0:
    proportion = n_copyright / n_total
    percentage = round(proportion * 100, 2)

result = {
    'total_readme_md_files_in_non_python_repos': n_total,
    'readme_md_files_with_copyright': n_copyright,
    'proportion': proportion,
    'percentage': percentage,
    'method': 'file-level proportion; README.md files counted where sample_path endswith README.md (case-insensitive); copyright detected by presence of keywords (copyright, ©, (c), all rights reserved)'
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qnxdQu7CwYKYQxPkISDRyVZd': 'file_storage/call_qnxdQu7CwYKYQxPkISDRyVZd.json', 'var_call_6CxOy12JsPpVKLsN4d3A8Gwr': 'file_storage/call_6CxOy12JsPpVKLsN4d3A8Gwr.json'}

exec(code, env_args)
