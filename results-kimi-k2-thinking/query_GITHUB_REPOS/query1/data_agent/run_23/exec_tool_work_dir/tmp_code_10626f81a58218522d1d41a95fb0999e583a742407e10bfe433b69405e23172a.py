code = """import json
import re

# Load non-Python repos
languages_file = locals()['var_functions.query_db:2']
with open(languages_file, 'r') as f:
    languages_data = json.load(f)

# Create set of non-Python repos for fast lookup
non_python_repos = set()
for item in languages_data:
    repo_name = item['repo_name']
    lang_desc = item.get('language_description', '') or ''
    if 'python' not in lang_desc.lower():
        non_python_repos.add(repo_name)

print(f"Loaded {len(non_python_repos)} non-Python repos")

# Load README data
readme_file = locals()['var_functions.query_db:22']
with open(readme_file, 'r') as f:
    readme_data = json.load(f)

print(f"Total README files: {len(readme_data)}")

# Filter READMEs to only non-Python repos
non_python_readmes = []
for item in readme_data:
    repo_name = item['sample_repo_name']
    if repo_name in non_python_repos:
        non_python_readmes.append({
            'repo': repo_name,
            'path': item['sample_path'],
            'content': item['content'] or ''
        })

print(f"READMEs from non-Python repos: {len(non_python_readmes)}")

# Check for copyright information
copyright_indicators = [
    r'copyright\s*[©]?(?:\s*\d{4})?(?:\s*[-–]\s*\d{4})?',
    r'\b©\b',
    r'all rights reserved',
    r'rights reserved'
]

# Compile regex patterns
copyright_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in copyright_indicators]

def has_copyright(content):
    if not content:
        return False
    for pattern in copyright_patterns:
        if pattern.search(content):
            return True
    return False

# Analyze each README
total_non_python_readmes = len(non_python_readmes)
copyright_count = 0
not_copyright_count = 0

for readme in non_python_readmes:
    if has_copyright(readme['content']):
        copyright_count += 1
    else:
        not_copyright_count += 1

print(f"Non-Python READMEs with copyright: {copyright_count}")
print(f"Non-Python READMEs without copyright: {not_copyright_count}")

# Calculate proportion
if total_non_python_readmes > 0:
    proportion = copyright_count / total_non_python_readmes
    print(f"Proportion: {proportion:.4f} ({copyright_count}/{total_non_python_readmes})")

result = {
    "total_non_python_repos": len(non_python_repos),
    "total_non_python_readmes": total_non_python_readmes,
    "copyright_count": copyright_count,
    "no_copyright_count": not_copyright_count,
    "proportion": proportion if total_non_python_readmes > 0 else 0
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'data_type': "<class 'str'>"}, 'var_functions.execute_python:14': {'total_repos': 3325634, 'non_python_count': 2774729, 'example_repos': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:23': {'total_repos': 3325634, 'python_repos': 550905, 'non_python_repos': 2774729}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
