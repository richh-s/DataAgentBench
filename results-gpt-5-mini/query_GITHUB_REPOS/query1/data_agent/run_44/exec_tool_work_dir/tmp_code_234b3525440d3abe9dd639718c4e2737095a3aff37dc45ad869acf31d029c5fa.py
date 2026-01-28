code = """import json, re

# Load data from previous tool calls (paths to JSON files)
with open(var_call_QvP35I5hkHAtO7ZXUk2ISs0a, 'r') as f:
    non_python_repos_list = json.load(f)
with open(var_call_8b4rx4YYANRRGOp0VeUoGLuc, 'r') as f:
    contents_list = json.load(f)

# Build set of non-Python repository names
non_python_set = set(item['repo_name'] for item in non_python_repos_list)

# Filter contents to README.md files (case-insensitive endswith)
readme_md_entries = [c for c in contents_list if isinstance(c.get('sample_path'), str) and c['sample_path'].lower().endswith('readme.md')]

# Further filter to those belonging to non-Python repos
readme_md_non_python = [c for c in readme_md_entries if c.get('sample_repo_name') in non_python_set]

# Group by repo and check for copyright indicators
repo_to_contents = {}
for entry in readme_md_non_python:
    repo = entry.get('sample_repo_name')
    repo_to_contents.setdefault(repo, []).append(entry.get('content') or '')

copyright_regex = re.compile(r'copyright|©|all rights reserved', re.IGNORECASE)
repos_with_readme = len(repo_to_contents)
repos_with_copyright = 0
for repo, contents in repo_to_contents.items():
    if any(copyright_regex.search(text) for text in contents if isinstance(text, str)):
        repos_with_copyright += 1

# Prepare result
result = {
    'total_non_python_repos_in_languages_table': len(non_python_set),
    'non_python_repos_with_README_md_in_contents_table': repos_with_readme,
    'readme_md_with_copyright_count': repos_with_copyright,
}

# Proportion (as float between 0 and 1) and percentage
if repos_with_readme > 0:
    proportion = repos_with_copyright / repos_with_readme
    result['proportion'] = proportion
    result['proportion_percent'] = proportion * 100
else:
    result['proportion'] = None
    result['proportion_percent'] = None

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_QvP35I5hkHAtO7ZXUk2ISs0a': 'file_storage/call_QvP35I5hkHAtO7ZXUk2ISs0a.json', 'var_call_8b4rx4YYANRRGOp0VeUoGLuc': 'file_storage/call_8b4rx4YYANRRGOp0VeUoGLuc.json'}

exec(code, env_args)
