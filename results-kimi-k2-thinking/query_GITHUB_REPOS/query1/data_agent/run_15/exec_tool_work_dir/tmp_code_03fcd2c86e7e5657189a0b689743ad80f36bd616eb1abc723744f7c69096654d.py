code = """import json
import re

# Read the languages data
with open('var_functions.query_db:0.json', 'r') as f:
    languages_data = json.load(f)

# Read the README.md contents data
with open('var_functions.query_db:2.json', 'r') as f:
    readme_data = json.load(f)

# Filter repositories that do NOT use Python
non_python_repos = []
for repo in languages_data:
    repo_name = repo['repo_name']
    language_desc = repo['language_description'].lower()
    
    # Check if Python is mentioned in the language description
    if 'python' not in language_desc:
        non_python_repos.append(repo_name)

print(f"Total repositories: {len(languages_data)}")
print(f"Non-Python repositories: {len(non_python_repos)}")

# Create a set for faster lookup
non_python_set = set(non_python_repos)

# Filter README.md files for non-Python repositories
non_python_readmes = []
for readme in readme_data:
    repo_name = readme['sample_repo_name']
    if repo_name in non_python_set:
        non_python_readmes.append({
            'repo_name': repo_name,
            'path': readme['sample_path'],
            'content': readme['content'] or ''  # Handle None content
        })

print(f"README.md files from non-Python repos: {len(non_python_readmes)}")

# Check for copyright information
copyright_patterns = [
    r'copyright', r'©', r'\(c\)', r'\[c\]', r'all rights reserved',
    r'Apache License', r'MIT License', r'GPL', r'GNU General Public License'
]

copyright_count = 0
total_readmes = len(non_python_readmes)

for readme in non_python_readmes:
    content = readme['content'].lower()
    has_copyright = any(re.search(pattern, content, re.IGNORECASE) for pattern in copyright_patterns)
    if has_copyright:
        copyright_count += 1

# Calculate proportion
if total_readmes > 0:
    proportion = copyright_count / total_readmes
    result = {
        'total_non_python_repos': len(non_python_repos),
        'total_non_python_readmes': total_readmes,
        'readmes_with_copyright': copyright_count,
        'proportion': proportion,
        'percentage': proportion * 100
    }
else:
    result = {
        'total_non_python_repos': len(non_python_repos),
        'total_non_python_readmes': 0,
        'readmes_with_copyright': 0,
        'proportion': 0,
        'percentage': 0
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
