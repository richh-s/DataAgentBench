code = """import json
import os
import re

# Load data from previous query results (file paths)
with open(var_call_pcevBPwbtuTCMlX6lr9Aw63o, 'r', encoding='utf-8') as f:
    repos_data = json.load(f)
with open(var_call_6du2hLJKyNH8NyBTNkMLb3wb, 'r', encoding='utf-8') as f:
    contents_data = json.load(f)

# Build set of non-Python repo names
non_py_repos = set(r['repo_name'] for r in repos_data)

# Filter contents for README.md files in non-Python repos
readme_md_entries = []
for e in contents_data:
    repo = e.get('sample_repo_name')
    path = e.get('sample_path') or ''
    if repo not in non_py_repos:
        continue
    # get filename
    fname = os.path.basename(path).lower()
    if fname == 'readme.md':
        readme_md_entries.append(e)

total = len(readme_md_entries)

# Define copyright detection
pattern = re.compile(r'copyright|©|all rights reserved', re.IGNORECASE)
count = 0
for e in readme_md_entries:
    c = e.get('content')
    if not c or not isinstance(c, str):
        continue
    if pattern.search(c):
        count += 1

proportion = None
if total > 0:
    proportion = count / total

result = {
    'total_readme_md_files_in_non_python_repos': total,
    'readme_md_with_copyright': count,
    'proportion': round(proportion, 4) if proportion is not None else None
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pcevBPwbtuTCMlX6lr9Aw63o': 'file_storage/call_pcevBPwbtuTCMlX6lr9Aw63o.json', 'var_call_6du2hLJKyNH8NyBTNkMLb3wb': 'file_storage/call_6du2hLJKyNH8NyBTNkMLb3wb.json'}

exec(code, env_args)
