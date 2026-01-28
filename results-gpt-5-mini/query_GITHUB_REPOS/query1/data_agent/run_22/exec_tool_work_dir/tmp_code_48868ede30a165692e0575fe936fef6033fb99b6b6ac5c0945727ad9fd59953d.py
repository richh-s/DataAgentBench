code = """import json, re

# Load the large query results from storage files
with open(var_call_tPWlll1c5Jui03DugUtKM0pd, 'r', encoding='utf-8') as f:
    non_python_langs = json.load(f)
with open(var_call_IratfooCUEHbiZd0rDrm8s98, 'r', encoding='utf-8') as f:
    contents = json.load(f)

# Build set of repo names that do NOT use Python (from the first query)
non_python_repos = set()
for r in non_python_langs:
    # safe access
    repo = r.get('repo_name')
    if repo:
        non_python_repos.add(repo)

# Filter contents for README.md files belonging to these repos
readme_entries = []
for c in contents:
    repo = c.get('sample_repo_name')
    path = c.get('sample_path')
    if not repo or not path:
        continue
    if repo in non_python_repos and path.lower().endswith('readme.md'):
        readme_entries.append(c)

# Define copyright detection pattern
pattern = re.compile(r'copyright|\u00a9|\(c\)|all rights reserved', re.I)

match_count = 0
for e in readme_entries:
    content = e.get('content')
    if not content:
        continue
    # content may be non-string; ensure string
    if not isinstance(content, str):
        try:
            content = str(content)
        except Exception:
            continue
    if pattern.search(content):
        match_count += 1

total = len(readme_entries)
proportion = None
if total > 0:
    proportion = match_count / total

result = {
    'total_readme_md_files_in_non_python_repos': total,
    'readme_md_files_with_copyright_info': match_count,
    'proportion': proportion
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_tPWlll1c5Jui03DugUtKM0pd': 'file_storage/call_tPWlll1c5Jui03DugUtKM0pd.json', 'var_call_IratfooCUEHbiZd0rDrm8s98': 'file_storage/call_IratfooCUEHbiZd0rDrm8s98.json'}

exec(code, env_args)
