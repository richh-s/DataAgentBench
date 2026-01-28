code = """import json
import re

# Access the language data from the first query using locals()
lang_var = locals()['var_functions.query_db:0']
readme_var = locals()['var_functions.query_db:2']

# Load the data if it's file paths, otherwise use directly
if isinstance(lang_var, str) and '.json' in lang_var:
    with open(lang_var, 'r') as f:
        languages_data = json.load(f)
else:
    languages_data = lang_var

if isinstance(readme_var, str) and '.json' in readme_var:
    with open(readme_var, 'r') as f:
        readme_data = json.load(f)
else:
    readme_data = readme_var

# Debug info
print(f"Languages data length: {len(languages_data)}")
print(f"README data length: {len(readme_data)}")

# Filter repositories that do NOT use Python
non_python_repos = []
for repo in languages_data:
    repo_name = repo.get('repo_name', '')
    language_desc = repo.get('language_description', '').lower()
    
    # Check if Python is mentioned
    if 'python' not in language_desc:
        non_python_repos.append(repo_name)

print(f"Non-Python repos: {len(non_python_repos)}")

# Create a set for faster lookup
non_python_set = set(non_python_repos)

# Filter README.md files for non-Python repositories
non_python_readmes = []
for readme in readme_data:
    repo_name = readme.get('sample_repo_name', '')
    path = readme.get('sample_path', '')
    
    # Only include actual README.md files (not in subdirectories with similar names)
    if repo_name in non_python_set and path == 'README.md':
        content = readme.get('content', '') or ''
        non_python_readmes.append({
            'repo_name': repo_name,
            'content': content
        })

print(f"README.md files from non-Python repos: {len(non_python_readmes)}")

copyright_patterns = ['copyright', '©', '(c)', 'all rights reserved', 
                      'apache license', 'mit license', 'gpl', 'bsd license',
                      'mozilla public license']

# Check for copyright information
copyright_count = 0
total_readmes = len(non_python_readmes)

for readme in non_python_readmes:
    content = readme['content'].lower()
    has_copyright = any(pattern in content for pattern in copyright_patterns)
    if has_copyright:
        copyright_count += 1

print(f"READMEs with copyright: {copyright_count}")

# Calculate proportion
proportion = copyright_count / total_readmes if total_readmes > 0 else 0

result = {
    'total_non_python_readmes': total_readmes,
    'readmes_with_copyright': copyright_count,
    'proportion': round(proportion, 4),
    'percentage': round(proportion * 100, 2)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
