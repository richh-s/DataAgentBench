code = """import json, re, os

# Load the query results from storage. The variables are file paths (strings) if the results were large.
# They are available as var_call_iCyR8Anxeb4xyZcNAbUQEWKZ and var_call_I1QHap44NnHRy4fjQ4Lxs7ju

def load_var(v):
    if isinstance(v, str) and os.path.exists(v):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return v

repos_no_python = load_var(var_call_iCyR8Anxeb4xyZcNAbUQEWKZ)
contents = load_var(var_call_I1QHap44NnHRy4fjQ4Lxs7ju)

# Extract set of repo names that do NOT use Python
non_python_repos = set(r['repo_name'] for r in repos_no_python)

# Regex for copyright indicators
pattern = re.compile(r'copyright|©|\(c\)|all rights reserved', re.I)

# Find README.md files in contents for those repos
repos_with_readme = set()
repos_with_copyright = set()

for row in contents:
    repo = row.get('sample_repo_name')
    path = row.get('sample_path') or ''
    if not repo or not path:
        continue
    # consider only files whose path ends with 'readme.md' (case-insensitive)
    if path.lower().endswith('readme.md') and repo in non_python_repos:
        repos_with_readme.add(repo)
        content = row.get('content') or ''
        if pattern.search(content):
            repos_with_copyright.add(repo)

num_with_readme = len(repos_with_readme)
num_with_copyright = len(repos_with_copyright)
proportion = None
if num_with_readme > 0:
    proportion = num_with_copyright / num_with_readme

result = {
    'non_python_repos_with_readme_md': num_with_readme,
    'readme_md_with_copyright': num_with_copyright,
    'proportion': proportion
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_iCyR8Anxeb4xyZcNAbUQEWKZ': 'file_storage/call_iCyR8Anxeb4xyZcNAbUQEWKZ.json', 'var_call_I1QHap44NnHRy4fjQ4Lxs7ju': 'file_storage/call_I1QHap44NnHRy4fjQ4Lxs7ju.json'}

exec(code, env_args)
