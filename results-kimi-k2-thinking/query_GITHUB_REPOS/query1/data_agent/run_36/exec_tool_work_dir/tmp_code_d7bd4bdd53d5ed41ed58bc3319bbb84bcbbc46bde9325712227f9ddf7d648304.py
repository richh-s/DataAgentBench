code = """import json
import re

# Load languages data
langs_file = 'file_storage/functions.query_db:10.json'
with open(langs_file, 'r') as f:
    languages_data = json.load(f)

# Load README data
readme_file = 'file_storage/functions.query_db:16.json'
with open(readme_file, 'r') as f:
    readme_data = json.load(f)

# Identify Python and non-Python repositories
python_repos = set()
all_repos = set()

for item in languages_data:
    repo_name = item.get('repo_name', '')
    if repo_name:
        all_repos.add(repo_name)
        lang_desc = item.get('language_description', '').lower()
        if 'python' in lang_desc:
            python_repos.add(repo_name)

non_python_repos = all_repos - python_repos

# Check copyright in README files for non-Python repos
copyright_patterns = [
    r'copyright\s+[©\\(c\\)]',
    r'©\\s*\\d{4}',
    r'\\(c\\)\\s*\\d{4}',
    r'copyright\\s+\\d{4}',
    r'all rights reserved'
]

copyright_count = 0
total_non_python_readmes = 0

for readme in readme_data:
    repo_name = readme.get('sample_repo_name', '')
    if repo_name in non_python_repos:
        total_non_python_readmes += 1
        content = readme.get('content', '') or ''
        content_lower = content.lower()
        has_copyright = any(re.search(pattern, content_lower) for pattern in copyright_patterns)
        if has_copyright:
            copyright_count += 1

# Calculate proportion
proportion = 0.0
if total_non_python_readmes > 0:
    proportion = copyright_count / total_non_python_readmes

result = {
    'total_repos': len(all_repos),
    'python_repos': len(python_repos),
    'non_python_repos': len(non_python_repos),
    'non_python_readmes_analyzed': total_non_python_readmes,
    'non_python_readmes_with_copyright': copyright_count,
    'proportion': proportion
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'total_repos': '3325634'}], 'var_functions.query_db:28': [{'count': '550905'}]}

exec(code, env_args)
