code = """import json, os, re

# Load data from storage-provided file paths
with open(var_call_WUQrtwEY6SVDpDQy555VX5lF, 'r', encoding='utf-8') as f:
    non_python_list = json.load(f)
with open(var_call_NT2l1Yh38pX6176jJFgV6bJn, 'r', encoding='utf-8') as f:
    contents_list = json.load(f)

# Build set of non-Python repo names
non_python_repos = {r['repo_name'] for r in non_python_list}

# Helper to detect README.md by basename
def is_readme_md(path):
    try:
        return os.path.basename(path).lower() == 'readme.md'
    except Exception:
        return False

# Collect README.md entries for non-Python repos
readme_by_repo = {}
for rec in contents_list:
    repo = rec.get('sample_repo_name')
    path = rec.get('sample_path', '')
    if repo in non_python_repos and is_readme_md(path):
        readme_by_repo.setdefault(repo, []).append(rec.get('content') or '')

# Detection regex for copyright
pattern = re.compile(r'copyright|©|\(c\)', re.I)

repos_with_readme = len(readme_by_repo)
repos_with_readme_and_copyright = 0
repos_with_readme_and_copyright_list = []
for repo, contents in readme_by_repo.items():
    found = any(bool(pattern.search(c)) for c in contents)
    if found:
        repos_with_readme_and_copyright += 1
        repos_with_readme_and_copyright_list.append(repo)

proportion = None
if repos_with_readme > 0:
    proportion = repos_with_readme_and_copyright / repos_with_readme

result = {
    'total_non_python_repos_in_languages_table': len(non_python_repos),
    'repos_with_readme_md_in_contents': repos_with_readme,
    'repos_with_readme_md_including_copyright': repos_with_readme_and_copyright,
    'proportion': proportion
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WUQrtwEY6SVDpDQy555VX5lF': 'file_storage/call_WUQrtwEY6SVDpDQy555VX5lF.json', 'var_call_NT2l1Yh38pX6176jJFgV6bJn': 'file_storage/call_NT2l1Yh38pX6176jJFgV6bJn.json'}

exec(code, env_args)
