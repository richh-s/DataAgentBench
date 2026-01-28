code = """import json
import re

# Load the data from the files
with open('file_storage/functions.query_db:0.json', 'r') as f:
    non_python_repos_raw = json.load(f)

with open('file_storage/functions.query_db:2.json', 'r') as f:
    readme_files_raw = json.load(f)

# Extract repo names
non_python_repos = {repo['repo_name'] for repo in non_python_repos_raw}

# Filter README files for non-Python repositories and check for copyright
readme_non_python = []
for item in readme_files_raw:
    repo_name = item['sample_repo_name']
    if repo_name in non_python_repos:
        content = item['content'] or ''  # Handle None content
        # Check for copyright indicators (case-insensitive)
        has_copyright = bool(re.search(r'copyright|\©\,?\s?\d+|\(c\)\s?\d+', content, re.IGNORECASE))
        readme_non_python.append({
            'repo_name': repo_name,
            'has_copyright': has_copyright,
            'content_length': len(content)
        })

# Calculate proportion
total_readmes = len(readme_non_python)
copyright_readmes = sum(1 for item in readme_non_python if item['has_copyright'])
proportion = copyright_readmes / total_readmes if total_readmes > 0 else 0

result = {
    'total_non_python_repos': len(non_python_repos),
    'total_readme_files': total_readmes,
    'readme_files_with_copyright': copyright_readmes,
    'proportion_with_copyright': proportion
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'non_python_type': "<class 'str'>", 'readme_type': "<class 'str'>", 'non_python_preview': 'file_storage/functions.query_db:0.json', 'readme_preview': 'file_storage/functions.query_db:2.json'}}

exec(code, env_args)
