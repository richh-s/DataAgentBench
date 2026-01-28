code = """import json, os, re

# Load the tool results from storage file paths
with open(var_call_KYnKWXQhPG53fWV8B1lmjNp4, 'r') as f:
    non_python_list = json.load(f)
with open(var_call_uf3GMFfGRf7ouk9ZQjXjhj0s, 'r') as f:
    contents_list = json.load(f)

# Build set of non-Python repositories
non_python_repos = set([r['repo_name'] for r in non_python_list if 'repo_name' in r])

# Filter contents to README.md files (case-insensitive basename == 'readme.md')
readme_entries = [c for c in contents_list if os.path.basename(c.get('sample_path','')).lower() == 'readme.md']

# Map repo -> list of readme contents
from collections import defaultdict
repo_readmes = defaultdict(list)
for e in readme_entries:
    repo = e.get('sample_repo_name') or e.get('sample_repo_name')
    content = e.get('content')
    repo_readmes[repo].append(content)

# Consider only repos that are in non_python_repos and have readme(s)
repos_with_readme = sorted([r for r in non_python_repos if r in repo_readmes])
repos_with_readme_count = len(repos_with_readme)

# Define copyright detection
pattern = re.compile(r'copyright|©|\(c\)', re.I)

count_with_copyright = 0
for repo in repos_with_readme:
    contents = repo_readmes.get(repo, [])
    has = False
    for c in contents:
        if c is None:
            continue
        # content may be truncated or placeholder like 'None'
        txt = str(c)
        if pattern.search(txt):
            has = True
            break
    if has:
        count_with_copyright += 1

proportion = None
if repos_with_readme_count > 0:
    proportion = count_with_copyright / repos_with_readme_count

result = {
    'total_non_python_repos': len(non_python_repos),
    'repos_with_readme_count': repos_with_readme_count,
    'repos_with_copyright_count': count_with_copyright,
    'proportion': proportion
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_KYnKWXQhPG53fWV8B1lmjNp4': 'file_storage/call_KYnKWXQhPG53fWV8B1lmjNp4.json', 'var_call_uf3GMFfGRf7ouk9ZQjXjhj0s': 'file_storage/call_uf3GMFfGRf7ouk9ZQjXjhj0s.json'}

exec(code, env_args)
