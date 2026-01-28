code = """import json
import re

# Load stored query results from files
with open(var_call_JghfiSDl66PeUPLvl431v7hV, 'r') as f:
    non_python_repos = json.load(f)
with open(var_call_KzN6jJrTv00wx3A7aeVIreOU, 'r') as f:
    contents = json.load(f)

# non_python_repos is a list of dicts with 'repo_name'
repo_set = set(r['repo_name'] for r in non_python_repos)

# Filter contents for README.md files belonging to these repos
readme_records = [c for c in contents if c.get('sample_repo_name') in repo_set and 'readme.md' in c.get('sample_path','').lower()]

total_readmes = len(readme_records)

# Define patterns indicating copyright
patterns = [r'copyright', r'\u00a9', r'©', r'all rights reserved', r"\(c\)"]
regex = re.compile('|'.join(patterns), re.IGNORECASE)

matches = 0
for r in readme_records:
    content = r.get('content') or ''
    if regex.search(content):
        matches += 1

proportion = (matches / total_readmes) if total_readmes > 0 else None

result = {
    'total_readme_files_in_non_python_repos': total_readmes,
    'readme_files_with_copyright_info': matches,
    'proportion': proportion
}

import json
print("----BEGIN PRINT FORMAT----")
print("print(\"__RESULT__:\")")
print("print('" + json.dumps(result).replace("'", "\\'") + "')")
print("----END PRINT FORMAT----")"""

env_args = {'var_call_hKbiWS7TDxY6fP5WkoWTmv2N': ['languages', 'repos', 'licenses'], 'var_call_WntdmEySBpV0Vyj8FXa2Liq9': ['commits', 'contents', 'files'], 'var_call_JghfiSDl66PeUPLvl431v7hV': 'file_storage/call_JghfiSDl66PeUPLvl431v7hV.json', 'var_call_KzN6jJrTv00wx3A7aeVIreOU': 'file_storage/call_KzN6jJrTv00wx3A7aeVIreOU.json'}

exec(code, env_args)
