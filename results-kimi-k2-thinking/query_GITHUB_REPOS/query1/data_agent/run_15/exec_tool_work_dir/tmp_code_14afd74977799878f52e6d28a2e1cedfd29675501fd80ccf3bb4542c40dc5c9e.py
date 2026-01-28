code = """import json
import re

# Access the language data from the first query
languages_data = locals()['var_functions.query_db:0']

# Access the README data from the second query  
readme_data = locals()['var_functions.query_db:2']

# First, analyze language data to identify non-Python repositories
non_python_repos = []
for repo in languages_data:
    repo_name = repo['repo_name']
    language_desc = repo['language_description'].lower()
    
    # Check if Python is mentioned in the language description
    # Look for 'python' as a complete word, not part of other words
    if not re.search(r'\bpython\b', language_desc):
        non_python_repos.append(repo_name)

# Create a set for faster lookup
non_python_set = set(non_python_repos)

# Filter README.md files for non-Python repositories
# Also filter for actual README.md files (not just files with README.md in the path)
non_python_readmes = []
for readme in readme_data:
    repo_name = readme['sample_repo_name']
    path = readme['sample_path']
    
    # Check if the file is actually named README.md (not just in a directory with that name)
    if repo_name in non_python_set and path.endswith('README.md'):
        content = readme['content'] if readme['content'] else ''
        non_python_readmes.append({
            'repo_name': repo_name,
            'path': path,
            'content': content
        })

# Define patterns for copyright detection
copyright_patterns = [
    r'copyright', r'©', r'\(c\)', r'\[c\]', r'all rights reserved',
    r'apache license', r'mit license', r'gpl', r'gnu general public license',
    r'bsd license', r'mozilla public license', r'artistic license',
    r'eclipse public license'
]

# Check for copyright information in README contents
copyright_count = 0
total_readmes = len(non_python_readmes)

for readme in non_python_readmes:
    content = readme['content'].lower()
    has_copyright = any(re.search(pattern, content) for pattern in copyright_patterns)
    if has_copyright:
        copyright_count += 1

# Calculate proportion and percentage
proportion = copyright_count / total_readmes if total_readmes > 0 else 0
percentage = proportion * 100

result = {
    'total_non_python_repos': len(non_python_repos),
    'total_non_python_readmes': total_readmes,
    'readmes_with_copyright': copyright_count,
    'proportion': round(proportion, 4),
    'percentage': round(percentage, 2)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
