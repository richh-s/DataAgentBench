code = """import json
import pandas as pd
import re
import os

# Load results from previous queries (file paths provided in variables)
with open(var_call_dZYzdGr67exvjPAkSNgObrUz, 'r') as f:
    non_py_repos = json.load(f)
with open(var_call_tjI3Rn2v2FtaTvEMc1YKRMqk, 'r') as f:
    readmes = json.load(f)

# Extract sets and dataframes
non_py_set = set(r['repo_name'] for r in non_py_repos)

# Filter to README.md files (basename == 'README.md', case-insensitive)
readme_md = [r for r in readmes if os.path.basename(r['sample_path']).lower() == 'readme.md']

# Keep only those from non-Python repos
readme_md_non_py = [r for r in readme_md if r['sample_repo_name'] in non_py_set]

# Map repo -> list of contents
from collections import defaultdict
repo_contents = defaultdict(list)
for r in readme_md_non_py:
    content = r.get('content') or ''
    repo_contents[r['sample_repo_name']].append(content)

# Heuristic to detect copyright
pattern = re.compile(r"copyright|©|\(c\)|all rights reserved", re.IGNORECASE)

repos_with_readme = set(repo_contents.keys())
repos_with_copyright = set()
for repo, contents in repo_contents.items():
    for c in contents:
        if c and pattern.search(c):
            repos_with_copyright.add(repo)
            break

total_non_python_repos = len(non_py_set)
repos_with_readme_count = len(repos_with_readme)
repos_with_copyright_count = len(repos_with_copyright)

proportion = None
if repos_with_readme_count > 0:
    proportion = repos_with_copyright_count / repos_with_readme_count

result = {
    'total_non_python_repos': total_non_python_repos,
    'non_python_repos_with_README_md': repos_with_readme_count,
    'repos_with_copyright_in_README_md': repos_with_copyright_count,
    'proportion': proportion
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_dZYzdGr67exvjPAkSNgObrUz': 'file_storage/call_dZYzdGr67exvjPAkSNgObrUz.json', 'var_call_tjI3Rn2v2FtaTvEMc1YKRMqk': 'file_storage/call_tjI3Rn2v2FtaTvEMc1YKRMqk.json'}

exec(code, env_args)
