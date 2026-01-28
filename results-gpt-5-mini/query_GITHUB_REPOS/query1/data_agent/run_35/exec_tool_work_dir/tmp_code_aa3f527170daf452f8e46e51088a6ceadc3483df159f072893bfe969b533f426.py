code = """import json
from pathlib import Path

# Load previous tool results
# var_call_KUW1fMdu0W7EEV0ECjkAuJKQ and var_call_SEjWeBaavYj8ud8m1J9FIWZ9 are provided by storage

p1 = Path(var_call_KUW1fMdu0W7EEV0ECjkAuJKQ)
with p1.open('r', encoding='utf-8') as f:
    non_python_repos = json.load(f)  # list of dicts with 'repo_name'

p2 = Path(var_call_SEjWeBaavYj8ud8m1J9FIWZ9)
with p2.open('r', encoding='utf-8') as f:
    contents = json.load(f)  # list of dicts with sample_repo_name, sample_path, content

# Build set of non-python repo names
non_py_set = set(r['repo_name'] for r in non_python_repos)

# Filter contents to README.md files only and belonging to non-python repos
readme_files = []
for row in contents:
    repo = row.get('sample_repo_name')
    path = row.get('sample_path') or ''
    content = row.get('content')
    if not repo or repo not in non_py_set:
        continue
    if 'readme' in path.lower() and path.lower().endswith('.md'):
        readme_files.append({'repo': repo, 'path': path, 'content': content})

# Detection patterns for copyright
import re
patterns = [re.compile(r'copyright', re.I), re.compile(r'©'), re.compile(r'all rights reserved', re.I), re.compile(r'版权所有')]

def has_copyright(text):
    if text is None:
        return False
    # Some content fields contain the string "None" to indicate missing content
    if isinstance(text, str) and text.strip().lower() == 'none':
        return False
    if not isinstance(text, str):
        return False
    for p in patterns:
        if p.search(text):
            return True
    return False

# Compute counts
total = len(readme_files)
with_copyright = sum(1 for f in readme_files if has_copyright(f['content']))

proportion = None
if total > 0:
    proportion = with_copyright / total

result = {
    'total_readme_md_files_in_non_python_repos': total,
    'readme_md_files_with_copyright': with_copyright,
    'proportion': proportion
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_KUW1fMdu0W7EEV0ECjkAuJKQ': 'file_storage/call_KUW1fMdu0W7EEV0ECjkAuJKQ.json', 'var_call_SEjWeBaavYj8ud8m1J9FIWZ9': 'file_storage/call_SEjWeBaavYj8ud8m1J9FIWZ9.json'}

exec(code, env_args)
