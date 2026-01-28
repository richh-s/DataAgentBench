code = """import json
import re
import os

# Load all data
langs_file = 'file_storage/functions.query_db:10.json'
with open(langs_file, 'r') as f:
    languages_data = json.load(f)

readme_file = 'file_storage/functions.query_db:16.json'  # All README files
with open(readme_file, 'r') as f:
    readme_data = json.load(f)

readme_root_file = 'file_storage/functions.query_db:40.json'  # Root README.md only
with open(readme_root_file, 'r') as f:
    readme_root_data = json.load(f)

# Identify Python and non-Python repositories (sampling for efficiency)
python_repos = set()
all_repos = set()

# Process all language data
for item in languages_data:
    repo_name = item.get('repo_name', '')
    if repo_name:
        all_repos.add(repo_name)
        lang_desc = item.get('language_description', '').lower()
        if 'python' in lang_desc:
            python_repos.add(repo_name)

non_python_repos = all_repos - python_repos

# Check for copyright in README files (using ALL README files for better coverage)
copyright_patterns = [
    r'copyright\s+[©\\(c\\)]',
    r'©\\s*\\d{4}',
    r'\\(c\\)\\s*\\d{4}',
    r'copyright\\s+\\d{4}',
    r'all rights reserved',
    r'apache license',
    r'mit license',
    r'gpl license'
]

non_python_readmes_with_copyright = 0
total_non_python_readmes = 0

# Create a set to track processed repos to avoid double counting
processed_repos = set()

for readme in readme_root_data:  # Use root README files only for cleaner analysis
    repo_name = readme.get('sample_repo_name', '')
    if repo_name in non_python_repos and repo_name not in processed_repos:
        processed_repos.add(repo_name)
        total_non_python_readmes += 1
        content = readme.get('content', '') or ''
        content_lower = content.lower()
        has_copyright = any(re.search(pattern, content_lower) for pattern in copyright_patterns)
        if has_copyright:
            non_python_readmes_with_copyright += 1

# Also count root README.md files from the larger dataset
for readme in readme_data:
    repo_name = readme.get('sample_repo_name', '')
    path = readme.get('sample_path', '').lower()
    if (repo_name in non_python_repos and 
        repo_name not in processed_repos and 
        (path == 'readme.md' or path == 'readme')):
        processed_repos.add(repo_name)
        total_non_python_readmes += 1
        content = readme.get('content', '') or ''
        content_lower = content.lower()
        has_copyright = any(re.search(pattern, content_lower) for pattern in copyright_patterns)
        if has_copyright:
            non_python_readmes_with_copyright += 1

# Calculate final proportion
proportion = 0.0
if total_non_python_readmes > 0:
    proportion = non_python_readmes_with_copyright / total_non_python_readmes

# Calculate percentage
percentage = round(proportion * 100, 2)

result = {
    'summary': {
        'total_repositories': len(all_repos),
        'python_repositories': len(python_repos),
        'non_python_repositories': len(non_python_repos),
        'non_python_repositories_with_readme': total_non_python_readmes
    },
    'copyright_analysis': {
        'non_python_readmes_with_copyright': non_python_readmes_with_copyright,
        'proportion': proportion,
        'percentage': f"{percentage}%"
    }
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'total_repos': '3325634'}], 'var_functions.query_db:28': [{'count': '550905'}], 'var_functions.execute_python:36': {'total_repos': 3325634, 'python_repos': 550905, 'non_python_repos': 2774729, 'non_python_readmes_analyzed': 138, 'non_python_readmes_with_copyright': 15, 'proportion': 0.10869565217391304}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': [{'count': '133'}]}

exec(code, env_args)
