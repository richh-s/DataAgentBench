code = """import json
import re
import os

# Read non-Python repositories
non_python_file = '/tmp/tmpqntf1a1p.json'
with open(non_python_file, 'r') as f:
    non_python_data = json.load(f)

non_python_repos = {repo['repo_name'] for repo in non_python_data}
print('Total non-Python repositories:', len(non_python_repos))

# Read README files
readme_file = '/tmp/tmp4y6j7o3k.json'
with open(readme_file, 'r') as f:
    readme_data = json.load(f)

print('Total README files found:', len(readme_data))

# Filter to only non-Python repositories' README files
filtered_readmes = []
for readme in readme_data:
    repo_name = readme['sample_repo_name']
    # Check if this is a non-Python repo
    if repo_name in non_python_repos:
        # Also check if it's a root-level README.md (not nested)
        path = readme['sample_path']
        if path == 'README.md' or path.endswith('/README.md'):
            # If nesting, make sure it's not too deep (e.g., not in subdirs)
            # A simple check: count slashes
            slash_count = path.count('/')
            if slash_count <= 1:  # Root or one level deep max
                filtered_readmes.append(readme)

print('README.md files in non-Python repositories:', len(filtered_readmes))

# Check for copyright information in content
copyright_patterns = [
    r'\bcopyright\b',
    r'©',
    r'\(c\)\s+\d{4}',
    r'copyrights',
    r'all rights reserved',
    r'Rights Reserved'
]

def has_copyright(content):
    if not content:
        return False
    content_lower = content.lower()
    for pattern in copyright_patterns:
        if re.search(pattern, content_lower, re.IGNORECASE):
            return True
    return False

# Analyze each README
total_count = 0
copyright_count = 0
examples = []

for readme in filtered_readmes:
    total_count += 1
    content = readme.get('content', '')
    
    if has_copyright(content):
        copyright_count += 1
        if len(examples) < 3:
            examples.append({
                'repo': readme['sample_repo_name'],
                'path': readme['sample_path'],
                'has_copyright': True
            })
    else:
        if len(examples) < 3:
            examples.append({
                'repo': readme['sample_repo_name'],
                'path': readme['sample_path'],
                'has_copyright': False
            })

proportion = copyright_count / total_count if total_count > 0 else 0

result = {
    'total_non_python_repos': len(non_python_repos),
    'readme_files_analyzed': total_count,
    'readme_with_copyright': copyright_count,
    'readme_without_copyright': total_count - copyright_count,
    'proportion': proportion,
    'percentage': proportion * 100,
    'examples': examples[:5]
}

print('\n=== Analysis Results ===')
print('Total non-Python repositories:', len(non_python_repos))
print('README.md files analyzed:', total_count)
print('README.md with copyright:', copyright_count)
print('README.md without copyright:', total_count - copyright_count)
print('Proportion:', proportion)
print('Percentage: {:.2f}%'.format(proportion * 100))

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'count': 0, 'first_five': []}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
